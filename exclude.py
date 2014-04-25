#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
# Exclude lines (column1) from file1 that is not 
#  in the set of file2. 
#
# Usage: ./exclude.py <file1.csv> <file2.csv>
##################################################
import sys
SPLITTEGN = ";"

#
# Compare two line2, and line1
#
def sammenlikn(linje1, linje2):
    o1 = linje1.split(SPLITTEGN)[0]
    o2 = linje2.split(SPLITTEGN)[0]

    if(o1 == o2):
        return o1

    return 0


# Setup filenames
try:
    firstPath = sys.argv[1]
    secondPath = sys.argv[2]
except:
    print("Usage ./exclude.py <firstFile> <secondFile>")

#
# Make outfile path
#
newPath = slist[0]+"New."+slist[1]
slist = firstPath.split(".");

# Start loop 
try:
    file1 = open(firstPath,"r");
    fileout = open(newPath, "w")
except:
    print("Can not open "+firstPath)

for linje1 in file1:

    try:
        file2 = open(secondPath)
    except:
        print("Can not open "+secondPath)

    iandrefil = False
    for linje2 in file2:
        
        resultat = sammenlikn(linje1, linje2)
        if(resultat != 0):
            iandrefil = True

    if not iandrefil:
        fileout.write(linje1)

print("The result is written to: "+newPath)
