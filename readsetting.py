#!/usr/bin/python
# coding : UTF-8

class ReadSetting:
    def __init__(self, usecyg):
        if usecyg == 0:
            self.path1 = self._get_path1_cl()
            self.path2 = self._get_path2_cl()
            self.path3 = self._get_path3_cl()
        else:
            self.path1 = self._get_path1_cgwin()
            self.path2 = self._get_path2_cgwin()
            self.path3 = self._get_path3_cgwin()

    def _get_path1_cl(self):
        setting = open("setting.txt")
        line = setting.readline()
        while line:
            if line.startswith("object project="):
                obj_path = line[15:-1]
            else:
                pass
            line = setting.readline()
        return obj_path

    def _get_path2_cl(self):
        setting = open("setting.txt")
        line = setting.readline()
        while line:
            if line.startswith("sha1.txt="):
                hash_file = line[9:-1]
            else:
                pass
            line = setting.readline()
        return hash_file

    def _get_path3_cl(self):
        setting = open("setting.txt")
        line = setting.readline()
        while line:
            if line.startswith("CCFinderX path="):
                ccfx_path = line[15:-1]
            else:
                pass
            line = setting.readline()
        return ccfx_path

    def _get_path1_cgwin(self):
        setting = open("setting.txt")
        line = setting.readline()
        while line:
            if line.startswith("object project="):
                obj_path = line[15:-2]
            else:
                pass
            line = setting.readline()
        return obj_path

    def _get_path2_cgwin(self):
        setting = open("setting.txt")
        line = setting.readline()
        while line:
            if line.startswith("sha1.txt="):
                hash_file = line[9:-2]
            else:
                pass
            line = setting.readline()
        return hash_file

    def _get_path3_cgwin(self):
        setting = open("setting.txt")
        line = setting.readline()
        while line:
            if line.startswith("CCFinderX path="):
                ccfx_path = line[15:]
            else:
                pass
            line = setting.readline()
        return ccfx_path
