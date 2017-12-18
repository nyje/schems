#!/usr/bin/env python
import sys
i={}

f = open(sys.argv[1],"r")
c = f.read()
f.close()

import re
quoted = re.compile('(?:"(.*?)")')
for value in quoted.findall(c):
    if ":" in value:
        if not value in i.keys():
            i[value]=1
        else:
            i[value]+=1

for a in sorted(i.keys()):
    print "minetest.register_alias(\"%s\",\"\")"%(a)



