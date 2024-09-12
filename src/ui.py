# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 160)
        self.actioncopyright = QAction(MainWindow)
        self.actioncopyright.setObjectName(u"actioncopyright")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.processComboBox = QComboBox(self.centralwidget)
        self.processComboBox.setObjectName(u"processComboBox")
        self.processComboBox.setGeometry(QRect(220, 10, 341, 22))
        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(560, 10, 121, 24))
        self.onlyCheckBox = QCheckBox(self.centralwidget)
        self.onlyCheckBox.setObjectName(u"onlyCheckBox")
        self.onlyCheckBox.setGeometry(QRect(50, 10, 171, 22))
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(280, 50, 241, 24))
        self.refreshCheckBox = QCheckBox(self.centralwidget)
        self.refreshCheckBox.setObjectName(u"refreshCheckBox")
        self.refreshCheckBox.setGeometry(QRect(50, 50, 171, 22))
        self.copyrightLabel = QLabel(self.centralwidget)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setGeometry(QRect(490, 100, 241, 16))
        self.versionLabel = QLabel(self.centralwidget)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(10, 100, 91, 16))
        self.logButton = QPushButton(self.centralwidget)
        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(560, 50, 121, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 744, 21))
        self.aboutMenu = QMenu(self.menubar)
        self.aboutMenu.setObjectName(u"aboutMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.aboutMenu.menuAction())
        self.aboutMenu.addAction(self.actioncopyright)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Renpy Runtime Editor", None))
        self.actioncopyright.setText(QCoreApplication.translate("MainWindow", u"copyright", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh Process", None))
        self.onlyCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show Renpy Process Only", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.refreshCheckBox.setText(QCoreApplication.translate("MainWindow", u"Auto Refresh After Return", None))
        self.copyrightLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a92024 Last moment,All rights reserved.", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version 1.6.0", None))
        self.logButton.setText(QCoreApplication.translate("MainWindow", u"Open Log File", None))
        self.aboutMenu.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

