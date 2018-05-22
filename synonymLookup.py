#!/bin/python

###
# synonymLookup.py: lets users find synonyms for the words they pass to the script as arguments
# usage: ./synonymLookup.py WORD
###

# encoding errors can be fixed  by exporting lc_all with utf-8
from bs4 import BeautifulSoup
from lxml import html
import requests
import sys
page = requests.get("http://www.thesaurus.com/browse/"+sys.argv[1])

soup = BeautifulSoup(page.content, 'lxml')

soup.prettify()

print ("Synonyms for " + sys.argv[1] + ":")
synonymNumber = 1
for definition in soup.find_all("a", class_="css-ebz9vl e1s2bo4t1"):
    print (str(synonymNumber) + ": " + str(definition.text).strip(), " ", )
    synonymNumber += 1


