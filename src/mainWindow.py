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

from PyKDE4.kdecore import *
from PyKDE4.kdeui import *

from mainwindowUi import Ui_MainWindow
from privacyDialog import privacyDialog
from infoDialog import smoltPrivacy

from PyQt4 import Qt
from PyQt4 import QtGui
from PyQt4 import QtCore

import subprocess

from host import Host

class MainWindow(KMainWindow, Ui_MainWindow):
    def __init__(self):
        KMainWindow.__init__(self)
        self.setupUi(self)

        self.createActions()
        self.setToolBar()
        self.host = Host()

        # Set and fill the first tab.
        self.setDefaultTable()
        self.fillDefaultTable()

        # Set and fill the second tab.
        self.setDetailedTable()
        self.fillDetailedTable()

        self.smoltURL = 'http://smolt.pardus.org.tr:8090'

    def fillDefaultTable(self):
        ''' Fill the host information to the table '''
        label_list = self.host.getLabels()
        data_list = self.host.host_info()

        for item in range(len(label_list)):
            self.defaultTableWidget.insertRow(item)

            label_item = QtGui.QTableWidgetItem(label_list[item])
            #label_item.setFlags(QtCore.Qt.NoItemFlags)
            self.setRowColor(self.defaultTableWidget, label_item)
            self.defaultTableWidget.setItem(item, 0, label_item)

            _value = QtCore.QVariant(data_list[item]).toString()
            data_item = QtGui.QTableWidgetItem(_value)
            #data_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(self.defaultTableWidget, data_item)
            self.defaultTableWidget.setItem(item, 1, data_item)
            #print label_list[item], ' : ', data_list[item]

    def fillDetailedTable(self):
        ''' Fill the table with device list '''

        #devices = []
        devices = self.host.get_device_info()

        line = self.detailedTableWidget.rowCount()
        for vendorId, deviceId, subsysVendorId, subsysDeviceId, bus, driver, type, description in devices:
            self.detailedTableWidget.insertRow(line)

            bus_item = QtGui.QTableWidgetItem(bus)
            #bus_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(self.detailedTableWidget, bus_item)
            self.detailedTableWidget.setItem(line, 0, bus_item)

            driver_item = QtGui.QTableWidgetItem(driver)
            #driver_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(self.detailedTableWidget, driver_item)
            self.detailedTableWidget.setItem(line, 1, driver_item)

            type_item = QtGui.QTableWidgetItem('other')
            #type_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(self.detailedTableWidget, type_item)
            self.detailedTableWidget.setItem(line, 2, type_item)

            desc_item = QtGui.QTableWidgetItem(description)
            #desc_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(self.detailedTableWidget, desc_item)
            self.detailedTableWidget.setItem(line, 3, desc_item)
            line += 1
            #print driver

    def setDefaultTable(self):
        ''' Specifys the defaultTableWidget properties'''

        labels = QtCore.QStringList([])
        labels.append(i18n("Label"))
        labels.append(i18n("Data"))

        self.defaultTableWidget.setHorizontalHeaderLabels(labels)
        self.defaultTableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.defaultTableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.defaultTableWidget.verticalHeader().hide()
        self.defaultTableWidget.setShowGrid(False)
        self.defaultTableWidget.setSortingEnabled(False)
        #self.defaultTableWidget.setAlternatingRowColors(True)
        #self.defaultTableWidget.setAutoFillBackground(True)
        self.defaultTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.defaultTableWidget.horizontalHeader().setCascadingSectionResizes(True)

    def setDetailedTable(self):
        ''' Specifys the detailedTableWidget properties '''

        labels = QtCore.QStringList([])
        labels.append(i18n("Bus"))
        labels.append(i18n("Driver"))
        labels.append(i18n("Type"))
        labels.append(i18n("Description"))

        self.detailedTableWidget.setHorizontalHeaderLabels(labels)
        self.detailedTableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Interactive)
        self.detailedTableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Interactive)
        self.detailedTableWidget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Interactive)
        self.detailedTableWidget.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Stretch)

        self.detailedTableWidget.verticalHeader().hide()
        self.detailedTableWidget.setShowGrid(False)
        self.detailedTableWidget.setSortingEnabled(False)
        self.detailedTableWidget.setAlternatingRowColors(True)
        self.detailedTableWidget.setAutoFillBackground(True)
        self.detailedTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.detailedTableWidget.horizontalHeader().setCascadingSectionResizes(True)

    def setRowColor(self, widget, tableItem):
        ''' Set row background to two colors consecutively like KTableWidget does'''
        if widget.rowCount() % 2 == 0:
            tableItem.setBackgroundColor(QtGui.QColor('#e1e1e1')) # Light gray
        else:
            tableItem.setBackgroundColor(QtGui.QColor('#ffffff')) # White

    def setToolBar(self):
        self.toolBar.addAction(self.exitAct)
        self.toolBar.addAction(self.webAct)
        self.toolBar.addAction(self.privacyAct)
        self.toolBar.addAction(self.sendAct)

    def createActions(self):
        self.exitAct = QtGui.QAction(i18n("&Exit"), self)
        self.exitAct.setIcon(KIcon("application-exit.png"))
        self.exitAct.setShortcut("Ctrl+q")
        self.exitAct.setStatusTip(i18n("Exit Smolt without sending profile"))
        self.connect(self.exitAct, QtCore.SIGNAL("triggered()"), self.close)

        self.sendAct = QtGui.QAction(i18n("&Send my profile"), self)
        self.sendAct.setIcon(KIcon("dialog-ok-apply.png"))
        self.sendAct.setShortcut("Ctrl+S")
        self.sendAct.setStatusTip(i18n("Send my profile"))
        self.connect(self.sendAct, QtCore.SIGNAL("triggered()"), self._send)

        self.privacyAct = QtGui.QAction(i18n("Show &Privacy Policy"), self)
        self.privacyAct.setIcon(KIcon("help-about.png"))
        self.privacyAct.setShortcut("Ctrl+P")
        self.privacyAct.setStatusTip(i18n("Show the Smolt Privacy Policy"))
        self.connect(self.privacyAct, QtCore.SIGNAL("triggered()"), self.privacy)

        self.webAct = QtGui.QAction(i18n("&Go my profile page"), self)
        self.webAct.setIcon(KIcon("go-home.png"))
        self.webAct.setShortcut("Ctrl+O")
        self.webAct.setStatusTip(i18n("Take me to my smolt profile page"))
        self.connect(self.webAct, QtCore.SIGNAL("triggered()"), self.web)

        # Create actions for file and help menu
        self.connect(self.action_Send, QtCore.SIGNAL("triggered()"), self._send)
        self.connect(self.action_Exit, QtCore.SIGNAL("triggered()"), self.close)
        self.connect(self.action_Privacy_Policy, QtCore.SIGNAL("triggered()"), self.privacy)
        self.connect(self.action_My_Smolt_Page, QtCore.SIGNAL("triggered()"), self.web)
        self.connect(self.action_About, QtCore.SIGNAL("triggered()"), self.about)

        self.action_Send.setIcon(KIcon("dialog-ok-apply.png"))
        self.action_My_Smolt_Page.setIcon(KIcon("go-home.png"))
        self.action_Exit.setIcon(KIcon("application-exit.png"))

    def _send(self):
        self.proc = QtCore.QProcess()
        command = "smoltSendProfile"
        arguments = ["-a", "--submitOnly"]
        self.proc.startDetached(command, arguments)

    def privacy(self):
        self.privacyInfo = privacyDialog()
        self.privacyInfo.show()

    def web(self):
        # TODO: Get the url from smolt.
        self.private = smoltPrivacy()
        self.private.show()

    def about(self):
        self.about = QtGui.QMessageBox.about(self, i18n("About Smolt Gui"), \
                i18n("     2009 (c) Fethican Coşkuner\nSmolt KDE4 Graphical User Interface.\n\n\n  http://fedorahosted.org/smolt\n  http://code.google.com/p/smoltkde4gui\n"))
