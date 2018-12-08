#!/bin/bash

##
#
# findAll: searches for a pattern in all files in the current directory. 
# Uses /dev/null to trick grep into displaying filenames where pattern is found
#
# by Fredrik Walloe
#
##

cat *.* | grep --color -E $1 *.* /dev/null

