# Standard library imports
import sys
from pathlib import Path

# Third-party limports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QFontDatabase

# Local library imports
from ui.main_window import Main_Window

def main():
    """main() method runs the main program."""
    app = QApplication(sys.argv)

    window = Main_Window()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Closing program...")