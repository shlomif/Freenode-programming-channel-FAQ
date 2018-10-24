#(c) Xavier Combelle here made in public domain

import subprocess,re
for line in open("FAQ.mdwn"):
    if line.startswith("#"):
        print("""- [{}](#{})""".format(line.strip("#").strip(),re.sub("\W+","-",line.strip("#").strip()).strip("-")))
        
for line in open("FAQ.mdwn"):
    print(line,end="")
