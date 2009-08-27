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

import os
from urlparse import urljoin

from infoDialogUi import Ui_infoDialog

Pardus_Smolt = 'http://smolt.pardus.org.tr:8090/client/show/'

class smoltPrivacy(QDialog, Ui_infoDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.actions()
        self.setStack()

    def actions(self):
        self.connect(self.closeButton, SIGNAL("clicked()"), self.close)

    def getProfileURL(self):
        # TODO get smolt url from smolt config
        filePUuid = open('/etc/smolt/pub-uuid-smolt.pardus.org.tr', 'r')
        self.uuid = filePUuid.read().strip()
        filePUuid.close()
        if not self.uuid == '':
            self.uuid = urljoin(Pardus_Smolt, self.uuid)
            self.uuid = "<a href=\"%s\">%s</a>" % (self.uuid, self.uuid)

    def getAdminToken(self):
        fileToken = open('/etc/smolt/smolt-token-smolt.pardus.org.tr', 'r')
        self.token = fileToken.read().strip()
        fileToken.close()

    def setLink_and_admin(self):
        self.getProfileURL()
        self.getAdminToken()
        self.directUrlLabel.setText(self.uuid)
        self.Kadmin.setText(self.token)

    def setStack(self):
        self.setLink_and_admin()
        if self.uuid == '':
            self.stackedWidget.setCurrentIndex(1)

