#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#
# Convert only big chars to small with one big first of each word
#  .csv files
#
# usage: ./firstbigchar.py <filename>
# @author Per-Henrik Kvalnes
#

filename = sys.argv[1]

try:
	f = open(filename)
except:
	print("Kan ikke aapne filen " + filename)


output = ""

for line in f:
	spchar = ","
	strings = line.split(spchar)

	#for every word in line
	for i in range(len(strings)):
		word = strings[i]
		word = word.lower()
		word = word[0].upper()+word[1:]


		output += word

		if i != len(strings)-1:
			output += spchar


print "File converted"
newfilename = filename.split(".")[0]+"new.csv"
newfile = open(newfilename, "w")
newfile.write(output)
newfile.close()
f.close()
print "New file written to "+newfilename
