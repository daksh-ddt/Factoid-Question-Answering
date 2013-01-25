# -*- coding: utf-8 -*-
'''

'''
import urllib
import json


class Bing_interface:

    def __init__(self):
        self.bingAccountKey = 'dmeLVnBSkLXa2lQ7kSG0yFdNmu0CTXqvFy3Cij7uads='
        self.bingBaseURL = \
            'https://user:%s@api.datamarket.azure.com/Bing/SearchWeb/Web?' % \
            self.bingAccountKey

    def search(self, query):
        bing_parameters = {
            "Query": "'%s'" % query,
            "Market": "'en-US'",
            "$top": "50",
            "$format": "JSON"
        }
        queryString = urllib.urlencode(bing_parameters)
        url = self.bingBaseURL + queryString
        print url
        json_data = urllib.urlopen(url)
        results = json.load(json_data)
        return results


if __name__ == "__main__":
    bing_interface = Bing_interface()
    print bing_interface.search("les paul")
