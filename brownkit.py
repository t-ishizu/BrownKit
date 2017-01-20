#!/usr/bin/python
# coding : UTF-8
import sys
import readsetting

#main-routine
ARGS = sys.argv
if len(ARGS) == 1:
    print "Use Argument: (0 use command line)(1 use cygwin) "
elif int(ARGS[1]) != 0 and int(ARGS[1]) != 1:
    print "Illigal Argument: (0 use command line)(1 use cygwin) "
else:
    pass
READ_SETTING = readsetting.ReadSetting(int(ARGS[1]))
print READ_SETTING.path1
print READ_SETTING.path2
print READ_SETTING.path3
