__author__ = 'jdennis'

import xmlwitch
import os
import xlrd
import readexcel

#open file, read with xlrd
#grab 1st row as header as list
#for each other row create dictionary with key being corresponding list in #1 (could be 2 dimensional list_
#send dict to function that creates xml & writes to file
xl = readexcel.readexcel('/home/tim/Dropbox/PythonXML/Ethiopia_250k_Metadata.xls')
sheetnames = xl.worksheets()
sheet = sheetnames[0]

for row in xl.getiter(sheet):
  print row
  write_xmlfile(write_to_xml(row))
  

def write_to_xml(xls_row_as_dict):
    '''takes dict representing a row in a geo xls and creates a xml str'''
	#need to persist the layerID & the callnumber+filename in sqlite db
    xml = xmlwitch.Builder()
    with xml.add(allowDups='false'):
        with xml.doc():
            xml.field("450281", name='LayerId') #need to retrieve id & increment
            xml.field(xls_row_as_dict.CALLNUMBER+xls_row_as_dict.FILENAME, name='Name')#shld be call_number & file name from xls
            xml.field('UCB', name='WorkspaceName')
            xml.field('initial collection', name='CollectionId')
            xml.field('Berkeley', name='Institution')
            xml.field('Berkeley', name='InstitutionSort')
            xml.field('Public', name='Access')
            xml.field('Polygon', name='DataType')
            xml.field('Polygon', name='DataTypeSort')
            xml.field('Online', name='Availability')
            xml.field('Napa County School District boundaries', name='LayerDisplayName')# date=year,  john will add column for location & theme 
            xml.field('Napa County School District boundaries', name='LayerDisplayNameSort') # same as above
            xml.field('UC Berkeley Libraries', name='Publisher')
            xml.field('UC Berkeley Libraries', name='PublisherSort')
            xml.field("County of Napa Assessor's Office", name='Originator')
            xml.field("County of Napa Assessor's Office", name='OriginatorSort')
            xml.field('society boundaries Schools School District Education', name='ThemeKeywords')
            xml.field('American Canyon Napa St. Helena Yountville Calistoga Napa County California', name='PlaceKeywords') # = sheetname in xls
            xml.field('Boundaries for school districts in Napa County.', name='Abstract' )
            xml.field('http://gis-gs.lib.berkeley.edu:8080/geoserver/gwc/service/wms', name='Location')
            xml.field('38.864947', name='MaxY') # in xls
            xml.field('38.153318', name='MinY') # in xls
            xml.field('-122.649217', name='MinX') # in xls
            xml.field('-122.061226', name='MaxX') # in xls
            xml.field('-122.3552215', name='CenterX')
            xml.field('38.5091325', name='CenterY')
            xml.field('0.2939954999999941', name='HalfWidth')
            xml.field('0.35581450000000103', name='HalfHeight')
            xml.field('0.4184314473389928', name='Area')
            xml.field('2000-01-01T01:01:01Z', name='ContentDate')
    return str(xml)

def write_xmlfile(xml):
	'''Takes xml string representation of row in xls and writes it to a file.'''
	print xml
