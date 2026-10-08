# Third party imports
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt

def create_main_layout(parent, widgets):
    """
    Create a vertical layout manager for the main window.

    Widgets dictionary order:
        Navigation Bar Group
        0 - main_title label object
        1 - mode_button button object
        2 - settings_button button object
        3 - weather_image svg object (bg for nav bar)

        Current Forecast
        4 - city_title label object
        5 - main_temp label object
        6 - main_desc label object

        Five-Day Forecast
        7 - forecast_month label object
        8 - forecast_week label object
        9 - forecast_images svg objects
        10 - forecast_temp label object

        Detailed Forecast
        11 - feel_like_temp label object
        12 - humid_level label object
        13 - sunrise_time label object
        14 - sunset_time label object
    """

    # Create a vertical layout manager for the main layout of the app
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    # Create a horizontal layout manager for the navigation bar
    nav_bar = QHBoxLayout()
    nav_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    # Create light/dark mode button object
    widgets["mode_button"].setAlignment(Qt.Alignment.AlignLeft)
    nav_bar.addWidget(widgets["mode_button"])

    # Create app title label object
    widgets["main_title"].setAlignment(Qt.AlignmentFlag.AlignCenter)
    nav_bar.addWidget(widgets["main_title"])

    # Create settings button object
    widgets["settings_button"].setAlignment(Qt.AlignmentFlag.AlignRight)
    nav_bar.addWidget(widgets["settings_button"])

    # Create the background image object
    widgets["weather_image"].setAlignment(Qt.AlignmentFlag.AlignCenter)
    nav_bar.addWidget(widgets["weather_image"])

    # Add the navigation bar to the main layout manager
    main_layout.addLayout(nav_bar)

    # Create a vertical layout manager for the current forecast information
    current_forecast = QVBoxLayout()
    current_forecast.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Create the city name title label object
    widgets["city_title"].setAlignment(QtAlignmentFlag.AlignCenter)
    current_forecast.addWidget(widgets["city_title"])

    # Create the main currrent temperature label object
    widgets["main_temp"].setAlignment(QtAlignmentFlag.AlignCenter)
    current_forecast.addWidget(widgets["main_temp"])

    # Create the current weather description label object
    widgets["main_desc"].setAlignment(QtAlignmentFlag.AlignCenter)
    current_forecast.addWidget(widgets["main_desc"])

    # Add the current forecast to the main layout manager
    main_layout.addLayout(current_forecast)

    # Set the layout manager to organize widgets
    parent.setLayout(main_layout)

    return main_layout

def create_settings_layout(parent, widgets):
    """
    Create a form layout manager for the settings window.

    Widgets dictionary order:
        0 - dialog_title label object
        1 - api_textbox lineedit (textbox) object
        2 - api_submit button object
        3 - city_textbox lineedit object
        4 - city_submit button object
        5 - temp_units button object
    """
    pass