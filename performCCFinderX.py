#!/usr/bin/python
# coding : UTF-8
import sys

args = sys.argv
print 'loading...' + args[1]
f=open(args[1])
line = f.readline()

while line:
	print line
	line = f.readline()
f.close