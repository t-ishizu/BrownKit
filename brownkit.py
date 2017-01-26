#!/usr/bin/python
# coding : UTF-8
import sys
import readsetting
import shaonelist
import movesourcecode
import performCCFinderX
import data
#main-routine
ARGS = sys.argv
if len(ARGS) == 1:
    print "Use Argument: (0 use command line)(1 use cygwin) "
elif int(ARGS[1]) != 0 and int(ARGS[1]) != 1:
    print "Illigal Argument: (0 use command line)(1 use cygwin) "
else:
    pass
READ_SETTING = readsetting.ReadSetting(int(ARGS[1]))
print READ_SETTING.path1# object project
print READ_SETTING.path2# sha-one text
print READ_SETTING.path3# ccfinderX path
print READ_SETTING.path4# data
print READ_SETTING.path5# working
# class.__init__()
SHA_ONE_LIST = shaonelist.Sha_One_List(READ_SETTING.path1, READ_SETTING.path2)
MOVE_SOURCE_CODE = movesourcecode.Move_Source_Code(READ_SETTING.path1, READ_SETTING.path5)
PERFORM_CCFINDERX = performCCFinderX.Perform_Ccfinderx(READ_SETTING.path3, READ_SETTING.path5)
DATA = data.Data("git_db", READ_SETTING.path3)

while(SHA_ONE_LIST.change_revision(DATA.get_performed_num())):
    MOVE_SOURCE_CODE.move_file()
    print "total " + str(SHA_ONE_LIST.get_list_size()) + " runnning " + str(DATA.get_performed_num())
    PERFORM_CCFINDERX.perform()
    DATA.register(SHA_ONE_LIST.get_sha_one(DATA.get_performed_num()))