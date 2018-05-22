#!/bin/python
# encoding errors can be fixed  by exporting lc_all with utf-8
from bs4 import BeautifulSoup
from lxml import html
import requests
import sys
page = requests.get("http://www.dictionary.com/browse/" + sys.argv[1] + "?s=t")

soup = BeautifulSoup(page.content, 'lxml')

#print(soup.prettify())

print("==============================")
print("Definitions of " + sys.argv[1])
print("==============================\n")


soup.prettify()
#definition=soup.find_all("div", class_="def-content")

entryNumber = 1

for definition in soup.find_all("div", class_="def-content"):
    if str("see: ") not in definition.text:
        print (str(entryNumber) + ": ", str(definition.text).strip() + "\n")
        entryNumber +=1

