#!/bin/python

import urllib.request

baseURL='https://www.archlinux.org/news/'

req = urllib.request.Request(
	baseURL,
	data=None,
	headers={
		'User-Agent': 'Arch Update - News Checker'
	}
)

f = urllib.request.urlopen(req)
print (f.read().decode('utf-8'))

