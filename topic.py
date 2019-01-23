#!/usr/bin/env python3
# (c) Xavier Combelle here made in public domain

import re

out_s = ""
for line in open("FAQ.mdwn"):
    if line.startswith("#"):
        out_s += ("""- [{}](#{})\n""".format(
            line.strip("#").strip(),
            re.sub("\\W+", "-", line.strip("#").strip()).strip("-")))

for line in open("FAQ.mdwn"):
    out_s += line

print(out_s, end="")
