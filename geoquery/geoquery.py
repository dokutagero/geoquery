import sys
sys.path.insert(0,'../lib/')
import xmlToDict_functions as x2d

query_filepath = "../GC_Tr_100.xml"
training_dict = x2d.xmlToDict(query_filepath)

