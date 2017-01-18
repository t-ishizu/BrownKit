#!/usr/bin/python
# coding : UTF-8
import sys
import subprocess

args = sys.argv
print 'loading... ' + args[1]+'/../sha1.txt'
hashFile=open(args[1]+"/../sha1.txt")
line = hashFile.readline()

while line:
	print line	
	line = hashFile.readline()
hashFile.close