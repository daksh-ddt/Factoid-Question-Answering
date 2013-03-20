# -*- coding: utf-8 -*-
"""
Modified on Mon Sep 24 19:23:50 2012

@author: gavin hackeling
"""
import os
from collections import defaultdict
from nltk import word_tokenize
from networkx.algorithms.components.connected import connected_components
from networkx import Graph
from networkx.algorithms.clique import cliques_containing_node
import matplotlib.pyplot as plt
import networkx as nx


def to_graph(l):
    G = Graph()
    for clique in l:
        G.add_nodes_from(clique)
        G.add_edges_from(to_edges(clique))
    return G


def tuples_to_graph(tuples):
    G = Graph()
    for node, attribute in tuples:
        print 'adding', node, attribute
        G.add_nodes_from(node, freq=attribute)
        G.add_edges_from(to_edges(node))
    return G


def to_edges(l):
    it = iter(l)
    last = next(it)
    for current in it:
        yield last, current
        last = current


def extract(tokens, pos_tagged_documents, ranked_docs):

    # Move to __init__
    colors_file = os.path.join(os.path.dirname(__file__),
        '../../resources/gazetteer_colors.txt')
    with open(colors_file) as f:
        colors = f.read().splitlines()

    colors = [c.lower() for c in colors]
    one_part_colors = [c for c in colors if c.count(' ')==0]

    two_part_colors = [c for c in colors if c.count(' ')==1]
    two_part_1of2 = [c.split(' ')[0] for c in two_part_colors]

    three_part_colors = [c for c in colors if c.count(' ')==2]
    three_part_1of3 = [c.split(' ')[0] for c in three_part_colors]

    four_part_colors = [c for c in colors if c.count(' ')==3]
    four_part_1of4 = [c.split(' ')[0] for c in four_part_colors]
    # Move

    answer_freq = defaultdict(int)
    # Extract candidate answers
    for doc in ranked_docs:
        doc_tokens = word_tokenize(doc.lower())
        for index, token in enumerate(doc_tokens):
            if token in one_part_colors:
                answer_freq[token] += 1
            if token in two_part_1of2:
                try:
                    possible_color = (' '.join([token, doc_tokens[index+1]]))
                    if possible_color in two_part_colors:
                        answer_freq[possible_color] += 1
                except IndexError:
                    print 'IndexError', token
            if token in three_part_1of3:
                try:
                    possible_color = (' '.join([
                        token, tokens[index+1], doc_tokens[index+2]]))
                    if possible_color in three_part_colors:
                        answer_freq[possible_color] += 1
                except IndexError:
                    print 'IndexError', token
            if token in four_part_1of4:
                print token
                try:
                    possible_color = (' '.join([
                        token, tokens[index+1],
                        doc_tokens[index+2], doc_tokens[index+3]]))
                    if possible_color in four_part_colors:
                        answer_freq[possible_color] += 1
                except IndexError:
                    print 'IndexError', token

    print '\n\n'
    answer_tuples = [a for a in answer_freq.items()]
    print 'answer tuples', answer_tuples
    #G = to_graph(unjoined_entities)
    G = tuples_to_graph(answer_tuples)
    # Then need to consolidate candidate answers
    nx.draw(G)
    plt.savefig("/home/gavin/plot.png")

    for i in answer_freq.items():
        print i
    if len(answer_freq) == 0:
        answers = ["Sorry, I could not find any answers for that."]
    else:
        answers = sorted(
            answer_freq.items(), key=lambda x: x[1], reverse=True)[0]
    print answers[0]
    return 'factoid', answers[0], answers, None