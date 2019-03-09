#!/usr/bin/env python3
# (c) Xavier Combelle here made in public domain

import re
import sys

# * https://github.com/jch/html-pipeline/
# blob/master/lib/html/pipeline/toc_filter.rb


def add_toc(fn):
    out_s = ""
    for line in open(fn):
        if line.startswith("#"):
            # See:
            # * https://gist.github.com/asabaylus/3071099
            stripped = line.strip("#").strip()
            out_s += ("""- [{}](#{})\n""".format(
                stripped,
                re.sub("[ ]", "-",
                       re.sub("[^\\w\\- ]", "", stripped.lower())).strip("-")))

    out_s += open(fn).read()
    return out_s


open(sys.argv[1], "wt").write(add_toc("FAQ.mdwn"))
