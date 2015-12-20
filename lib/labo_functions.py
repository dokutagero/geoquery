# Group 17
# @authors: Jordi Ganzer, Nil Sanz

from lxml import etree
import labo_classes
import os

def saveQueriesToXml(listQueries, fileName):
	'''
	This function takes a list of objects of class Query `listQueries`, and saves the xml represention in the file `fileName`
	'''

	#http://stackoverflow.com/questions/3844360/best-way-to-generate-xml-in-python
	#Create root element:
	elExampleSet = etree.Element('EXAMPLE-SET')
	for i, query in enumerate(listQueries):
		elQueryno = etree.Element('QUERYNO')
		elQueryno.text = query.queryno
		elExampleSet.append(elQueryno)

		elQuery = etree.Element('QUERY')
		elQuery.text = query.query
		elExampleSet.append(elQuery)

		elLocal = etree.Element('LOCAL')
		elLocal.text = query.local
		elExampleSet.append(elLocal)

		elWhat = etree.Element('WHAT')
		elWhat.text = query.what
		elExampleSet.append(elWhat)

		elWhatType = etree.Element('WHAT-TYPE')
		elWhatType.text = query.whatType
		elExampleSet.append(elWhatType)

		elGeoRelation = etree.Element('GEO-RELATION')
		elGeoRelation.text = query.geoRelation
		elExampleSet.append(elGeoRelation)

		elWhere = etree.Element('WHERE')
		elWhere.text = query.where
		elExampleSet.append(elWhere)

		elLatLong = etree.Element('LAT-LONG')
		elLatLong.text = query.latLong
		elExampleSet.append(elLatLong)

	strXml = etree.tostring(elExampleSet, pretty_print=True)
	text_file = open(fileName, "w")
	text_file.write(strXml)
	text_file.close()