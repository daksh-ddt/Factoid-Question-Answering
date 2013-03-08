# -*- coding: utf-8 -*-
import json
import answer_classifier as classifier
from model import answer as Answer
import query_builder
import bing_interface
import document_creator
import answer_extractor as ae


class Factoid_handler:

    def __init__(self):
        self.query_builder = query_builder.Query_builder()
        self.bing_interface = bing_interface.Bing_interface()
        self.answer_classifier = classifier.Answer_classifier()
        self.answer_extractor = ae.Answer_extractor()

    def answer(self, question):
        # Create Answer object
        # This will be serialized and returned after it is processed.
        answer = Answer.Answer(question)

        # Predict coarse and fine answer types
        answer.predicted_coarse, answer.predicted_fine = \
            self.answer_classifier.predict_answer_type(question)

        # Build a query
        answer.query, filtered_keywords, tokens = \
            self.query_builder.build_query(question)
        print 'Query', answer.query

        # Retrieve search results from Bing
        search_results = self.bing_interface.search(answer.query, 10)

        # Extract snippets from the search results
        ranked_docs, pos_tagged_documents = document_creator.create(
            search_results, filtered_keywords, tokens)

        # Rank the candidate answers
        answer.question_type, \
        answer.best_answer, \
        answer.all_answers, \
        answer.supplement \
        = self.answer_extractor.extract_answers(
            tokens,
            pos_tagged_documents,
            ranked_docs,
            answer.predicted_coarse,
            answer.predicted_fine,
            filtered_keywords,
            True,
        )

        # Populate, serialize and return the Answer
        response = json.dumps(vars(answer), sort_keys=True, indent=4)
        return response