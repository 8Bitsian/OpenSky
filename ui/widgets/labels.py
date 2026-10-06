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

def create_city_name(parent):
    """Create the city name label for current city selected."""
    return create_label(parent, "city_label", "No city selected.")

def create_temperature(parent):
    """Create the temperature label for current temp."""
    return create_label(parent, "temp_label", "--")

def create_description(parent):
    """Create the description label for the current state of weather."""
    return create_label(parent, "desc_label", "No data found.")

def create_feel_temp(parent):
    """Create what the temperature feels like label for current day."""
    return create_label(parent, "feel_label", "--")

def create_high_temp(parent):
    """Create the high temperature label for current day."""
    return create_label(parent, "high_label", "--")

def create_low_temp(parent):
    """Create the low temperature label for current day."""
    return create_label(parent, "low_label", "--")
