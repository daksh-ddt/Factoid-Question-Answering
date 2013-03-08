# -*- coding: utf-8 -*-
"""

"""
import os
import nltk.tokenize.punkt


class Query_builder:

    def __init__(self):
        base_path = os.path.dirname(__file__)
        stop_words_file = open(
            os.path.join(base_path, '../resources/stop_words.txt'))
        self.stop_words = [
            line.strip() for line in stop_words_file.readlines()]
        stop_words_file.close()

    def build_query(self, question):
        question = question[0].encode('ascii', 'ignore')
        tokens = nltk.wordpunct_tokenize(question)
        filtered_keywords = [
            filter(str.isalnum, token).lower() for token in tokens]
        filtered_keywords = [
            token for token in tokens if len(token) > 0]
        filtered_keywords = [
            t for t in filtered_keywords if t not in self.stop_words]
        return " ".join(filtered_keywords), filtered_keywords, tokens
