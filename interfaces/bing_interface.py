# -*- coding: utf-8 -*-
'''
An interface to the Bing Search and Synonyms APIs

'''
import urllib
import json


class Bing_interface:

    def __init__(self):
        self.composite_search = False

        # TODO move this to a file before making source public
        self.bing_account_key = 'dmeLVnBSkLXa2lQ7kSG0yFdNmu0CTXqvFy3Cij7uads='
        self.search_base_url = \
            'https://user:%s@api.datamarket.azure.com/Bing/SearchWeb/Web?' \
            % self.bing_account_key
        self.composite_base_url = \
            'https://user:%s@api.datamarket.azure.com/Bing/Search/v1/Composite?' \
            % self.bing_account_key
        self.synonyms_base_url = \
            'https://user:%s@api.datamarket.azure.com/Bing/Synonyms/GetSynonyms?' \
            % self.bing_account_key

    def search(self, query, num_results):
        if self.composite_search:
            bing_parameters = {
                "Sources": "'web'",
                "Query": "'%s'" % query,
                "Market": "'en-US'",
                "$top": num_results,
                "$format": "JSON"
            }
            queryString = urllib.urlencode(bing_parameters)
            url = self.composite_base_url + queryString
            json_data = urllib.urlopen(url)
            results = json.load(json_data)
            return results['d']['results'][0]['Web']
        else:
            bing_parameters = {
                "Query": "'%s'" % query,
                "Market": "'en-US'",
                "$top": num_results,
                "$format": "JSON"
            }
            queryString = urllib.urlencode(bing_parameters)
            url = self.search_base_url + queryString
            json_data = urllib.urlopen(url)
            results = json.load(json_data)
            return results['d']['results']

    def get_synonyms(self, query):
        bing_parameters = {
            "Query": "'%s'" % query,
            "$format": "JSON"
        }
        queryString = urllib.urlencode(bing_parameters)
        url = self.synonyms_base_url + queryString
        json_data = urllib.urlopen(url)
        results = json.load(json_data)
        return [s['Synonym'].encode("UTF-8", "ignore")
            for s in results['d']['results']]


if __name__ == "__main__":
    bing_interface = Bing_interface()
    print bing_interface.search("les paul", 4)
    #print bing_interface.get_synonyms('NYU')
