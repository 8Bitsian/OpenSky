# Standard library imports
import sys, os
from pathlib import Path

# Third-party limports
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QPushButton
from PyQt6.QtCore import Qt

# Local library imports
from ui.windows.settings_dialog import Settings_Window
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

        # Create title object
        self.title = create_app_title(central_widget)
        
        # Create dictionary of all widgets
        widgets = {
            "app_title": self.title
        }

        # Apply the layout manager to widget dictionary
        create_main_layout(central_widget, widgets)

    

    def open_settings(self):
        """Inside the main window class open a settings dialog window"""
        dialog = Settings_Window(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            username = dialog.username.text()
            print(username)