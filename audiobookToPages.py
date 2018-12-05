#!/usr/bin/python

####
##
## audiobookToPages.py: gives an estimate number of pages based on how many hours you've listened to an audiobook. 
## Created by: Fredrik Walloe 
## Version: 1.0
##
####

hours_listened = input('Enter hours listened: ')
length_of_book = input('Enter length of audiobook in hours: ')
number_of_pages = input('Enter length of the book in pages: ')

percent_listened = (float(hours_listened) / float(length_of_book)) * 100
pages_read = (float(number_of_pages) / float(length_of_book)) * float(hours_listened)

print ("You've listened for " + str(hours_listened) + " hours, which represents " + str(pages_read) + " pages (or " + str(percent_listened) + "%)")
