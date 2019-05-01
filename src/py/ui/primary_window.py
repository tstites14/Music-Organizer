"""Main UI screen"""

import sys
import os

from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QToolButton, QTextEdit, QPushButton, QComboBox)

class PrimaryWindow(QMainWindow):
    """Class containing the main ui window"""

    def __init__(self, app):
        super().__init__()

        self._ui = None
        self._folder_choice = None
        self._folder_textbox = None
        self._sort_bybox = None
        self._sort_button = None
        self.load_window(app)

    def load_window(self, app):
        """Loads the main window ui"""

        path = os.path.dirname(sys.modules['__main__'].__file__)
        widget = uic.loadUi(os.path.join(path, '../ui/main.ui'))
        widget.show()

        self._ui = widget
        self._folder_choice = self._ui.folder_choice
        self._folder_textbox = self._ui.folder_textbox
        self._sort_bybox = self._ui.sort_by_box
        self._sort_button = self._ui.sort_button

        self._folder_choice.clicked.connect(self.folder_choice_click)
        self._sort_button.clicked.connect(self.sort_button_click)

        sys.exit(app.exec())

    def folder_choice_click(self):
        """Event handler for folder_choice presses"""

        print("TEST")

    def sort_button_click(self):
        """Event handler for sort_button presses"""

        print("TEST2")
