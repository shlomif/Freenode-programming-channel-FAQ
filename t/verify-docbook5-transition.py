#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import re
import unittest

import html_unit_test
from html_unit_test import ns


class MyTests(html_unit_test.TestCase):
    def test_initial_docbook(self):
        input_fn = './first-version-of-docbook5-FAQ.docbook5.xml'
        doc = self.doc(input_fn, filetype='docbook5')
        sections = doc.xpath('//db:section')
        id_attr = '{xml}id'.format(xml=("{" + ns['xml'] + "}"))

        def _compare_ids():
            NO_SQ = "(?:[^\\[\\]]*?)"
            MARKDOWN_TOC_LINE_RE = (
                "^ *\\* \\[((?:" + NO_SQ + "|(?:\\[" + NO_SQ + "\\])"
                ")*)\\]\\(#([^\\)]+?)\\)$"
            )
            markdown_fn = (
                "FAQ_with_ToC__generated-"
                "before-docbook5-transiton.md"
            )
            with open(markdown_fn) as md_fh:
                for line in md_fh:
                    if line == "# Freenode programming channel FAQ\n":
                        return True
                    m = re.match(MARKDOWN_TOC_LINE_RE, line)
                    self.assertTrue(m, "match")
                    # title = m[1]
                    want_id = m[2]
                    section = sections.xpath_results.pop(0)
                    id2 = section.get(id_attr)
                    self.assertEqual(want_id, id2, "IDs match")
            assert False

        _compare_ids()
        if 0:
            for section in sections.xpath_results:
                print(section.get(id_attr))


if __name__ == '__main__':
    from pycotap import TAPTestRunner
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    TAPTestRunner().run(suite)
