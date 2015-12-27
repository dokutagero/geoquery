import sys
sys.path.insert(0,'../lib/')
import xmlToDict_functions as xml2dict
import dbPediaInterface as dbpi
import labo_classes
from labo_functions import saveQueriesToXml


# Geo-relations
geo_relations = ["in", "on", "of","near", "next to", around", "along",
                 "at", "from", "to", "within", "north of", "south of",
                 "east of", "west of", "northeast of", "northwest of",
                 "southeast of", "southwest of", "north to", "east to",
                 "west to", "northeast to", "northwest to",
                 "southeast to"]


query_filepath = "../GC_Tr_100.xml"
training_dict = xml2dict.xmlToDict(query_filepath)

query_list = []
# Storing the queries in a list.
# The structure of each training_dict element is {#id : {tags}}
for k,v in training_dict.iteritems():
    print v['QUERY']
    query_list.append(v['QUERY'])

# Data pre-processing
query_list = [query.lower() for query in query_list]


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

saveQueriesToXml(out_geotags, '../test/miau.xml')

