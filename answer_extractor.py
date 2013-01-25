# -*- coding: utf-8 -*-
"""


"""
import nltk.tokenize
import alchemy

from unidecode import unidecode


def extract_answers(results, answerType, keywordsList):

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
    # for answertype 'other', need coarse label too
    answerTypeOtherMap = {

    }

    answerTypePOS = [
        'code',
        'count',
        'date',
        'dist',
        'money',
        'ord',
        'perc',
        'period',
        'speed',
        'temp',
        'volsize',
        'weight'
    ]

    if answerType in answerTypeNEMap:
        rankedAnswers = alchemy.parseEntities(
            results, answerType, keywordsList)
    elif answerType in answerTypePOS:
        rankedAnswers = []
        for result in results:
            result = unidecode(u'%s' % result)
            resultTokens = nltk.tokenize.word_tokenize(result)
            resultTags = nltk.pos_tag(resultTokens)
            print '%s: %s' % (resultTokens, resultTags)
            for tag in resultTags:
                if tag[1] == 'CD':
                    print '%s, %s' % (tag, tag[0])
                    rankedAnswers.append([tag[0]])
                #if tag[1] == 'CD':
                 #   rankedAnswers.append(tag[0])
        return rankedAnswers
    else:
        rankedAnswers = [["Sorry, I can't do that yet."]]
    return rankedAnswers
