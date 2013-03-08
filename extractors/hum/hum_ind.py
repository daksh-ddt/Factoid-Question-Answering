# -*- coding: utf-8 -*-
'''

'''
from nltk import ne_chunk
from nltk import Tree
from collections import defaultdict
from networkx.algorithms.components.connected import connected_components
from networkx import Graph
from networkx.algorithms.clique import cliques_containing_node
from collections import defaultdict
import itertools


def extract(tokens, pos_tagged_documents, ranked_docs):

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

    tokens_lowered = [t.lower() for t in tokens]
    person_freq = defaultdict(int)

    unjoined_entities = []
    for pos_tagged_doc in pos_tagged_documents:
        phrase_chunks = ne_chunk(pos_tagged_doc)
        for chunk in [c for c in phrase_chunks if hasattr(c, 'node')]:
            entity = [c[0] for c in chunk.leaves()]
            for token in entity:
                if token.lower() not in tokens_lowered:
                    unjoined_entities.append(entity)

    G = to_graph(unjoined_entities)
    token_freq = defaultdict(int)

    for entity in unjoined_entities:
        for token in entity:
            token_freq[token] += 1
    top_token = sorted(token_freq.items(), key=lambda x: x[1], reverse=True)[0]
    top_clique = cliques_containing_node(G, nodes=top_token[0])
    # Flatten if multiple cliques are retrieved
    top_clique = list(itertools.chain(*top_clique))
    joined_entities = set(['~'.join(entity) for entity in unjoined_entities])
    entity_lengths = [(entity, len(entity)) for entity in joined_entities]
    entity_lengths = sorted(entity_lengths, key=lambda x: x[1], reverse=True)\

    for i in entity_lengths:
        all_tokens_contained = True
        for token in i[0].split('~'):
            if token not in top_clique:
                all_tokens_contained = False
        if all_tokens_contained:
            answer = i[0].replace('~', ' ')
            break

    return 'factoid', answer, None, None