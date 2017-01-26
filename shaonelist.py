#!/usr/bin/python
# coding : UTF-8
import os
import os.path
import sys
import subprocess

class Sha_One_List:
    def __init__(self, object_path, sha_one_file):
        Sha_One_List.object_path = object_path
        if os.path.isfile(sha_one_file):
            pass
        else:
            print "has no file: %s", sha_one_file
            sys.exit()
        Sha_One_List.sha_one_list = []
        sha_one_stream = open(sha_one_file)
        line = sha_one_stream.readline()
        while line:
            Sha_One_List.sha_one_list.append(line[:-1])
            line = sha_one_stream.readline()
        sha_one_stream.close()

    
    def _run_cmd(self, cmd):
        ret = subprocess.check_call( cmd , shell=True)
        return ret == 0

    def get_list_size(self):
        return len(Sha_One_List.sha_one_list)

    def get_sha_one(self, performed_num):
        return Sha_One_List.sha_one_list[performed_num]

    def change_revision(self, performed_num):
        if performed_num >= len(Sha_One_List.sha_one_list):
            return False
        else:
            pass
        os.chdir(Sha_One_List.object_path)
        if self._run_cmd("git checkout " + Sha_One_List.sha_one_list[performed_num]):
            return True
        else:
            return False
