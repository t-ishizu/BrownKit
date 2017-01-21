#!/usr/bin/python
# coding : UTF-8
import os.path
import sys

class Sha_One_List:
    def __init__(self, sha_one_file):
        if os.path.isfile(sha_one_file):
            pass
        else:
            print "has no file: %s", sha_one_file
            sys.exit()
        Sha_One_List.sha_one_list = []
        sha_one_stream = open(sha_one_file)
        line = sha_one_stream.readline()
        while line:
            Sha_One_List.sha_one_list.append(line[:-2])
            line = sha_one_stream.readline()
        sha_one_stream.close()
