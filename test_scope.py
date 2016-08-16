#!/usr/bin/env python
# -*- encoding:utf-8 -*-


import unittest


class testLanguage(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIf(self):
        print('==== %s ====' % 'if scope')
        if True:
            data = 123
            print('inside', data)
        print('outside', data)

    def testWith(self):
        print('==== %s ====' % 'with scope')
        f = 123
        print('outside:', f)
        with open('test_scope.py') as f:
            data = 456
            print('inside:', f)
            print('inside data', data)
        print('outside', f)
        print('outside data', data)

    def testFor(self):
        print('==== %s ====' % 'for scope')
        for c in range(0, 10):
            print('inside: %d' % c)
        print('outside: %d' % c)


if __name__ == '__main__':
    unittest.main()
