#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

# import re
import unittest

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
            output_text = ""
            while len(sections.xpath_results):
                section = sections.xpath_results.pop(0)
                id2 = section.get(id_attr)
                title_xpath = './db:title/text()'
                docbook5_title_list = section.xpath(
                    title_xpath, namespaces=ns
                )
                docbook5_title = docbook5_title_list[0]
                count_parent_section_elements = 0
                parent = section
                while parent is not None:
                    tag = lxml.etree.QName(parent).localname
                    print(tag)
                    if tag == 'section':
                        count_parent_section_elements += 1
                    parent = parent.getparent()
                assert count_parent_section_elements > 0
                output_text += "{}* [{}](#{})\n".format(
                    ("    " * (count_parent_section_elements - 1)),
                    docbook5_title, id2)
            print(output_text)
            return output_text

        _process_sections()
        if 0:
            for section in sections.xpath_results:
                print(section.get(id_attr))


if __name__ == '__main__':
    from pycotap import TAPTestRunner
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    TAPTestRunner().run(suite)
