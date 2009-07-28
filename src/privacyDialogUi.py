# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/privacyPolicy.ui'
#
# Created: Fri Jul 24 00:50:21 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_privacyDialog(object):
    def setupUi(self, privacyDialog):
        privacyDialog.setObjectName("privacyDialog")
        privacyDialog.resize(435, 390)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/smolt-icon-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        privacyDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(privacyDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(privacyDialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(privacyDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(privacyDialog)
        QtCore.QMetaObject.connectSlotsByName(privacyDialog)

    def retranslateUi(self, privacyDialog):
        privacyDialog.setWindowTitle(QtGui.QApplication.translate("privacyDialog", "Privacy Policy", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("privacyDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Smolt will only send hardware and basic operating system information to the Pardus smolt server (smoon).  The only tie from the database to a submitters machine is the UUID.  As long as the submitter does not give out this UUID the submission is anonymous.  If at any point in time a user wants to delete their profile from the database they need only run</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-style:italic;\">smoltDeleteProfile</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   The information sent to the smolt database server should be considered public in that anyone can view the statistics, data and share machine profiles.  In  many ways smolt is designed to get hardware vendors and other 3rd parties attention.  As such, not only will this information be shared with 3rd parties, we will be using smolt as leverage to gain better support for open source drivers and better support in general.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">IP Logging:</span>  In Pardus\'s smolt install all web traffic goes through a proxy server first.  This is the only place IP addresses are being logged and they are kept on that server for a period of 4 weeks at which time log rotation removes these logs.  The Pardus Project does not aggregate ip addresses in the smolt database.  These logs are private and will not be available to the general public.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Users unhappy with this policy should simply not use smolt.  Users with questions about this policy should contact the Pardus Infrastructure Team at admin [at] pardus.org.tr  Also remember that users can delete their profiles at any time using \"<span style=\" font-style:italic;\">smoltDeleteProfile</span>\"</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("privacyDialog", "&Close", None, QtGui.QApplication.UnicodeUTF8))

