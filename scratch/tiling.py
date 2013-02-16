# -*- coding: utf-8 -*-


l = [
    [u'Doctor', u'John', u'Pembert'],
    [u'Doctor', u'John', u'Pembert'],
    [u'Doctor', u'John', u'Pembert'],
    [u'John', u'Stith', u'Pemberton'],
    [u'John', u'Stith', u'Pemberton'],
    [u'John', u'Stith', u'Pemberton'],
    [u'John'],
    [u'Pemberton'],
    [u'Atlanta'],
    [u'Georgia'],
    [u'John', u'Pemberton'],
    [u'John', u'Pemberton'],
    [u'Columbus'],
    [u'Georgia'],
    [u'John', u'Pemberton'],
    [u'John', u'Pemberton'],
    [u'Pemberton'],
    [u'French'],
    [u'Coca-Cola', u'Company'],
    [u'Coca-Cola', u'Company'],
    [u'Coke'],
    [u'Cuba'],
    [u'North', u'Korea'],
    [u'North', u'Korea'],
    [u'Coca-Cola', u'Vanilla'],
    [u'Coca-Cola', u'Vanilla'],
    [u'Diet', u'Coke'],
    [u'Diet', u'Coke'],
    [u'Jacobs'],
    [u'Pharmacy'],
    [u'John', u'S.', u'Pemberton'],
    [u'John', u'S.', u'Pemberton'],
    [u'John', u'S.', u'Pemberton'],
    [u'Diet', u'Coke'],
    [u'Diet', u'Coke'],
    ]


from networkx.algorithms.components.connected import connected_components
from networkx import Graph
from networkx.algorithms.clique import cliques_containing_node
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import itertools

def to_graph(l):
    G = Graph()
    for clique in l:
        G.add_nodes_from(clique)
        G.add_edges_from(to_edges(clique))
    return G

def to_edges(l):
    it = iter(l)
    last = next(it)
    for current in it:
        yield last, current
        last = current

G = to_graph(l)


dd = defaultdict(int)

for entity in l:
    for token in entity:
        dd[token] += 1
top = sorted(dd.items(), key=lambda x: x[1], reverse=True)[0]

top_clique = cliques_containing_node(G, nodes=top[0])
# Flatten if multiple cliques are retrieved
top_clique = list(itertools.chain(*top_clique))

joined_entities = set(['~'.join(entity) for entity in l])
entity_lengths = [(entity, len(entity)) for entity in joined_entities]
entity_lengths = sorted(entity_lengths, key=lambda x: x[1], reverse=True)


for i in entity_lengths:
    all_tokens_contained = True
    for token in i[0].split('~'):
        if token not in top_clique:
            all_tokens_contained = False
            print 'token %s not in %s' % (token, top_clique)
    if all_tokens_contained:
        print 'made it with', i
        break



#nx.draw(G)
#plt.savefig("./graph1.png")