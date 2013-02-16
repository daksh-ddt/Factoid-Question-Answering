# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""
import urllib
import json
from collections import defaultdict


# TODO incorporate document ranking into entity score
def extract(tokens, pos_tagged_documents, ranked_docs):
    answer_freq = defaultdict(int)
    for doc in ranked_docs:
        parameters = {
            "apikey": "693f8f0aa9e91878fa2644d2de3735323bf1a35d",
            "text": doc.encode('utf-8', 'replace'),
            "outputMode": "json"
            }
        base_url = \
        'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?'
        encoded_parameters = urllib.urlencode(parameters)
        url = base_url + encoded_parameters
        json_data = urllib.urlopen(url)
        data = json.load(json_data)
        for entity in data['entities']:
            if entity['type'].lower() == 'person':
                if 'disambiguated' in entity:
                    entity_name = entity['disambiguated']['name']
                    answer_freq[entity_name] += 1
                else:
                    entity_name = entity['text']
                    answer_freq[entity_name] += 1

    #print answer_freq

    answer = sorted(
        answer_freq.items(), key=lambda x: x[1], reverse=True)[0]
    return answer[0]




#def parseEntities(results, answerType, keywordsList):
    #answerFrequencies = defaultdict(int)



        ## get JSON seach results from Alchemy
        ##alchemy_json_data = urllib.urlopen(alchemyURL)
        ##alchemy_data = json.load(alchemy_json_data)

        #for entity in alchemy_data['entities']:
            #if 'disambiguated' in entity:
                #entityName = entity['disambiguated']['name'].encode('ascii', 'replace')
                #for possibleAnswerType in answerTypeNEMap[answerType]:
                    #print 'Possible answer types include %s' % possibleAnswerType
                    #if entity['type'].lower() == possibleAnswerType:
                        #print 'Candidate answer (disambiguated): %s' % entityName
                        #sentences = sent_tokenize(result)
                        #for sentence in sentences:
                            #print 'Sentence: %s' % unidecode(sentence)
                            #if entityName in sentence:
                                #matches = [key for key in keywordsList if (key.lower() in sentence.lower())]
                                #weight = len(matches) / len(keywordsList) * len(matches) * disambiguatedAnswerWeight
                                #print 'Entity: %s: %s' % (entityName, weight)
                                #answerFrequencies[entityName] += weight
                            #else:
                                #answerFrequencies[entityName] += 0.1
            ##else:
                ##entityName = entity['text']
                ##for possibleAnswerType in answerTypeNEMap[answerType]:
                    ##print 'Possible answer types include %s' % possibleAnswerType
                    ##if entity['type'].lower() == possibleAnswerType:
                        ##print 'Candidate answer (disambiguated): %s' % entityName.encode('ascii', 'replace')
                        ##sentences = sent_tokenize(result)
                        ##for sentence in sentences:
                            ##print 'Sentence: %s' % unidecode(sentence)
                            ##if entityName in sentence:
                                ##matches = [key for key in keywordsList if (key.lower() in sentence.lower())]
                                ##print matches
                                ##weight = len(matches) / len(keywordsList) * len(matches) * disambiguatedAnswerWeight
                                ##print 'Entity: %s: %s' % (entityName, weight)
                                ##answerFrequencies[entityName] += weight
                            ##else:
                                ##answerFrequencies[entityName] += 0.1

        ##print answerFrequencies
        ###rankedAnswers = answerFrequencies.sort(key=lambda x: x[1])
        ##rankedAnswers = sorted(answerFrequencies.iteritems(), key=lambda (k,v): v, reverse=True)
        ##print '\n', rankedAnswers

    ##return rankedAnswers
##