# Standard library imports
import sys

# Third-party limports
from PyQt6.QtWidgets import QApplication

# Local library imports
from ui.app_theme import load_fonts, load_stylesheet
from ui.windows.main_window import Main_Window

def main():
    """main() method runs the main program."""
    app = QApplication(sys.argv)

    load_fonts()
    load_stylesheet(app)

    window = Main_Window()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Closing program...")