#!/bin/bash

###
#
# Checks whether a given website is up (HTTP response code 200)
#
# by Fredrik Walloe
#
###

curl -Is $1 -L | grep HTTP/ | grep 200 > /dev/null 

if [ $? -eq 0 ]
	then
		echo "$1 is up" 
	else
		echo "$1 is down"
fi

