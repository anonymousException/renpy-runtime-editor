import webbrowser

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from copyright import Ui_CopyrightDialog


class MyCopyrightForm(QDialog, Ui_CopyrightDialog):
    def __init__(self, parent=None):
        super(MyCopyrightForm, self).__init__(parent)
        self.setupUi(self)
        self.url_label.setStyleSheet(
            "QLabel::hover"
            "{"
            "background-color : lightgreen;"
            "}"
        )
        self.url_label.setStyleSheet("color:blue")
        self.url_label.mousePressEvent = self.open_url

        self.url_label.setCursor(Qt.PointingHandCursor)

    def open_url(self, event):
        webbrowser.open(self.url_label.text())