#!/bin/python

###
#
###

#### IMPORTS ####

import requests
import sys
import json
import pprint

#### VARIABLES ####

sys.tracebacklimit=0
account = sys.argv[1]

url = 'https://haveibeenpwned.com/api/v2/breachedaccount/' + account + ''

#### MAIN #### 

print ("Account checked: " + account + "\n")

try:
    response = requests.get(url)
    breachInfo = json.loads(response.content)
    print(json.dumps(breachInfo, indent=4)) 

except: 
    print ("No information found on " + account + " in the database; no known breach.")


