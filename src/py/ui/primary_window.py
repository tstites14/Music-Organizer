"""Main UI screen"""

import sys
import os

from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
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

        #Loads the ui from the .ui file
        path = os.path.dirname(sys.modules['__main__'].__file__)
        widget = uic.loadUi(os.path.join(path, '../ui/main.ui'))
        widget.show()

        #Assigns widget objects to the ui's objects
        self._ui = widget
        self._folder_choice = self._ui.folder_choice
        self._folder_textbox = self._ui.folder_textbox
        self._sort_bybox = self._ui.sort_by_box
        self._sort_button = self._ui.sort_button

        #Connects buttons to trigger methods
        self._folder_choice.clicked.connect(self.folder_choice_click)
        self._sort_button.clicked.connect(self.sort_button_click)

        sys.exit(app.exec())

    def folder_choice_click(self):
        """Event handler for folder_choice presses"""

        #Open a file dialog and get the files that end with the .py extension
        directory = QFileDialog.getExistingDirectory(self, "Select Folder", "/home")
        files = [_f for _f in os.listdir(directory) if _f.endswith(".py")]

        #Combine the directory and file names to generate a path for each file
        for _f in files:
            path = f"{directory}/{_f}"
            print(path)

    def sort_button_click(self):
        """Event handler for sort_button presses"""

        print("TEST2")
