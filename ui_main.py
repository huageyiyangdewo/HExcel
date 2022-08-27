# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'handle.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.directoryLayout = QHBoxLayout()
        self.directoryLayout.setObjectName(u"directoryLayout")
        self.directoryButton = QPushButton(self.centralwidget)
        self.directoryButton.setObjectName(u"directoryButton")

        self.directoryLayout.addWidget(self.directoryButton)

        self.directoryText = QLabel(self.centralwidget)
        self.directoryText.setObjectName(u"directoryText")

        self.directoryLayout.addWidget(self.directoryText)

        self.directoryLineText = QLineEdit(self.centralwidget)
        self.directoryLineText.setObjectName(u"directoryLineText")

        self.directoryLayout.addWidget(self.directoryLineText)

        self.directoryLayout.setStretch(0, 2)
        self.directoryLayout.setStretch(1, 1)
        self.directoryLayout.setStretch(2, 5)

        self.verticalLayout.addLayout(self.directoryLayout)

        self.fileLayout = QHBoxLayout()
        self.fileLayout.setObjectName(u"fileLayout")
        self.fileButton = QPushButton(self.centralwidget)
        self.fileButton.setObjectName(u"fileButton")

        self.fileLayout.addWidget(self.fileButton)

        self.fileText = QLabel(self.centralwidget)
        self.fileText.setObjectName(u"fileText")

        self.fileLayout.addWidget(self.fileText)

        self.fileLineText = QLineEdit(self.centralwidget)
        self.fileLineText.setObjectName(u"fileLineText")

        self.fileLayout.addWidget(self.fileLineText)

        self.fileLayout.setStretch(0, 2)
        self.fileLayout.setStretch(1, 1)
        self.fileLayout.setStretch(2, 5)

        self.verticalLayout.addLayout(self.fileLayout)

        self.ProcessLayout = QHBoxLayout()
        self.ProcessLayout.setObjectName(u"ProcessLayout")
        self.processButton = QPushButton(self.centralwidget)
        self.processButton.setObjectName(u"processButton")

        self.ProcessLayout.addWidget(self.processButton)

        self.processText = QLabel(self.centralwidget)
        self.processText.setObjectName(u"processText")

        self.ProcessLayout.addWidget(self.processText)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.ProcessLayout.addWidget(self.progressBar)

        self.ProcessLayout.setStretch(0, 5)
        self.ProcessLayout.setStretch(1, 1)
        self.ProcessLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.ProcessLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.directoryButton.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u5904\u7406\u7684\u6587\u4ef6\u5939", None))
        self.directoryText.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u4f4d\u7f6e:", None))
        self.fileButton.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u914d\u7f6e\u6587\u4ef6", None))
        self.fileText.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4f4d\u7f6e:", None))
        self.processButton.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u5f00\u59cb\u5904\u7406", None))
        self.processText.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u8fdb\u5ea6:", None))
    # retranslateUi

