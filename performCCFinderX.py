#!/usr/bin/python
# coding : UTF-8
import sys
import os
import subprocess

def run(cmd):
    	ret = subprocess.check_call( cmd , shell=True)
	return ret == 0


setting = open("setting.txt")
line = setting.readline()
while line:
    	print line
	if line.startswith("object project="):
		objPath = line[15:-1]
	elif line.startswith("sha1.txt="):
		hashFile = line[9:-1]
	elif line.startswith("CCFinderX path="):
		ccfxPath = line[15:-1]
	else:
		pass
	line = setting.readline()
setting.close
stream = open(hashFile)
line = stream.readline()
os.chdir(objPath)
if run("git checkout " + line):
	while line:
		line = stream.readline()
	stream.close