#!/bin/bash
#Copies file passed as $1 to Dropbox or to specific folder if $2 is used
#Note that if a file with the same name exists, it will be overwritten!
#usage with alias: toDropbox $1 $2

cp -r $1 ~/Dropbox/$2
notify-send "Moved $1 to Dropbox$2"
