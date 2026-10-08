# Third party imports
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt

# Local library imports
from ui.layouts.main_layout import (create_nav_bar_layout,
                                        create_forecast_layout,
                                        create_fiveday_layout,
                                        create_detailed_layout)

from ui.layouts.dialog_layout import (create_navbar_layout,
                                       create_api_key_layout,
                                       create_city_name_layout,
                                       create_unit_button_layout)

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

        Five-Day Forecast (will make 5 layouts side-by-side)
        7 - forecast_month label object
        8 - forecast_week label object
        9 - forecast_image svg object
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

    # Add the navigation bar to the main layout manager
    main_layout.addLayout(create_nav_bar_layout(widgets))

    # Add the current forecast to the main layout manager
    main_layout.addLayout(create_forecast_layout(widgets))

    # Add the next five-day forecast to the main layout manager
    main_layout.addLayout(create_fiveday_layout(widgets))

    # Add the current detailed forecast to the main layout manager
    main_layout.addLayout(create_detailed_layout(widgets))

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
    # Create a vertical layout manager for the main layout of the app
    setting_layout = QVBoxLayout()
    setting_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    # Add the settings title to the settings layout manager
    setting_layout.addLayout(create_navbar_layout(widgets))

    # Add the current forecast to the settings layout manager
    setting_layout.addLayout(create_api_key_layout(widgets))

    # Add the next five-day forecast to the settings layout manager
    setting_layout.addLayout(create_city_name_layout(widgets))

    # Add the current detailed forecast to the settings layout manager
    setting_layout.addLayout(create_unit_button_layout(widgets))

    # Set the layout manager to organize widgets
    parent.setLayout(setting_layout)

    return setting_layout