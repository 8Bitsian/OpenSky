# Standard library imports
import sys, os
from pathlib import Path

# Third-party limports
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QPushButton
from PyQt6.QtCore import Qt

# Local library imports
from ui.dialogs.settings_dialog import Settings_Window
from ui.widgets.images import load_icon
from ui.widgets.labels import create_app_title
from ui.widgets.layouts import create_main_layout

# Ex. from ui.window import Main_Window
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic window description
        self.setWindowTitle("OpenSky")
        self.setMinimumSize(400, 600)
        # Image sourced from https://feathericons.com/
        self.setWindowIcon(load_icon("drizzle.svg"))

        # Create a generic widget for the layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create title label object
        self.main_title = create_app_title(central_widget)
        # Create mode button object
        # Create settings button object
        # Create main weather-state svg object

        # Create main city name label object
        # Create main current temperature label object
        # Create main weather description label object

        # 1 horizonal layout containing these widgets for each of the next five days
        # Create forecast month date label object
        # Create forecast week date label object
        # Create forecast weather-state svg object
        # Create forecast high temperature label object
        # Create forecast low temperature label object
        
        # Create feels-like temperature label object
        # Create Humidity label object

        # Create Air quality label object
        # Create pollen label object

        # Create dictionary of all widgets
        main_widgets = {
            "main_title": self.title
        }

        # Apply the layout manager to widget dictionary
        create_main_layout(central_widget, main_widgets)
