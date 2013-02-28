# -*- coding: utf-8 *-*
'''
{
"question": ["who was the first president"]
}

'''
import os
import json
import tornado.web
import tornado.ioloop
from tornado.options import define, options
import answer_classifier as classifier
from model import answer as Answer
import query_builder
import bing_interface
import document_creator
import answer_extractor as ae


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('ask_get.html')

    def post(self):
        # Retrieve the question
        data_json = tornado.escape.json_decode(self.request.body)
        question = [data_json['question']]
        print 'Question:', question

        # Create Answer object
        # This will be serialized and returned after it is processed.
        answer = Answer.Answer(question)

        # Predict coarse and fine answer types
        answer.predicted_coarse, answer.predicted_fine = \
            answer_classifier.predict_answer_type(question)

        # Build a query
        answer.query, filtered_keywords, tokens = \
            query_builder.build_query(question)
        print 'Query', answer.query

        # Retrieve search results from Bing
        search_results = bing_interface.search(answer.query, 10)

        # Extract snippets from the search results
        ranked_docs, pos_tagged_documents = document_creator.create_documents(
            search_results, filtered_keywords, tokens)

        # Rank the candidate answers
        ranked_answers = answer_extractor.extract_answers(
            tokens,
            pos_tagged_documents,
            ranked_docs,
            answer.predicted_coarse,
            answer.predicted_fine,
            filtered_keywords,
            True,
        )

        print ranked_answers
        # Populate, serialize and return the Answer
        answer.best_answer = ranked_answers
        #answer.all_answers = ranked_answers
        response = json.dumps(
            vars(answer), sort_keys=True, indent=4)
        self.write(response)


handlers = [
            (r"/", MainHandler),
            ]


settings = dict(template_path=os.path.join(
    os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8009, help="run on the given port", type=int)


if __name__ == "__main__":
    query_builder = query_builder.Query_builder()
    bing_interface = bing_interface.Bing_interface()
    answer_classifier = classifier.Answer_classifier()
    answer_extractor = ae.Answer_extractor()
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
