# Third party imports
from PyQt6.QtWidgets import QButtonGroup, QPushButton, QRadioButton

def create_button(parent, object_name, on_click=None, text=""):
    """Create a button object w/specific parameters"""
    # Create button object
    button = QPushButton(text, parent)
    # Set object name for reference in style sheet
    button.setObjectName(object_name)

    # Connect the button object to a module when clicked
    if on_click is not None:
        button.clicked.connect(on_click)

    return button

def create_radio_button(parent, object_name, text=""):
    """Create a radio button object w/specific parameters"""
    # Create button object
    radio = QRadioButton(text, parent)
    # Set object name for reference in style sheet
    radio.setObjectName(object_name)

    return radio

def create_api_submit(parent, on_submit_click=None):
    """Create the city input submit button to enter the city name."""
    return create_button(parent, "api_submit_button", on_submit_click, "Submit")

def create_city_submit(parent, on_submit_click=None):
    """Create the city input submit button to enter the city name."""
    return create_button(parent, "city_submit_button", on_submit_click, "Submit")

def create_mode_switch(parent, on_mode_switch=None):
    """Create the city input submit button to enter the city name."""
    return create_button(parent, "mode_button", on_mode_switch)

def create_settings_button(parent, open_settings=None):
    """Create the city input submit button to enter the city name."""
    return create_button(parent, "settings_button", open_settings)

def create_temp_unit_preference(parent, on_unit_change=None):
    """ Create the temperature-unit button groups and its radio buttons."""
    # Create button objects
    celsius = create_radio_button(parent, "celsius_button", "Celsius")
    fahrenheit = create_radio_button(parent, "fahrenheit_button", "Fahrenheit")

    # Create button group
    group = QButtonGroup(parent)
    group.addButton(celsius, 0)     # 0 = Metric
    group.addButton(fahrenheit, 1)  # 1 = Imperial

    # Connect the button group to a module when clicked
    if on_unit_change is not None:
        group.idClicked.connect(on_unit_change)

    # Default to Celsius
    celsius.setChecked(True)

    return (group, fahrenheit, celsius)