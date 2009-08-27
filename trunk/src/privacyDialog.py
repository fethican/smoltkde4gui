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

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from privacyDialogUi import Ui_privacyDialog

class privacyDialog(QDialog, Ui_privacyDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.actions()

    def actions(self):
        self.connect(self.closeButton, SIGNAL("clicked()"), self.close)
