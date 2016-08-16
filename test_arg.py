#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import argparse
import unittest


class testArgs(unittest.TestCase):
    def setUp(self):
        self.args = (
            ['--foo', 'abc', 'abcdefg.ext'],
            ['-a', 'abc', '-a', 'bcd', '-a', 'cde', 'def.def'],
            ['-vvvv', 'abc.ea'],
            #['--version'],
        )
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--foo', help='foo help', default='foo')
        self.parser.add_argument('-a', '--all', help='all help', action='append')
        self.parser.add_argument('-v', '--verbose', help='verbose help', action='count')
        #self.parser.add_argument('--version', action='version', version='%(prog)s 0.3')
        self.parser.add_argument('file', help='add filename')

    def testargs(self):
        for args in self.args:
            print('args: ', args)
            pargs = self.parser.parse_args(args)
            print(pargs)

if __name__ == '__main__':
    unittest.main()
