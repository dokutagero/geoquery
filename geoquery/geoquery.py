import sys
sys.path.insert(0,'../lib/')
import xmlToDict_functions as x2d
import dbPediaInterface as dbpi

query_filepath = "../GC_Tr_100.xml"
training_dict = x2d.xmlToDict(query_filepath)

query_list = []
# Storing the queries in a list.
# The structure of each training_dict element is {#id : {tags}}
for k,v in training_dict.iteritems():
    print v['QUERY']
    query_list.append(v['QUERY'])

# Testing DBPedia accessor
for q in query_list:
    print dbpi.isLocation(q)

