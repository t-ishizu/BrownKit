#!/usr/bin/python
# coding : UTF-8
import MySQLdb
import os.path
from getpass import getpass
class Data:
    def __init__(self,database_name):
        Data.name = raw_input('your name: ')
        Data.passward = getpass('your password: ')
        Data.database_name = database_name
        conn = MySQLdb.connect(
            user=Data.name,
            passwd=Data.passward,
            db=database_name
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
        