"""Main UI screen"""

import sys

from PyQt5.QtCore import Qt
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
        self.load_window()

    def load_window(self):
        """Loads the main window ui"""

        app = QApplication(sys.argv)
        self._folder_choice = QToolButton()
        self._folder_textbox = QTextEdit()
        self._sort_bybox = QComboBox()
        self._sort_button = QPushButton()

        widget = uic.loadUi("../ui/main.ui")
        widget.show()

        sys.exit(app.exec())

    def exit(self, key):
        """Exits application"""

        if key.key() == Qt.Key_Escape:
            self.close()

    def button_clicked(self):
        """Event handler for button presses"""

        #sender = self.sender()
