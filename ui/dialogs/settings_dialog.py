# Third-party limports
from PyQt6.QtWidgets import QDialog

# Local library imports
from ui.controllers.main_controller import (on_submit_click,
                                            on_unit_changed)

from ui.widgets.lineedits import (create_api_key_input,
                                  create_city_input)

from ui.widgets.layouts import create_settings_layout

from ui.widgets.buttons import (create_api_submit,
                                create_city_submit,
                                create_temp_unit_preference)

# Ex. from ui.window import Main_Window
class Settings_Window(QDialog):
    def __init__(self):
        super().__init__()
        
        # Basic window description
        self.setWindowTitle("Settings")
        self.setMinimumSize(200, 300)
        # Image sourced from https://feathericons.com/
        self.setWindowIcon(load_icon("settings.svg"))

        # Create a generic widget for the layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create title label object
        self.setting_title = create_app_title(central_widget)

        # Create OpenWeatherMapAPI key line edit (textbox) object
        self.api_key_textbox = create_api_key_input(central_widget)
        self.api_key_submit = create_api_submit(central_widget, on_submit_click)

        # Create city input line textbox object
        self.city_name_textbox = create_city_input(central_widget)
        self.city_name_submit = create_city_submit(central_widget, on_submit_click)

        # Create temperature conversation radio buttons
        self.temp_unit_choice = create_temp_unit_preference(central_widget, on_unit_change)

        # Create dictionary of all widgets
        settings_widgets = {
            "dialog_title": self.setting_title,
            "api_textbox": self.api_key_textbox,
            "api_button": self.api_key_submit,
            "city_textbox": self.city_name_textbox,
            "city_button": self.city_name_submit,
            "temp_button": self.temp_unit_choice
        }

        # Apply the layout manager to widget dictionary
        create_main_layout(central_widget, settings_widgets)