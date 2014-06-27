#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest


class testRange(unittest.TestCase):
    def setUp(self):
        self.b = 0
        self.e = 10

    def testrange(self):
        print('==== %s ====' % 'range')
        a = range(self.b, self.e)
        print(a)

    def testxrange(self):
        print('Note: no xrange in python3')
        print('==== %s ====' % 'xrange')
        a = xrange(self.b, self.e)
        print(a)
        print('==== %s ====' % 'list(xrange)')
        print(list(a))

    def testxrange2(self):
        print('Note: no xrange in python3')
        print('==== %s ====' % 'for xrange')
        for val in xrange(self.b, self.e):
            print(val)


if __name__ == '__main__':
    unittest.main()
