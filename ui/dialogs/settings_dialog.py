# Third-party limports
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QWidget

# Local library imports
from ui.controllers.dialog_controller import (on_submit_click,
                                              on_unit_change)

from ui.layouts.layouts import create_settings_layout

from ui.widgets.buttons import (create_api_submit,
                                create_city_submit,
                                create_temp_unit_preference)

from ui.widgets.images import load_icon

from ui.widgets.labels import create_app_title

from ui.widgets.lineedits import (create_api_key_input,
                                  create_city_input)

# Ex. from ui.window import Main_Window
class Settings_Window(QDialog):
    def __init__(self, parent=None, api_key="", city_name="", units="metric"):
        super().__init__(parent)
        
        # Basic window description
        self.setWindowTitle("Settings")
        self.setMinimumSize(300, 200)
        # Image sourced from https://feathericons.com/
        self.setWindowIcon(load_icon("settings.svg"))

        self.api_key = api_key
        self.city_name = city_name
        self.selected_units = units

        # Create a generic widget for the layout manager
        central_widget = QWidget(self)
        dialog_layout = QVBoxLayout(self)
        dialog_layout.addWidget(central_widget)

        # Create title label object
        self.setting_title = create_app_title(central_widget)

        # Create OpenWeatherMap API key line edit (textbox) object
        self.api_key_textbox = create_api_key_input(central_widget)
        self.api_key_textbox.setText(api_key)

        # Create API key submission button object
        self.api_key_submit = create_api_submit(central_widget)
        self.api_key_submit.clicked.connect(
            lambda checked=False: on_submit_click(self)
        )

        # Create city input line textbox object
        self.city_name_textbox = create_city_input(central_widget)
        self.city_name_textbox.setText(city_name)

        # Create city name submission button object
        self.city_name_submit = create_city_submit(central_widget)
        self.city_name_submit.clicked.connect(
            lambda checked=False: on_submit_click(self)
        )

        # Create temperature conversation radio buttons
        (self.unit_button_group,
         self.fahrenheit_button,
         self.celsius_button) = create_temp_unit_preference(central_widget)

        self.unit_button_group.idClicked.connect(
            lambda button_id: on_unit_change(self, button_id)
        )

        if units == "imperial":
            self.fahrenheit_button.setChecked(True)
        else:
            self.celsius_button.setChecked(True)

        # Create dictionary of all widgets
        settings_widgets = {
            "dialog_title": self.setting_title,
            "api_textbox": self.api_key_textbox,
            "api_submit": self.api_key_submit,
            "city_textbox": self.city_name_textbox,
            "city_submit": self.city_name_submit,
            "celsius_button": self.celsius_button,
            "fahrenheit_button": self.fahrenheit_button
        }

        # Apply the layout manager to widget dictionary
        create_settings_layout(central_widget, settings_widgets)