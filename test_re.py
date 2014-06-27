#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import re
import unittest


class testRegex(unittest.TestCase):
    def setUp(self):
        self.teststr = """
        <img recindex='00001' alt='abc' />other1
        <img recindex='00002' alt='abc' />other2
        <img recindex='00003' alt='abc' />other3
        <img recindex='00004' alt='abc' />other4
        <img recindex='00005' alt='abc' />other5

        """

    def replfunc(self, mo):
        m = mo.group(1)
        print('match str: %s' % m)
        return '<img src="img_%s"' % m

    def testrepl(self):
        print('origin str: %s' % self.teststr)
        pattern = r'''<img\s+recindex=['"](\d+)['"]'''
        regex = re.compile(pattern)
        mo = regex.sub(self.replfunc, self.teststr)
        print('replace str: %s' % mo)


if __name__ == '__main__':
    unittest.main()
