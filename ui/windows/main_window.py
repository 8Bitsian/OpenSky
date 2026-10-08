# Standard library imports
import sys, os
from pathlib import Path

# Third-party limports
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QPushButton
from PyQt6.QtCore import Qt

# Local library imports
from ui.controllers.main_controller import (open_settings,
                                         on_submit_click,
                                         on_mode_switch,
                                         on_dialog_click,
                                         on_unit_changed,
                                         display_weather,
                                         update_picture,
                                         set_forecast_icons)

from ui.dialogs.settings_dialog import Settings_Window

from ui.widgets.images import (load_icon,
                               create_current_weather_image,
                               create_forecast_weather_image)

from ui.widgets.buttons import (create_city_submit,
                                create_mode_switch,
                                create_settings_button)

from ui.widgets.labels import (create_app_title,
                               create_city_name,
                               create_main_temp,
                               create_description,
                               create_feel_temp,
                               create_humidity,
                               create_forecast_temp,
                               create_forecast_month,
                               create_forecast_week,
                               create_sunrise,
                               create_sunset)

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
        self.mode_button = create_mode_switch(central_widget, on_mode_switch)
        # Create settings button object
        self.settings_button = create_settings_button(central_widget, on_dialog_click)
        # Create main weather-state svg object
        self.current_weather_image = create_current_weather_image(central_widget, "drizzle.svg")
        # Create main city name label object
        self.city_name_label = create_city_name(central_widget)
        # Create main current temperature label object
        self.main_temp_label = create_main_temp(central_widget)
        # Create main weather description label object
        self.main_desc_label = create_description(central_widget)

        # 1 horizonal layout containing these widgets for each of the next five days
        # Create forecast month date label object
        self.forecast_month_label = create_forecast_month(central_widget)
        # Create forecast week date label object
        self.forecast_week_label = create_forecast_week(central_widget)
        # Create forecast weather-state svg object
        self.forecast_weather_images = [
            create_forecast_weather_image(
                central_widget,
                "drizzle.svg",
                index
            )
            for index in range(5)
        ]

        # Create forecast temperature label object
        self.forecast_temp_label = create_forecast_temp(central_widget)
        
        # Create feels-like temperature label object
        self.feels_like_temp_label = create_feel_temp(central_widget)
        # Create humidity label object
        self.humid_level_label = create_humidity(central_widget)

        # Create sunrise time label object
        self.sunrise_label = create_sunrise(central_widget)
        # Create sunset time label object
        self.sunset_label = create_sunset(central_widget)

        # Create dictionary of all widgets
        main_widgets = {
            "main_title": self.main_title,
            "mode_button": self.mode_button,
            "settings_button": self.settings_button,
            "weather_image": self.current_weather_image,
            "city_title": self.city_name_label,
            "main_temp": self.main_temp_label,
            "main_desc": self.main_desc_label,
            "forecast_month": self.forecast_month_label,
            "forecast_week": self.forecast_week_label,
            "forecast_images": self.forecast_weather_images,
            "forecast_temp": self.forecast_temp_label,
            "feel_like_temp": self.feels_like_temp_label,
            "humid_level": self.humid_level_label,
            "sunrise_time": self.sunrise_label,
            "sunset_time": self.sunset_label,
        }

        for index, image in enumerate(self.forecast_weather_images):
            main_widgets[f"forecast_weather_image_{index}"] = image

        # Apply the layout manager to widget dictionary
        create_main_layout(central_widget, main_widgets)