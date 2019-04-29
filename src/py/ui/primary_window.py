"""Main UI screen"""

import sys, os

from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QToolButton, QTextEdit, QPushButton, QComboBox)

class PrimaryWindow(QMainWindow):
    """Class containing the main ui window"""

    def __init__(self, app):
        super().__init__()

        self._folder_choice = None
        self._folder_textbox = None
        self._sort_bybox = None
        self._sort_button = None
        self.load_window(app)

    def load_window(self, app):
        """Loads the main window ui"""

        self._folder_choice = QToolButton()
        self._folder_textbox = QTextEdit()
        self._sort_bybox = QComboBox()
        self._sort_button = QPushButton()

        path = os.path.dirname(sys.modules['__main__'].__file__)
        widget = uic.loadUi(os.path.join(path, '../ui/main.ui'))
        widget.show()

        sys.exit(app.exec())

    def button_clicked(self):
        """Event handler for button presses"""

        #sender = self.sender()
