#!/bin/bash

####
##
## checkUpdates.sh: detects and prints the number of packages that are out of date; meant to be used with Polybar, where the displayed message will change colour depending on whether any packages are out of date. 
## Created by: Fredrik Walloe
##
####

#updates=$(pacman -Qu | wc -l)

pacman -Qu | awk 'END { print (NR == 0 ? "%{F#555}0 packages%{F-}" : "%{F#ffb52a}"NR " %{F-}"  "%{F#ffb52a}package" (NR > 1 ? "s%{F-}" : "")); }'
