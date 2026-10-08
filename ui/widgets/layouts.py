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

        Current Forecast
        3 - weather_image svg object
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

    # Create a vertical layout manager
    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
    
    # Create app title label object
    widgets["app_title"].setAlignment(Qt.AlignmentFlag.AlignCenter)
    vbox.addWidget(widgets["app_title"])

    # Set the layout manager to organize widgets
    parent.setLayout(vbox)

    return vbox

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