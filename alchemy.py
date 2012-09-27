# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""
import urllib
import json
from collections import defaultdict

disambiguatedAnswerWeight = 2

# Map of Classifier Answer Types to NE types
answerTypeNEMap = {
    "ind" : ["person"],
    "city" : ["city"],
    "country" : ["country", "StateOrCounty"],
    "mount" : ["GeographicFeature", "Mountain", "MountainPass", "MountainRange"],
    "state" : ["StateOrCounty"],
    "other" : ["Continent", "country", "city", "stateorcounty", "GeographicFeature"],
    "gr" : ["Organization"],
    "cremat" : ["PrintMedia", "RadioProgram", "RadioStation", "TelevisionShow", "TelevisionStation",
                "MusicGroup", "Movie"],
    "techmeth" : ["Technology"],
    "religion" : ["ReligiousOrganization", "ReligiousOrder"],
    "sport" : ["Sport"],
    "dismed" : ["HealthCondition"]
}


# Read the Alchemy API key
alchemyEndpoint = 'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?'
alchemyApiKeyFile = open("api_key.txt", "r")
#alchemyApiKeyFile = open("/home/ubuntu/www/api_key.txt", "r")
alchemyApiKey = alchemyApiKeyFile.read()
alchemyApiKeyFile.close()

def parseEntities(results, answerType, apphome):
    answerFrequencies = defaultdict(int)
    for result in results:
        alchemyParameters = {
            "apikey" : "693f8f0aa9e91878fa2644d2de3735323bf1a35d",
            "text" : result['text'].encode('utf-8'),
            "outputMode" : "json"
            }
        alchemyQueryString = urllib.urlencode(alchemyParameters)
        alchemyURL = alchemyEndpoint + alchemyQueryString
        # get JSON seach results from Alchemy
        alchemy_json_data = urllib.urlopen(alchemyURL)
        alchemy_data = json.load(alchemy_json_data)
        for entity in alchemy_data['entities']:
            if 'disambiguated' in entity:
                entityName = entity['disambiguated']['name']
                for possibleAnswerType in answerTypeNEMap[answerType]:
                    print 'Possible answer types include %s' % possibleAnswerType
                    if entity['type'].lower() == possibleAnswerType:
                        print 'Candidate answer (disambiguated): %s' % entityName
                        answerFrequencies[entityName] += disambiguatedAnswerWeight
            else:
                entityName = entity['text']
                for possibleAnswerType in answerTypeNEMap[answerType]:
                    print 'Possible answer types include %s' % possibleAnswerType
                    if entity['type'].lower() == possibleAnswerType:
                        print 'Candidate answer (disambiguated): %s' % entityName
                        answerFrequencies[entityName] += disambiguatedAnswerWeight
                
#                print 'Candidate answer (ambiguous): %s' % entityName
#                answerFrequencies[entityName] += 1

        print answerFrequencies
        rankedAnswers = sorted(answerFrequencies.iteritems(), reverse=True)
        
    return rankedAnswers
    
    
    
    
    
    
    
    
    
    
    