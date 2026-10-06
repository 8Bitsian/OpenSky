# Standard library imports
import sys
from pathlib import Path

# Third-party limports
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QFile, QTextStream
from PyQt6.QtGui import QFontDatabase

# Local library imports
from ui.widgets.main_window import Main_Window

def main():
    """main() method runs the main program."""
    app = QApplication(sys.argv)

    window = Main_Window()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Closing program...")