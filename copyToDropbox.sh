#!/bin/bash

####
##
## copyToDropbox.sh: simple helper script that copies a file or folder to either the Dropbox folder or a subdirectory.
## Version: 1.0
## Usage: $1 should be the file you want to move; supply $2 if you want to specify a subfolder.
##
####

cp -r $1 ~/Dropbox/$2
notify-send "Moved $1 to Dropbox$2"
