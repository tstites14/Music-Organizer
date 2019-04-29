"""Main file that starts the app"""

import sys

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    APP = QApplication(sys.argv)

    from ui.primary_window import PrimaryWindow
    MAIN = PrimaryWindow()
    MAIN.load_window()
    sys.exit(APP.exec_())
