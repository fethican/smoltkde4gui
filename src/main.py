#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyKDE4.kdeui import *
from PyKDE4.kdecore import *
from about import aboutData
from smoltKdeGui import MainWindow


if __name__ == "__main__":
	
    KCmdLineArgs.init(sys.argv, aboutData)

    app = KApplication()

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()
