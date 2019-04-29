"""Main UI screen"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QToolButton, QTextEdit, QPushButton, QComboBox)

class PrimaryWindow(QMainWindow):
    """Class containing the main ui window"""

    def __init__(self):
        super().__init__()

        self._folder_choice = None
        self._folder_textbox = None
        self._sort_bybox = None
        self._sort_button = None

        self.load_mainwindow()

    def load_mainwindow(self):
        """Loads the main window ui"""

        app = QApplication(sys.argv)
        self._folder_choice = QToolButton("FolderChoice", self)
        self._folder_textbox = QTextEdit("FolderTextbox", self)
        self._sort_bybox = QComboBox("SortByBox", self)
        self._sort_button = QPushButton("SortButton", self)

        widget = uic.loadUi("../ui/main.ui")
        widget.show()

        self._folder_choice.clicked.connect(self.button_clicked())

        sys.exit(app.exec())
