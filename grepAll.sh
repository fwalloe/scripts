#!/bin/bash

##
#
# Searches for pattern in all files in the current position. 
# Uses /dev/null to trick grep into displaying filenames where pattern is found
#
# by Fredrik Walløe
#
##

cat *.* | grep --color -E $1 *.* /dev/null

