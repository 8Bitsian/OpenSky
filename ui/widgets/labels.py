# Third party imports
from PyQt6.QtWidgets import QLabel

def create_label(parent, object_name, text=""):
    """Create the label widget object w/specified paramters"""
    # Create label object
    label = QLabel(text, parent)
    # Set object name for reference in style sheet
    label.setObjectName(object_name)
    # Return label object to method
    return label

def create_app_title(parent):
    """Create the app title label for the program."""
    return create_label(parent, "app_title", "OpenSky")

def create_dialog_title(parent):
    """Create the dialog title label for the program."""
    return create_label(parent, "dialog_title", "Settings")

def create_city_name(parent):
    """Create the city name label for current city selected."""
    return create_label(parent, "city_label", "No city selected.")

def create_main_temp(parent):
    """Create the temperature label for current temp."""
    return create_label(parent, "temp_label", "--")

def create_description(parent):
    """Create the description label for the current state of weather."""
    return create_label(parent, "desc_label", "No data found.")

def create_feel_temp(parent):
    """Create what the temperature feels like label for current day."""
    return create_label(parent, "feel_label", "Feels like: --")

def create_humidity(parent):
    """Create the low temperature label for current day."""
    return create_label(parent, "humid_label", "Humidity: --")

def create_forecast_temp(parent):
    """Create the high temperature label for current day."""
    return create_label(parent, "forecast_label", "--")

def create_forecast_month(parent):
    """Create a day of the month (1-31) label for the forecast."""
    return create_label(parent, "month_label", "d")

def create_forecast_week(parent):
    """Create a day of the week (mon-sun) label for the forecast."""
    return create_label(parent, "week_label", "ddd")

def create_sunrise(parent):
    """Create the sunrise time label for the forecast."""
    return create_label(parent, "sunrise_label", "--")

def create_sunset(parent):
    """Create the sunrise time label for the forecast."""
    return create_label(parent, "sunset_label", "--")