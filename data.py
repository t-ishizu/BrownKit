#!/usr/bin/python
# coding : UTF-8
import MySQLdb
import os.path
import sys
from getpass import getpass
class Data:
    def __init__(self,database_name,output_path):
        Data.output_path = output_path
        Data.name = raw_input('your name: ')
        Data.passward = getpass('your password: ')
        Data.database_name = database_name
        conn = MySQLdb.connect(
            user=Data.name,
            passwd=Data.passward,
            db=Data.database_name
        )

        cursor = conn.cursor()

        sql = 'show tables'
        cursor.execute(sql)
        tables = cursor.fetchall()
        if len(tables) > 0:
            find = False
            for (table_name,) in cursor:
                if table_name == "revision_tb":
                    find = True
            if find:
                pass
            else:
                print 'true'
                cursor.execute('create table revision_tb (id int,sha1 char(40), LOC int, SLOC int, CLOC int, CVRL float,  file_num int)')
        else:
             cursor.execute('create table revision_tb (id int,sha1 char(40), LOC int, SLOC int, CLOC int, CVRL float,  file_num int)')
        cursor.execute('select * from revision_tb')
        results = cursor.fetchall()
        Data.version_num = len(results)    
        conn.commit()
        cursor.close()
        conn.close()
 
    def get_performed_num(self):
        return Data.version_num

    def register(self, sha_one):
        conn = MySQLdb.connect(
            user=Data.name,
            passwd=Data.passward,
            db=Data.database_name
        )
        line_metrics_file = Data.output_path + '\linemetrics.tsv'
        if os.path.isfile(line_metrics_file):
            pass
        else:
            print "has no file: " +  line_metrics_file
            sys.exit()
        stream = open(line_metrics_file)
        line = stream.readline()
        # first line skip
        line = stream.readline()
        file_num = 0
        loc = 0
        sloc = 0
        cloc = 0
        while line:
            line_list = line[:-1].split('\t')
            file_num += 1
            loc += int(line_list[1])
            sloc += int(line_list[2])
            cloc += int(line_list[3])
            line = stream.readline()
        stream.close()

        cursor = conn.cursor()
        sql = "insert into revision_tb values(\'" + str(self.get_performed_num()+1) +"\',\'" + sha_one + "\',\'" + str(loc) + "\',\'" + str(sloc) + "\',\'" + str(cloc) + "\',\'" + str(float(cloc)/sloc) + "\',\'" + str(file_num) + "\')"
        print sql
        cursor.execute(sql)

        cursor.execute('select * from revision_tb')
        results = cursor.fetchall()
        Data.version_num = len(results)    
        conn.commit()
        cursor.close()
        conn.close()