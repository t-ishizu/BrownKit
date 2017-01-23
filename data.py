#!/usr/bin/python
# coding : UTF-8
import MySQLdb
import os.path
from getpass import getpass
class Data:
    def __init__(self):
        Data.name = raw_input('your name: ')
        Data.passward = getpass('your password: ')
        
