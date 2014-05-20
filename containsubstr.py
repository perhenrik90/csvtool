#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################
# Sort out rows with substring
#
#  @author Per-Henrik Kvalnes
##################################

import sys

try:
    inPath = sys.argv[1]
    searchKey = sys.argv[2]
except:
    print("Usage ./containsubstr.py <csvfile> <substring>")


slist = inPath.split(".");
newPath = slist[0]+"New."+slist[1]

try:
    inFile = open(inPath, "r")
    outFile = open(newPath, "w")
except:
    print("Can not open "+inFile)

for line in inFile:
    if searchKey in line:
        outFile.write(line)

inFile.close()
outFile.close()
