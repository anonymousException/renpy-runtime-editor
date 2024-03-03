# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runtime.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_runtimeDialog(object):
    def setupUi(self, runtimeDialog):
        if not runtimeDialog.objectName():
            runtimeDialog.setObjectName(u"runtimeDialog")
        runtimeDialog.resize(825, 446)
        self.oriWhatTextEdit = QTextEdit(runtimeDialog)
        self.oriWhatTextEdit.setObjectName(u"oriWhatTextEdit")
        self.oriWhatTextEdit.setGeometry(QRect(100, 60, 621, 51))
        self.oriWhatTextEdit.setReadOnly(True)
        self.label = QLabel(runtimeDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 81, 16))
        self.currentWhatTextEdit = QTextEdit(runtimeDialog)
        self.currentWhatTextEdit.setObjectName(u"currentWhatTextEdit")
        self.currentWhatTextEdit.setGeometry(QRect(100, 130, 621, 51))
        self.currentWhatTextEdit.setReadOnly(True)
        self.label_2 = QLabel(runtimeDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 150, 81, 16))
        self.wholineEdit = QLineEdit(runtimeDialog)
        self.wholineEdit.setObjectName(u"wholineEdit")
        self.wholineEdit.setGeometry(QRect(100, 20, 621, 20))
        self.wholineEdit.setReadOnly(True)
        self.label_3 = QLabel(runtimeDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 20, 31, 16))
        self.whoEditButton = QPushButton(runtimeDialog)
        self.whoEditButton.setObjectName(u"whoEditButton")
        self.whoEditButton.setGeometry(QRect(720, 20, 75, 20))
        self.oriWhatEditButton = QPushButton(runtimeDialog)
        self.oriWhatEditButton.setObjectName(u"oriWhatEditButton")
        self.oriWhatEditButton.setGeometry(QRect(720, 60, 75, 51))
        self.currentWhatEditButton = QPushButton(runtimeDialog)
        self.currentWhatEditButton.setObjectName(u"currentWhatEditButton")
        self.currentWhatEditButton.setGeometry(QRect(720, 130, 75, 51))
        self.verticalLayoutWidget = QWidget(runtimeDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 220, 781, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.replaceButton = QPushButton(runtimeDialog)
        self.replaceButton.setObjectName(u"replaceButton")
        self.replaceButton.setGeometry(QRect(330, 390, 111, 24))
        self.reloadButton = QPushButton(runtimeDialog)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setGeometry(QRect(640, 390, 141, 24))
        self.autoReloadCheckBox = QCheckBox(runtimeDialog)
        self.autoReloadCheckBox.setObjectName(u"autoReloadCheckBox")
        self.autoReloadCheckBox.setGeometry(QRect(20, 390, 211, 20))
        self.label_4 = QLabel(runtimeDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 200, 311, 16))
        self.versionLabel = QLabel(runtimeDialog)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(20, 430, 91, 16))
        self.copyrightLabel = QLabel(runtimeDialog)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setGeometry(QRect(580, 430, 241, 16))

        self.retranslateUi(runtimeDialog)

        QMetaObject.connectSlotsByName(runtimeDialog)
    # setupUi

    def retranslateUi(self, runtimeDialog):
        runtimeDialog.setWindowTitle(QCoreApplication.translate("runtimeDialog", u"Renpy Runtime Editor", None))
        self.label.setText(QCoreApplication.translate("runtimeDialog", u"original what", None))
        self.label_2.setText(QCoreApplication.translate("runtimeDialog", u"current_what", None))
        self.label_3.setText(QCoreApplication.translate("runtimeDialog", u"who", None))
        self.whoEditButton.setText(QCoreApplication.translate("runtimeDialog", u"edit", None))
        self.oriWhatEditButton.setText(QCoreApplication.translate("runtimeDialog", u"edit", None))
        self.currentWhatEditButton.setText(QCoreApplication.translate("runtimeDialog", u"edit", None))
        self.replaceButton.setText(QCoreApplication.translate("runtimeDialog", u"Replace to file(s)", None))
        self.reloadButton.setText(QCoreApplication.translate("runtimeDialog", u"Reload Game Scripts ", None))
        self.autoReloadCheckBox.setText(QCoreApplication.translate("runtimeDialog", u"Enable auto reload after replace", None))
        self.label_4.setText(QCoreApplication.translate("runtimeDialog", u"Edited List (Left-Click to re-edit ; Right-Click to delete)", None))
        self.versionLabel.setText(QCoreApplication.translate("runtimeDialog", u"Version 1.1.0", None))
        self.copyrightLabel.setText(QCoreApplication.translate("runtimeDialog", u"\u00a92024 Last moment,All rights reserved.", None))
    # retranslateUi

