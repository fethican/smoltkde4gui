#!/usr/bin/python
# -*- coding: utf-8 -*-

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
