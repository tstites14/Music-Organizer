"""Main file that starts the app"""

import sys
import os

from PyQt5.QtWidgets import QApplication

def is_prod():
    """Check if the app is running in frozen mode"""

    is_frozen = getattr(sys, 'frozen', False)
    frozen_temp_path = getattr(sys, '_MEIPASS', '')

    if is_frozen:
        basedir = frozen_temp_path
    else:
        basedir = os.path.dirname(os.path.abspath(__file__))
    return get_resources(resource_dir=basedir)

def get_resources(resource_dir):
    """Get the correct path for the ui file based on OS"""

    ui_file = open(os.path.join(resource_dir, 'main.ui'))

    return ui_file

if __name__ == "__main__":
    APP = QApplication(sys.argv)

    from ui.primary_window import PrimaryWindow
    MAIN = PrimaryWindow(APP, is_prod())
