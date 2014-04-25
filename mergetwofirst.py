#!/usr/bin/env python                                                           
# -*- coding: utf-8 -*-
#
# Merge first two colums in csv file
# Tested onnnnn python3
#
# @author Per-Henrik E. Kvalnes
#
import sys

splittSym = ";"

# Open files 
filename = sys.argv[1]

try:
        infile = open(filename)
except:
        print("Can not open file: " + filename)

outfile = open(filename+"New","w")


# Travaser csv filen 
for line in infile:
    # fjern linje skift
    line = line.rstrip() 
    words = line.split(splittSym) 

    # hvis det er innhold i kollone 2, ta det med.
    if(words[1] != ""):
        newline = words[0]+" "+words[1]+";"
    else:
        newline = words[0]+";"

    i = 2
    while i < len(words):
        newline += words[i]+";"
        i += 1

        # Legg til nytt linjeskift der det skal vare
    newline += "\n"
    outfile.write(newline)


infile.close()
outfile.close()

print("New file has been written to "+filename+"New.csv")
