#!/usr/bin/python
# -*- coding: utf-8 -*-

# smoltkde4gui - KDE4 user interface for Smolt
#
# Copyright (C) 2009,  Fethican Coşkuner
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Please read the COPYING file.

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
