#!/usr/bin/python
# coding : UTF-8
import os
import subprocess

class Perform_Ccfinderx:
	def __init__(self, detector_path, working_path):
		self.detector_path = detector_path
		self.working_path = working_path

	def perform(self):
    		os.chdir(self.detector_path)
    		self._run_ccfx(self.detector_path + '/ccfx.exe d cpp -dn ' + self.working_path)
    		self._run_ccfx(self.detector_path + '/ccfx.exe p ' + self.detector_path + '/a.ccfxd -o clonepair.tsv')
		self._run_ccfx(self.detector_path + '/ccfx.exe m ' + self.detector_path + '/a.ccfxd -c -o clonemetrics.tsv')
		self._run_ccfx(self.detector_path + '/ccfx.exe m ' + self.detector_path + '/a.ccfxd -w -o linemetrics.tsv')

	def _run_cmd(self, cmd):
    		ret = subprocess.check_call( cmd , shell=True)
		return ret == 0

	def _run_ccfx(self, cmd):
    		ret = subprocess.check_call(cmd)
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
