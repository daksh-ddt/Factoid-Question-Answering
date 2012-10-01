# -*- coding: utf-8 -*-
"""
ShallowQA v0.5 Alder

Modified on Mon Oct 1 19:23:50 2012

@author: gavin hackeling

"""

import alchemy

def parseEntities(results, answerType, apphome):
    
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
    
    if answerType in answerTypeNEMap:
        rankedAnswers = alchemy.parseEntities(results, answerType, apphome)
    else:
        rankedAnswers = [["Sorry, I can't do that yet."]]
    return rankedAnswers