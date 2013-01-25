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
import answer_extractor


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hello")

    def post(self):
        data_json = tornado.escape.json_decode(self.request.body)
        question = data_json['question']
        answer = Answer.Answer(question)
        # Predict coarse and fine answer types
        answer.predicted_coarse, answer.predicted_fine = \
            answer_classifier.predict_answer_type(question)

        # Build a query
        answer.query, filtered_keywords = query_builder.build_query(question)

        search_results = bing_interface.search(answer.query)

        documents = document_creator.create_documents(
            search_results, 10, filtered_keywords)

        ranked_answers = answer_extractor.extract_answers(
            documents, answer.predicted_fine, filtered_keywords)

        answer.best_answer = ranked_answers[0]
        answer.all_answers = ranked_answers
        response = json.dumps(
            vars(answer), sort_keys=True, indent=4)
        self.write(response)


handlers = [
            (r"/", MainHandler),
            ]


settings = dict(template_path=os.path.join(
    os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8000, help="run on the given port", type=int)


if __name__ == "__main__":
    query_builder = query_builder.Query_builder()
    bing_interface = bing_interface.Bing_interface()
    answer_classifier = classifier.Answer_classifier()
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
