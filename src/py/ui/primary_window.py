"""Main UI screen"""

import sys
import os

from mutagen.mp3 import EasyMP3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog

class PrimaryWindow(QMainWindow):
    """Class containing the main ui window"""

    def __init__(self, app):
        super().__init__()

        self._paths = []
        self._directory = ""

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

        #Open a file dialog and get the files that end with the .mp3 extension
        directory = QFileDialog.getExistingDirectory(self, "Select Folder", "/home")
        files = [_f for _f in os.listdir(directory) if _f.endswith(".mp3")]

        self._directory = directory

        #Combine the directory and file names to generate a path for each file
        for _f in files:
            self._paths.append(f"{directory}/{_f}")

        #Set the textbox ui item to the directory selected
        self._folder_textbox.setText(directory)
        self._folder_textbox.setReadOnly(True)

    def sort_button_click(self):
        """Event handler for sort_button presses"""

        folder_names = []

        #Get the index of the combo box selection
        type_of_sort = self._sort_bybox.currentIndex()

        for path in self._paths:
            track = EasyMP3(path)

            #Extract the appropriate type of ID3 data based on type_of_sort
            if type_of_sort == 0:
                artist = track["artist"][0]
                folder_names.append(artist)
            elif type_of_sort == 1:
                album = track["album"][0]
                folder_names.append(album)

        #Remove duplicates from list
        folder_names = list(dict.fromkeys(folder_names))
        self.sort_files(folder_names)

    def sort_files(self, names):
        """Sorts files into the appropriate folder"""

        for name in names:
            print(f"{self._directory}/{name}")
            os.mkdir(f"{self._directory}/{name}/")
