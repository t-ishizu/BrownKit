#!/usr/bin/python
# coding : UTF-8
import os
import subprocess

class Perform_CCFinderX:
	def __init__(self, detector_path, working_path):
		self.detector_path = detector_path
		self.working_path = working_path

	def perform(self):
    		os.chdir(self.detector_path)
    		if self._run_cmd('ccfx d cpp -dn ' + self.working_path):
    			print 'create a.ccfxd'

	def _run_cmd(self, cmd):
    		ret = subprocess.check_call( cmd , shell=True)
		return ret == 0

#setting = open("setting.txt")
#line = setting.readline()
##	if line.startswith("object project="):
#		objPath = line[15:-1]
#	elif line.startswith("sha1.txt="):
#		hashFile = line[9:-1]
#	elif line.startswith("CCFinderX path="):
#		ccfxPath = line[15:-1]
#	else:
#		pass
#	line = setting.readline()
#setting.close
#stream = open(hashFile)
#line = stream.readline()
#os.chdir(objPath)
#if run("git checkout " + line):
#	while line:
#		line = stream.readline()
#	stream.close
