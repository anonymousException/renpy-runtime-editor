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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_runtimeForm(object):
    def setupUi(self, runtimeForm):
        if not runtimeForm.objectName():
            runtimeForm.setObjectName(u"runtimeForm")
        runtimeForm.resize(825, 456)
        self.whoEditButton = QPushButton(runtimeForm)
        self.whoEditButton.setObjectName(u"whoEditButton")
        self.whoEditButton.setGeometry(QRect(740, 10, 75, 20))
        self.label_4 = QLabel(runtimeForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 190, 311, 16))
        self.label_2 = QLabel(runtimeForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 81, 16))
        self.label_3 = QLabel(runtimeForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 31, 16))
        self.reloadButton = QPushButton(runtimeForm)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setGeometry(QRect(640, 380, 141, 24))
        self.label = QLabel(runtimeForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 81, 16))
        self.autoReloadCheckBox = QCheckBox(runtimeForm)
        self.autoReloadCheckBox.setObjectName(u"autoReloadCheckBox")
        self.autoReloadCheckBox.setGeometry(QRect(20, 380, 211, 20))
        self.replaceButton = QPushButton(runtimeForm)
        self.replaceButton.setObjectName(u"replaceButton")
        self.replaceButton.setGeometry(QRect(330, 380, 111, 24))
        self.versionLabel = QLabel(runtimeForm)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(20, 420, 91, 16))
        self.verticalLayoutWidget = QWidget(runtimeForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 210, 801, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.enhanceCheckBox = QCheckBox(runtimeForm)
        self.enhanceCheckBox.setObjectName(u"enhanceCheckBox")
        self.enhanceCheckBox.setGeometry(QRect(60, 10, 111, 20))
        self.oriWhatTextEdit = QTextEdit(runtimeForm)
        self.oriWhatTextEdit.setObjectName(u"oriWhatTextEdit")
        self.oriWhatTextEdit.setGeometry(QRect(120, 50, 621, 51))
        self.oriWhatTextEdit.setReadOnly(True)
        self.wholineEdit = QLineEdit(runtimeForm)
        self.wholineEdit.setObjectName(u"wholineEdit")
        self.wholineEdit.setGeometry(QRect(170, 10, 571, 20))
        self.wholineEdit.setReadOnly(True)
        self.oriWhatEditButton = QPushButton(runtimeForm)
        self.oriWhatEditButton.setObjectName(u"oriWhatEditButton")
        self.oriWhatEditButton.setGeometry(QRect(740, 50, 75, 51))
        self.currentWhatEditButton = QPushButton(runtimeForm)
        self.currentWhatEditButton.setObjectName(u"currentWhatEditButton")
        self.currentWhatEditButton.setGeometry(QRect(740, 120, 75, 51))
        self.currentWhatTextEdit = QTextEdit(runtimeForm)
        self.currentWhatTextEdit.setObjectName(u"currentWhatTextEdit")
        self.currentWhatTextEdit.setGeometry(QRect(120, 120, 621, 51))
        self.currentWhatTextEdit.setReadOnly(True)
        self.copyrightLabel = QLabel(runtimeForm)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setGeometry(QRect(580, 420, 241, 16))

        self.retranslateUi(runtimeForm)

        QMetaObject.connectSlotsByName(runtimeForm)
    # setupUi

    def retranslateUi(self, runtimeForm):
        runtimeForm.setWindowTitle(QCoreApplication.translate("runtimeForm", u"Renpy Runtime Editor", None))
        self.whoEditButton.setText(QCoreApplication.translate("runtimeForm", u"edit", None))
        self.label_4.setText(QCoreApplication.translate("runtimeForm", u"Edited List (Left-Click to re-edit ; Right-Click to delete)", None))
        self.label_2.setText(QCoreApplication.translate("runtimeForm", u"current_what", None))
        self.label_3.setText(QCoreApplication.translate("runtimeForm", u"who", None))
        self.reloadButton.setText(QCoreApplication.translate("runtimeForm", u"Reload Game Scripts ", None))
        self.label.setText(QCoreApplication.translate("runtimeForm", u"original what", None))
        self.autoReloadCheckBox.setText(QCoreApplication.translate("runtimeForm", u"Enable auto reload after replace", None))
        self.replaceButton.setText(QCoreApplication.translate("runtimeForm", u"Replace to file(s)", None))
        self.versionLabel.setText(QCoreApplication.translate("runtimeForm", u"Version 1.3.0", None))
        self.enhanceCheckBox.setText(QCoreApplication.translate("runtimeForm", u"Enhance Mode", None))
        self.oriWhatEditButton.setText(QCoreApplication.translate("runtimeForm", u"edit", None))
        self.currentWhatEditButton.setText(QCoreApplication.translate("runtimeForm", u"edit", None))
        self.copyrightLabel.setText(QCoreApplication.translate("runtimeForm", u"\u00a92024 Last moment,All rights reserved.", None))
    # retranslateUi

