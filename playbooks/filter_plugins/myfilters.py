#!/usr/bin/python
import re
class FilterModule(object):
    def filters(self):
        return {
            'buildvalue': self.buildvalue
        }

    def buildvalue(self, nfile, srch):
        f = open (nfile, 'r')
        sfile = f.readline()
        x = re.search(srch + '-*[0-9]*', sfile)
        rep = srch + ('-1' if '-' not in x.group() else '-' + str((int(x.group().split('-')[1]) + 1))) 
        return rep
