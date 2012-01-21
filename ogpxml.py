__author__ = 'jdennis'

import xmlwitch

xml = xmlwitch.Builder()
with xml.add(allowDups='false'):
    with xml.doc():
        xml.updated('2003-12-13T18:30:02Z')
        xml.name('John Doe')
print(xml)