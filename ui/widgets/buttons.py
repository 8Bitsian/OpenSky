# Third party imports
from PyQt6.QtWidgets import QPushButton, QRadioButton, QButtonGroup

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

def create_city_submit(parent, on_submit_click):
    """Create the city input submit button to enter the city name."""
    return create_button(parent, "submit_button", on_submit_click, "Submit")

def create_temp_unit_preference(parent, on_unit_change):
    """
    Create the temperature-unit radio button.

    The button IDs:
        0: Metric (Celsius)
        1: Imperial (Fahrenheit)
    """
    # Create button objects
    celsius = create_radio_button(parent, "c_temp_button", "Celsius")
    fahrenheit = create_radio_button(parent, "f_temp_button", "Fahrenheit")

    # Create button group
    group = QButtonGroup(parent)
    group.addButton(celsius, 0)
    group.addButton(fahrenheit, 1)

    # Connect the button group to a module when clicked
    group.idClicked.connect(on_unit_change)

    # Default to Celsius
    celsius.setChecked(True)

    return (group, fahrenheit, celsius)