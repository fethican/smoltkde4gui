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

from PyQt4 import Qt
from PyQt4 import QtGui
from PyQt4 import QtCore

import subprocess

from host import Host

class MainWindow(KMainWindow, Ui_MainWindow):
    def __init__(self):
        KMainWindow.__init__(self)
        self.setupUi(self)

        self.host = Host()

        # Set and fill the first tab.
        self.setDefaultTable()
        self.fillDefaultTable()

        # Set and fill the second tab.
        self.setDetailedTable()
        self.fillDetailedTable()

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

            data_item = QtGui.QTableWidgetItem(data_list[item])
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

