#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest


class testBytes(unittest.TestCase):
    def setUp(self):
        self.byte = b'abcdefg123456'
        self.string = 'xyz890'

    def testToByte(self):
        print('==== %s ====' % 'To Byte')
        print(self.string.encode('utf-8'))

    def testToString(self):
        print('==== %s ====' % 'To String')
        print(self.byte.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
