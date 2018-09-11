# -*- coding: utf-8 -*-
# @Author: kyqiao
# @Date:   2018-08-27 17:16:39
# @Last Modified by:   kyqiao
# @Last Modified time: 2018-09-11 18:48:40
import re


class readf(object):
    def __init__(self, file, up_marker, down_marker, skipdata=0):
        super(readf, self).__init__()
        self.file = file
        self.up_marker = up_marker
        self.down_marker = down_marker
        self.start = False
        self.skipdata = -skipdata

    def readfile(self):
        output = open('test.txt', 'w')
        with open(file) as f:
            for line in f.readlines():
                if not self.start:
                    matchobj = re.search(self.up_marker, line)
                    if matchobj:
                        if self.skipdata > -1:
                            output.write(line)
                            self.start = True
                        else:
                            self.skipdata += 1
                else:
                    matchobj = re.search(self.down_marker, line)
                    if not matchobj:
                        output.write(line)
                    else:
                        self.start = False
                        output.close()
                        break


if __name__ == '__main__':
    file = r'log.lammps'
    up_marker = r'Step Temp'
    down_marker = r'Loop time'
    test = readf(file, up_marker, down_marker, skipdata=1)
    test.readfile()
