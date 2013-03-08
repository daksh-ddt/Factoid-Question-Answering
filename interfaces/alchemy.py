# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""
import os
import urllib
import json
from collections import defaultdict
from nltk.tokenize import sent_tokenize
from unidecode import unidecode

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


def parseEntities(results, answerType, keywordsList):
    answerFrequencies = defaultdict(int)
    base_path = os.path.dirname(__file__)
    # Read the Alchemy API key
    alchemyEndpoint = 'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?'
    alchemyApiKeyFile = open(os.path.join(base_path, 'api_key.txt'))
    alchemyApiKey = alchemyApiKeyFile.read()
    alchemyApiKeyFile.close()

    for result in results:
        alchemyParameters = {
            "apikey": "693f8f0aa9e91878fa2644d2de3735323bf1a35d",
            "text": result,
            "outputMode": "json"
            }
        alchemyQueryString = urllib.urlencode(alchemyParameters)
        alchemyURL = alchemyEndpoint + alchemyQueryString
        # get JSON seach results from Alchemy
        alchemy_json_data = urllib.urlopen(alchemyURL)
        alchemy_data = json.load(alchemy_json_data)

        for entity in alchemy_data['entities']:
            if 'disambiguated' in entity:
                entityName = entity['disambiguated']['name'].encode('ascii', 'replace')
                for possibleAnswerType in answerTypeNEMap[answerType]:
                    print 'Possible answer types include %s' % possibleAnswerType
                    if entity['type'].lower() == possibleAnswerType:
                        print 'Candidate answer (disambiguated): %s' % entityName
                        sentences = sent_tokenize(result)
                        for sentence in sentences:
                            print 'Sentence: %s' % unidecode(sentence)
                            if entityName in sentence:
                                matches = [key for key in keywordsList if (key.lower() in sentence.lower())]
                                weight = len(matches) / len(keywordsList) * len(matches) * disambiguatedAnswerWeight
                                print 'Entity: %s: %s' % (entityName, weight)
                                answerFrequencies[entityName] += weight
                            else:
                                answerFrequencies[entityName] += 0.1
            else:
                entityName = entity['text']
                for possibleAnswerType in answerTypeNEMap[answerType]:
                    print 'Possible answer types include %s' % possibleAnswerType
                    if entity['type'].lower() == possibleAnswerType:
                        print 'Candidate answer (disambiguated): %s' % entityName.encode('ascii', 'replace')
                        sentences = sent_tokenize(result)
                        for sentence in sentences:
                            print 'Sentence: %s' % unidecode(sentence)
                            if entityName in sentence:
                                matches = [key for key in keywordsList if (key.lower() in sentence.lower())]
                                print matches
                                weight = len(matches) / len(keywordsList) * len(matches) * disambiguatedAnswerWeight
                                print 'Entity: %s: %s' % (entityName, weight)
                                answerFrequencies[entityName] += weight
                            else:
                                answerFrequencies[entityName] += 0.1

        print answerFrequencies
        #rankedAnswers = answerFrequencies.sort(key=lambda x: x[1])
        rankedAnswers = sorted(answerFrequencies.iteritems(), key=lambda (k,v): v, reverse=True)
        print '\n', rankedAnswers

    return rankedAnswers
