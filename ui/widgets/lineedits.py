# Third party imports
from PyQt6.QtWidgets import QLineEdit

def create_textbox(parent, object_name, text="", password=False):
    """Create a line edit (textbox) object w/specific parameters"""
    # Create lineedit object
    textbox = QLineEdit(parent)
    # Set object name for reference in style sheet
    textbox.setObjectName(object_name)
    # Set placeholder text for the textbox
    textbox.setPlaceholderText(text)

    if password:
        textbox.setEchoMode(QLineEdit.EchoMode.Password)

    return textbox

def create_city_input(parent):
    """Create the city input textbox"""
    return create_textbox(parent, "city_input", "Enter City Name")

def create_api_key_input(parent):
    """Create the app title label for the program."""
    return create_textbox(parent, "api_key_input", "Enter OpenWeather API Key", password=True)