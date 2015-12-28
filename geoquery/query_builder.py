import nltk

def local_tagger(query):

    #Natural Language Processing With Python chapter 7
    query_tokens = nltk.word_tokenize(query)
    query_pos = nltk.pos_tag(query_tokens)

    grammar = r"""
        NP: {<DT>?<JJ>*<NN.*>+<DT>?<JJ>*<NN.*>*}
        """
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(query_pos)
    print result

    np_subtrees = list(result.subtrees(filter=lambda x: x.label()=='NP'))

    islocal = []
    dbpedia_queries = []
    for np_subtree in np_subtrees:
            dbpedia_queries.append([tagged_word[0] for tagged_word in np_subtree.leaves() ])

    return dbpedia_queries