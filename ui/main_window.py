# Standard library imports
import sys, os
from pathlib import Path

# Third-party limports
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt

# Local library imports
from ui.layouts import create_main_layout
from ui.labels import create_app_title

# Ex. from ui.window import Main_Window
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic window description
        self.setWindowTitle("OpenSky")
        self.setMinimumSize(400, 600)
        # Image sourced from https://feathericons.com/

        # Create a generic widget for the layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create title object
        self.title = create_app_title(central_widget)
        
        # Create dictionary of all widgets
        widgets = {
            "app_title": self.title
        }

        # Apply the layout manager to widget dictionary
        create_main_layout(central_widget, widgets)