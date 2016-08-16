#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys

from PyQt5 import QtCore, QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.aboutQt()
    win = QtWidgets.QDialog()
    # widget = QtWidgets.QMainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
