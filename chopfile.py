#!/usr/bin/env python                                                           
# -*- coding: utf-8 -*-
#
# Chop csv file in equal partitions
#
# @author Per-Henrik Kvalnes

import sys

partitionSize = 3

filename = sys.argv[1]

try:
    infile = open(filename)
except:
    print("Can not open file: "+ filename)

nLines = 0
nFile  = 0
outfile = None

for line in infile:
    if(nLines % partitionSize == 0):
        if(outfile != None): outfile.close()
        outfilename = "output"+str(nFile)+".csv"
        outfile = open(outfilename,"w")
        print("Chop to file "+outfilename)
        nFile += 1

    outfile.write(line)
    nLines += 1

infile.close()
