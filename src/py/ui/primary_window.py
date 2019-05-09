"""Main UI screen"""

import sys
import os

from mutagen.mp3 import EasyMP3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

class PrimaryWindow(QMainWindow):
    """Class containing the main ui window"""

    def __init__(self, app, ui_file):
        super().__init__()

        self._paths = []
        self._directory = ""

        self._ui = None
        self._folder_choice = None
        self._folder_textbox = None
        self._sort_bybox = None
        self._sort_button = None
        self.load_window(app, ui_file)

    def load_window(self, app, ui_file):
        """Loads the main window ui"""

        #Load the ui from the .ui file
        widget = uic.loadUi(ui_file)
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

        #Disable the sort button until a folder has been chosen
        self._sort_button.setEnabled(False)

        sys.exit(app.exec())

    def folder_choice_click(self):
        """Event handler for folder_choice presses"""

        #Open a file dialog
        directory = QFileDialog.getExistingDirectory(self, "Select Folder", "/home")
        
        if directory:
            #Get the files that end with the .mp3 extension
            files = [_f for _f in os.listdir(directory) if _f.endswith(".mp3")]

            self._directory = directory

            #Combine the directory and file names to generate a path for each file
            for _f in files:
                self._paths.append(f"{directory}/{_f}")

            #Set the textbox ui item to the directory selected
            self._folder_textbox.setText(directory)
            self._folder_textbox.setReadOnly(True)

            if self._paths:
                self._sort_button.setEnabled(True)

    def sort_button_click(self):
        """Event handler for sort_button presses"""

        folder_names = []
        file_names = {}

        #Get the index of the combo box selection
        type_of_sort = self._sort_bybox.currentIndex()

        for path in self._paths:
            track = EasyMP3(path)

            #Extract the appropriate type of ID3 data based on type_of_sort
            if type_of_sort == 0:
                artist = track["artist"][0]
                folder_names.append(artist)
                file_names[path.rsplit('/', 1)[1]] = artist
            elif type_of_sort == 1:
                album = track["album"][0]
                folder_names.append(album)
                file_names[path.rsplit('/', 1)[1]] = album

        #Remove duplicates from list
        folder_names = list(dict.fromkeys(folder_names))

        self.sort_files(folder_names, file_names)

        #Display a dialog showing success
        success = QMessageBox()
        success.setWindowTitle("Music Organizer - Success")
        success.setText("Success!")
        success.setStandardButtons(QMessageBox.Ok)
        success.exec()

    def sort_files(self, folder_names, file_names):
        """Sorts files into the appropriate folder"""

        #Make a folder for each artist/album
        for name in folder_names:
            if not os.path.isdir(f"{self._directory}/{name}"):
                os.mkdir(f"{self._directory}/{name}/")

        #Move each file into the appropriate folder
        for file_name in file_names:
            folder_name = file_names[file_name]
            src_dir = f"{self._directory}/{file_name}"
            dest_dir = f"{self._directory}/{folder_name}/{file_name}"

            os.rename(src_dir, dest_dir)
