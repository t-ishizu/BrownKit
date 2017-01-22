#!/usr/bin/python
# coding : UTF-8
import os
import shutil
import fnmatch

class Move_Source_Code:
    def __init__(self, object_path, working_path):
        self.object_path = object_path
        self.working_path = working_path

    def delete_working(self):
        if os.path.exists(self.working_path):
            shutil.rmtree(self.working_path)
        else:
            pass

    def create_working(self):
        if os.path.exists(self.working_path):
            self.delete_working()
        else:
            pass
        os.mkdir(self.working_path)

    def move_file(self):
        file_list = self._get_file_list()
        self.create_working()
        for file_name in file_list:
            shutil.copyfile(file_name, self.working_path + "/" + os.path.basename(file_name))

    def _get_file_list(self):
        file_list = []
        for(root, dirs, files) in os.walk(self.object_path):
            for file_name in files:
                target = os.path.join(root, file_name).replace("\\", "/")
                if os.path.isfile(target):
                    if fnmatch.fnmatch(os.path.basename(target), '*.c') or \
                    fnmatch.fnmatch(os.path.basename(target), '*.h'):
                        file_list.append(target)
        return file_list
