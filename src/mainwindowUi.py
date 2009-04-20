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

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 477)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.defaultTableWidget = QtGui.QTableWidget(0, 2, self.tab)
        self.defaultTableWidget.setObjectName("defaultTableWidget")
        #self.defaultTableWidget.setColumnCount(2)
        #self.defaultTableWidget.setRowCount(0)
        #item = QtGui.QTableWidgetItem()
        #self.defaultTableWidget.setHorizontalHeaderItem(0, item)
        #item = QtGui.QTableWidgetItem()
        #self.defaultTableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.defaultTableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.detailedTableWidget = QtGui.QTableWidget(self.tab_2)
        self.detailedTableWidget.setObjectName("detailedTableWidget")
        self.detailedTableWidget.setColumnCount(4)
        self.detailedTableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.detailedTableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 29))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_Send = QtGui.QAction(MainWindow)
        self.action_Send.setObjectName("action_Send")
        self.action_My_Smolt_Page = QtGui.QAction(MainWindow)
        self.action_My_Smolt_Page.setObjectName("action_My_Smolt_Page")
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Privacy_Policy = QtGui.QAction(MainWindow)
        self.action_Privacy_Policy.setObjectName("action_Privacy_Policy")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Send)
        self.menu_File.addAction(self.action_My_Smolt_Page)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.action_Privacy_Policy)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        #self.defaultTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Label", None, QtGui.QApplication.UnicodeUTF8))
        #self.defaultTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "My Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Detailed Info", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Send.setText(QtGui.QApplication.translate("MainWindow", "&Send", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Send.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_My_Smolt_Page.setText(QtGui.QApplication.translate("MainWindow", "&My Smolt Page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Privacy_Policy.setText(QtGui.QApplication.translate("MainWindow", "&Privacy Policy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
