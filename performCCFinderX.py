#!/usr/bin/python
# coding : UTF-8
import sys
import os
import subprocess

args = sys.argv
print 'loading... ' + args[1]+'/../sha1.txt'
hashFile=open(args[1]+"/../sha1.txt")
line = hashFile.readline()
os.chdir(args[1])
cmd1 = "git checkout " + line
ret1 = subprocess.check_call( cmd1 , shell=True)
print ret1 == 0
while line:
	#print line
	line = hashFile.readline()
hashFile.close