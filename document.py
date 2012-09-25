# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:19:05 2012

@author: gavin
"""

class Document(object):
    def __init__(self, text, fine, coarse, id):
        self.text = text;
        self.fine = fine
        self.coarse = coarse
        self.id = id