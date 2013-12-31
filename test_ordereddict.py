#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from ordereddict import OrderedDict
import unittest


class testDict(unittest.TestCase):
    def setUp(self):
        self.test_list = [
            ('title', 'title name'),
            ('creationdate', '2013-12'),
            ('author', 'unknown'),
            ('publisher', 'public domain')
        ]

    def testordereddict(self):
        udict = {}
        for name, value in self.test_list:
            udict[name] = value
        for key in udict:
            print(key, udict[key])


class testOrderedDict(unittest.TestCase):
    def setUp(self):
        self.test_list = [
            ('title', 'title name'),
            ('creationdate', '2013-12'),
            ('author', 'unknown'),
            ('publisher', 'public domain')
        ]

    def testordereddict(self):
        odict = OrderedDict()
        for name, value in self.test_list:
            odict[name] = value
        print('==== ordered dict ====')
        for key in odict:
            print(key, odict[key])


if __name__ == '__main__':
    unittest.main()
