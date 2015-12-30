import nltk

def local_tagger(queries):

    #Natural Language Processing With Python chapter 7
    queries_tokens = [nltk.word_tokenize(query) for query in queries]
    queries_pos = [nltk.pos_tag(token) for token in queries_tokens]
    #query_tokens = nltk.word_tokenize(query)
    #query_pos = nltk.pos_tag(query_tokens)

    #grammar = r"""
    #    NP: {<DT>?<JJ>*<NN.*>+<DT>?<JJ>*<NN.*>*}
    #    """

    # Una o mas preposiciones, determinante opcional y uno o mas nombres.
    grammar = r"""
            PP: {<IN>+<DT>?<NN>+}
            """
    cp = nltk.RegexpParser(grammar)
    result = []
    for query_pos in queries_pos:
        result.append(cp.parse(query_pos))
    #result = cp.parse(query_pos)
    for r in result:
        print r

    print "************************************************************************************ \n\n"
    #np_subtrees = list(result.subtrees(filter=lambda x: x.label()=='PP'))
    np_subtrees2 = [list(r.subtrees(filter=lambda x: x.label()=='PP')) for r in result]
    i=0
    non_detected = []
    for r in result:
        if !(r.subtrees(filter=lambda x: x.label()=='PP')):

            non_detected.append(i)

        i += 1
    np_subtrees3 = [list(r.subtrees(filter=lambda x: x.label()!='PP')) for r in result]


    islocal = []
    dbpedia_queries = []
    for np_subtrees in np_subtrees2:
        for np_subtree in np_subtrees:
                dbpedia_queries.append([tagged_word[0] for tagged_word in np_subtree.leaves() ])
                print np_subtree

    print "************************************************************************************ \n\n"


    for np_subtrees in np_subtrees3:
        for np_subtree in np_subtrees:
                dbpedia_queries.append([tagged_word[0] for tagged_word in np_subtree.leaves() ])
                print np_subtree

    return dbpedia_queries