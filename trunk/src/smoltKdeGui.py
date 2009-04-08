#!/usr/bin/python
# -*- coding: utf-8 -*-

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

        self.setDefaultTable()
        #self.run()
        self.fillDefaultTable()

    '''def run(self):
        p = subprocess.Popen(["smoltSendProfile", "-p"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.replace('\t','')

        out = str(out).splitlines()

        #self.defaultTableWidget.resizeColumnToContents(0)
        #self.defaultTableWidget.resizeColumnToContents(1)


        defaultData = []
        detailedData = {}

        for line in range(19):
            label, data = out[line].split(':')
            defaultData.append([label, data])

        # setting column number via outer for
        col = 0
        line = 0
        for row in defaultData:
            self.defaultTableWidget.insertRow(line)
            for column in row:
                item = QtGui.QTableWidgetItem(column)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.setRowColor(item)
                self.defaultTableWidget.setItem(line, col, item)
                col = 1
            col = 0
            line += 1'''

    def fillDefaultTable(self):
        label_list = self.host.getLabels()
        data_list = self.host.host_info()

        for item in range(len(label_list)):
            self.defaultTableWidget.insertRow(item)

            label_item = QtGui.QTableWidgetItem(label_list[item])
            label_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(label_item)
            self.defaultTableWidget.setItem(item, 0, label_item)

            data_item = QtGui.QTableWidgetItem(data_list[item])
            data_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setRowColor(data_item)
            self.defaultTableWidget.setItem(item, 1, data_item)
            print label_list[item], ' : ', data_list[item]


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
        self.defaultTableWidget.setAlternatingRowColors(True)
        self.defaultTableWidget.setAutoFillBackground(True)

    def setRowColor(self, tableItem):
        ''' Set row background to two colors consecutively like KTableWidget does'''
        if self.defaultTableWidget.rowCount() % 2 == 0:
            tableItem.setBackgroundColor(QtGui.QColor('#e1e1e1')) # Light gray
        else:
            tableItem.setBackgroundColor(QtGui.QColor('#ffffff')) # White

