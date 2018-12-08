#!/bin/python

####
##
## synonymLookup.py: lets users find synonyms for the words they pass to the script as arguments; can fail if a word has multiple possible meanings. 
## usage: ./synonymLookup.py WORD
## Note: if this stops working that likley means the class name for synonyms have changed on the website. Use the Inspect tool in your browser to find the correct class name for the synonyms 
## 
####

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
for definition in soup.find_all("a", class_="css-3kshty etbu2a31"):
    print (str(synonymNumber) + ": " + str(definition.text).strip(), " ", )
    synonymNumber += 1


