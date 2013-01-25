# -*- coding: utf-8 -*-
"""

"""
import nltk.tokenize.punkt


class Query_builder:

    def __init__(self):
        stop_words_file = open('resources/stop_words.txt', 'r')
        self.stop_words = [
            line.strip() for line in stop_words_file.readlines()]
        stop_words_file.close()

    def build_query(self, question):
        question = question[0].encode('ascii', 'ignore')
        keywords = nltk.wordpunct_tokenize(question)
        filtered_keywords = [
            filter(str.isalnum, token).lower() for token in keywords]
        filtered_keywords = [
            token for token in keywords if len(token) > 0]
        filtered_keywords = [
            t for t in filtered_keywords if t not in self.stop_words]
        return " ".join(filtered_keywords), filtered_keywords
