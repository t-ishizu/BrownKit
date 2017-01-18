#!/usr/bin/python
# coding : UTF-8
import sys

args = sys.argv
print 'loading...' + args[1]
hashFile=open(args[1])
line = hashFile.readline()

while line:
	print line
	line = hashFile.readline()
hashFile.close