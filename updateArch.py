#!/usr/bin/python

#### 
##
## updateArch.py: displays news from archlinux.org/news/ that are relevant to your update; will display all news items since your last update and let you know whether the software mentioned in the news appears to be installed on your machine.
## Created by Fredrik Walløe
##
####

#### IMPORTS ####
import subprocess
from bs4 import BeautifulSoup
from lxml import html
import requests
import time
import re

#### Functions ####

# Attempts to check whether software mentioned in Arch Linux News is installed on the machine; prints a warning if so. 
def isInstalled(text):
    installedSoftware = subprocess.Popen(["pacman -Qe"], stdout=subprocess.PIPE, shell=True)
    installedSoftware = str(installedSoftware.stdout.read(), 'utf-8')

    for line in installedSoftware.split("\n"):
        if text in line:
            print("Software mentioned in news (" + line + ") may be installed") 

#### Get date of last update ####

# Figure out when system was last updated; note that the use of 'grep -a git' is necessary here because grep treats parto f pacman.log as a non-text file. 
lastUpdate = subprocess.Popen(["grep -a git /var/log/pacman.log | awk '{print FNR $1}' | grep -o '....-..-..' | tail -1"], stdout=subprocess.PIPE, shell=True)

lastUpdate = str(lastUpdate.stdout.read(), 'utf-8')

# Use strptime so that update time can be compared with time of news items; only news items after this date are relevant
previousUpdate = time.strptime(lastUpdate.strip(), "%Y-%m-%d")

# Give this information to the user
print ("\n====================================")
print("Date of last update: " + str(lastUpdate).strip())
print ("====================================\n")

#### Get news since last update and display them ####

url = requests.get("https://www.archlinux.org/news/")
soup = BeautifulSoup(url.content, 'lxml')

soup.prettify()
news = soup.find_all("div", class_="news-article-list.box")
date = None

# Require user interaction only if there are relevant news since last update 
newsSinceLastUpdate = False

# Go through every news item and display ones that are relevant for this update
for newsItem in soup.find_all("td"):
    dateOfNewsItem = re.search(r'(\d{4}-\d{2}-\d{2})', str(newsItem))
    itemDate = dateOfNewsItem.group(0) if dateOfNewsItem else 'NOTADATE'
    itemDate = str(itemDate).replace("['", '').replace("']", '').replace('\n', '')

    # Print the date 
    if date is not None:
        print (str(date) + ": " + newsItem.text)
        date = None
        newsSinceLastUpdate = True
      

    # When newsItem contains a date
    if itemDate is not 'NOTADATE':
   #     print (itemDate.strip())
        itemDate = time.strptime(itemDate, "%Y-%m-%d")
        if itemDate > previousUpdate:
            date=newsItem.text
            isInstalled(newsItem.text)
    else:
        itemDate = ""



#### Require user interaction if there are news ####

if newsSinceLastUpdate:
    proceed = input("\nProceed with update?\t")
else:
    proceed = "y"

#### Proceed with update ####

if str("y") in proceed:
    subprocess.call(["sudo pacman -Syyyyu"], shell=True)

