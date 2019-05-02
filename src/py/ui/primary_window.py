"""Main UI screen"""

import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog

class PrimaryWindow(QMainWindow):
    """Class containing the main ui window"""

    def __init__(self, app):
        super().__init__()

        self._paths = []

        self._ui = None
        self._folder_choice = None
        self._folder_textbox = None
        self._sort_bybox = None
        self._sort_button = None
        self.load_window(app)

    def load_window(self, app):
        """Loads the main window ui"""

        #Load the ui from the .ui file
        path = os.path.dirname(sys.modules['__main__'].__file__)
        widget = uic.loadUi(os.path.join(path, '../ui/main.ui'))
        widget.show()

        #Assign widget objects to the ui's objects
        self._ui = widget
        self._folder_choice = self._ui.folder_choice
        self._folder_textbox = self._ui.folder_textbox
        self._sort_bybox = self._ui.sort_by_box
        self._sort_button = self._ui.sort_button

        #Connect buttons to trigger methods
        self._folder_choice.clicked.connect(self.folder_choice_click)
        self._sort_button.clicked.connect(self.sort_button_click)

        sys.exit(app.exec())

    def folder_choice_click(self):
        """Event handler for folder_choice presses"""

        #Open a file dialog and get the files that end with the .mp3 or .flac extension
        directory = QFileDialog.getExistingDirectory(self, "Select Folder", "/home")
        files = [_f for _f in os.listdir(directory) if _f.endswith(".mp3") or _f.endswith(".flac")]

        #Combine the directory and file names to generate a path for each file
        for _f in files:
            self._paths.append(f"{directory}/{_f}")

        #Set the textbox ui item to the directory selected
        self._folder_textbox.setText(directory)
        self._folder_textbox.setReadOnly(True)

    def sort_button_click(self):
        """Event handler for sort_button presses"""

        for path in self._paths:
            print(path)
