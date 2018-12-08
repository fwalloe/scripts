#!/usr/bin/python

####
##
## createDocumentation.py: automagically creates documentation for all files in the current folder by extracting this documentation line from all files. 
## Created by: Fredrik Walloe
## Creation date: 8-12-2018
## Version: 0.1
## Status: Incomplete
##
## Usage: run the script in the folder that contains the files you want to document; for this to work, all files must have a line that contains the file name followed by a colon and then a discription of what the script does. It is this line that will be automatically extracted. 
##
####

#### IMPORTS ####
import glob

#### VARIABLES ####
documentationLines = []

#### FUNCTIONS ####

#### MAIN ####

# Loop through all files in the folder
for filepath in glob.iglob('./*'):
    # Document python and bash scripts
    if filepath.endswith(".py") or filepath.endswith(".sh"):
        fileName = filepath.split("/")[-1]
        # Open each file and loop through it to find the documentation line
        with open(fileName, "r") as currentFile:
            for line in currentFile:
                # Ensures that we've found the right line
                if fileName + ":" in line:
                    # Get rid of the hashtags and store the documentation for later
                    documentationLines.append(line.replace("#", ""))


with open("./README.md", "w") as f:
    f.write("## A collection of scripts by Fredrik Walløe ##\n\n")

    f.write("This repository contains " + str(len(documentationLines)) + " scripts that are summarized below.\n\n")

    # Write each documentation line; use the filename as a headline.
    for script in documentationLines:
        f.write("# " + script.split(":")[0] + " #\n")
        f.write(script.split(":")[1] + "\n")
