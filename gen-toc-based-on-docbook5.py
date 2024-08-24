#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import re

import argparse
import sys
import lxml.etree

import html_unit_test
from html_unit_test import ns


class MyTests(html_unit_test.TestCase):
    def test_initial_docbook(self):
        input_fn = './FAQ.docbook5.xml'
        doc = self.doc(input_fn, filetype='docbook5')
        sections = doc.xpath('//db:section')
        id_attr = '{xml}id'.format(xml=("{" + ns['xml'] + "}"))

        def _process_sections():
            _toc_text = ""
            while len(sections.xpath_results):
                section = sections.xpath_results.pop(0)
                id2 = section.get(id_attr)
                title_xpath = './db:title/text()'
                docbook5_title_list = section.xpath(
                    title_xpath, namespaces=ns
                )
                docbook5_title = docbook5_title_list[0]
                docbook5_title = re.sub('\\n', ' ', docbook5_title)
                assert '\n' not in id2
                if id2 == 'what-is-the-channel-for-topictechnology':
                    docbook5_title = \
                        "What is the channel for <em>TOPIC</em>/TECHNOLOGY?"
                count_parent_section_elements = 0
                parent = section
                while parent is not None:
                    tag = lxml.etree.QName(parent).localname
                    if tag == 'section':
                        count_parent_section_elements += 1
                    parent = parent.getparent()
                assert count_parent_section_elements > 0
                _toc_text += "{}* [{}](#{})\n".format(
                    (" " * (3 * (count_parent_section_elements - 1))),
                    docbook5_title, id2)
            return _toc_text

        return _process_sections()


def main(argv):
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--output', type=str, required=True,
                        help='output filename')
    parser.add_argument('--input', type=str, required=True,
                        help='Input filename')
    args = parser.parse_args(argv[1:])
    out_s = ''
    with open(args.input, "rt") as fh:
        out_s += fh.read()
    output_toc = MyTests().test_initial_docbook()
    output_text = output_toc + out_s

    with open(args.output, "wt") as ofh:
        ofh.write(output_text)


if __name__ == '__main__':
    main(sys.argv)
