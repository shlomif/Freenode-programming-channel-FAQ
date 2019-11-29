#!/usr/bin/env python3
# (c) Xavier Combelle here made in public domain

import argparse
import subprocess
import sys

# * https://github.com/jch/html-pipeline/
# blob/master/lib/html/pipeline/toc_filter.rb


def add_toc(fn):
    out_s = subprocess.Popen(
        ["bash", "-c", "./github-markdown-toc/gh-md-toc - < " + fn],
        stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    out_s += open(fn).read()
    return out_s


def main(argv):
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--output', type=str, required=True,
                        help='output filename')
    parser.add_argument('--input', type=str, required=True,
                        help='Input filename')
    args = parser.parse_args(argv[1:])
    open(args.output, "wt").write(add_toc(args.input))


main(sys.argv)
