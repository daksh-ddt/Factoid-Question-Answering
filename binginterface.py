# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:12:33 2012

@author: gavin
"""
import urllib
import json

# Bing API
bingAccountKey = 'dmeLVnBSkLXa2lQ7kSG0yFdNmu0CTXqvFy3Cij7uads='
bingBaseURL = '@api.datamarket.azure.com/Bing/SearchWeb/Web?'

def search(query):
    print 'Searching Bing for %s' % query
    bingParameters = {
        "Query" : query,
        "Market" : "'en-US'",
        "$top" : "50",
        "$format" : "JSON"
    }
    queryString = urllib.urlencode(bingParameters)
    url = 'https://user:' + bingAccountKey + bingBaseURL + queryString
    print url
    # get JSON seach results from Bing
    json_data = urllib.urlopen(url)
    data = json.load(json_data)
    
    
    
    
    
    return data