#!/usr/bin/env python3
# (c) Xavier Combelle here made in public domain

import re


def add_toc(fn):
    out_s = ""
    for line in open(fn):
        if line.startswith("#"):
            out_s += ("""- [{}](#{})\n""".format(
                line.strip("#").strip(),
                re.sub("\\W+", "-", line.strip("#").strip()).strip("-")))

    out_s += open(fn).read()
    return out_s


print(add_toc("FAQ.mdwn"), end="")
