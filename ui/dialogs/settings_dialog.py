# Third-party limports
from PyQt6.QtWidgets import QDialog

# Local library imports
from controllers.main_controller import open_settings
from ui.widgets.layouts import create_settings_layout
from ui.widget.buttons import create_temp_unit_buttons

# Ex. from ui.window import Main_Window
class Settings_Window(QDialog):
    def __init__(self):
        super().__init__()