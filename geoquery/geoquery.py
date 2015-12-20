import sys
sys.path.insert(0,'../lib/')
import xmlToDict_functions as xml2dict
import dbPediaInterface as dbpi
import labo_classes
from labo_functions import saveQueriesToXml

query_filepath = "../GC_Tr_100.xml"
training_dict = xml2dict.xmlToDict(query_filepath)

query_list = []
# Storing the queries in a list.
# The structure of each training_dict element is {#id : {tags}}
for k,v in training_dict.iteritems():
    print v['QUERY']
    query_list.append(v['QUERY'])

# Testing DBPedia accessor
islocal = []
for q in query_list:
    print dbpi.isLocation(q)
    #generic_location = (dbpi.isLocation(q) | dbpi.isCountry(q) | dbpi.isCity(q) | dbpi.isRegion(q))
    islocal.append(dbpi.isLocation(q))

islocal_output = ['YES' if elem==True else 'NO' for elem in islocal]

# Output XML file
i=0
out_geotags = []
for q in query_list:
    element = labo_classes.Query(str(i),q,islocal_output[i],"","","","","")
    out_geotags.append(element)
    i+=1

saveQueriesToXml(out_geotags, 'miau.xml')

