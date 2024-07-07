#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.

import unittest

import html_unit_test
from html_unit_test import ns


class MyTests(html_unit_test.TestCase):
    def test_initial_docbook(self):
        input_fn = './first-version-of-docbook5-FAQ.docbook5.xml'
        doc = self.doc(input_fn, filetype='docbook5')
        sections = doc.xpath('//db:section')
        id_attr = '{xml}id'.format(xml=("{" + ns['xml'] + "}"))

        for s in sections.xpath_results:
            print(s.get(id_attr))


if __name__ == '__main__':
    from pycotap import TAPTestRunner
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    TAPTestRunner().run(suite)
