#!/usr/bin/python
# coding : UTF-8
import sys
from getpass import getpass
import MySQLdb
#main-routine
ARGS = sys.argv
if len(ARGS) == 1 or len(ARGS)  > 2:
    print "Use Argument: DATABASE_NAME with revision_tb "
else:
    pass
database_name = ARGS[1]
name = raw_input('your name: ')
passward = getpass('your password: ')
conn = MySQLdb.connect(
    user=name,
    passwd=passward,
    db=database_name
)

cursor = conn.cursor()

sql = "select * from revision_tb"
cursor.execute(sql)
records = cursor.fetchall()
sha_list = []
sloc_list = []
cloc_list = []
clone_per_list = []
for record in records:
    sha_list.append(record[1])
    sloc_list.append(record[3])
    cloc_list.append(record[4])
    clone_per_list.append(record[5])
cursor.close()
conn.close()
index_list = []
pre_cloc = cloc_list[0]
#pre_clone_per = clone_per_list[0]
for index in range(1, len(clone_per_list)-1):
    if(pre_cloc < cloc_list[index]):
        index_list.append(index)
    #if(0.005<clone_per_list[index]-pre_clone_per):
        #index_list.append(index)
    else:
        pass
    #pre_clone_per = clone_per_list[index]
    pre_cloc = cloc_list[index]
for index in index_list:
    print "new :"+ str(index-1) + " " + sha_list[index-1] + " " + str(clone_per_list[index-1]) + " "+ str(sloc_list[index-1]) + " " + str(cloc_list[index-1])
    print "old :" +str(index) + " " + sha_list[index] + " " + str(clone_per_list[index])  + " "+ str(sloc_list[index]) + " " + str(cloc_list[index]) + "\n"
