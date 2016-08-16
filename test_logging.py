#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest
import logging


class testBytes(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(format='%(levelname)s:%(levelno)s:%(lineno)d:%(funcName)s:%(message)s', level=20)

    def testWarning(self):
        logging.warning('test 中文')

    def testInfo(self):
        logging.info('test')

    def testOtherlevel(self):
        logging.debug('test')
        logging.error('test')
        logging.critical('test')


if __name__ == '__main__':
    unittest.main()
