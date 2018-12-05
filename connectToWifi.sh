#!/bin/bash

####
##
## connectToWifi.sh: either scans or connects to a wirless network using nmcli. 
## Created by: Fredrik Walloe
## Version 1.0
## Usage: supply 'scan' as an argument to scan for nearby networks. Otherwise, supply SSID as $1 and password as $2 
##
####

scan="scan"

if [ "$scan"="$1" ]
then
	nmcli dev wifi list
else
	echo "Connecting to $1"
	nmcli dev wifi connect $1 password $2
fi
