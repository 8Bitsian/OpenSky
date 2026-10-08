# Third party imports
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt

# Global variables
CENTER = Qt.AlignmentFlag.AlignCenter

def add_widgets(layout, widgets, *names, alignment=None):
    """Add named widgets to a layout, optionally with a shared alignment."""
    for name in names:
        widget = widgets[name]
        if alignment is None:
            layout.addWidget(widget)
        else:
            layout.addWidget(widget, alignment)

def create_navbar_layout(widgets):
    """Call the add_widgets function to create a horizontal layout manager for a navigation bar."""
    # Create a horizontal layout manager for the navigation bar
    nav_bar = QHBoxLayout()
    
    # Create settings dialog box title label object
    nav_bar.addWidget(widgets["dialog_title"], alignment=CENTER)

    # Add the navigation bar to the settings layout manager
    return nav_bar

def create_api_key_layout(widgets):
    """Call the add_widgets function to create a horizontal layout manager for the api key input."""
    # Create a horizontal layout manager for the navigation bar
    api_key = QHBoxLayout()
    
    # Create API key line edit (textbox) object
    api_key.addWidget(widgets["api_textbox"])

    # Create API key sumbit button object
    api_key.addWidget(widgets["api_submit"])

    # Add the API key input layout to the settings layout manager
    return api_key

def create_city_name_layout(widgets):
    """Call the add_widgets function to create a horizontal layout manager for the city name input."""
    # Create a horizontal layout manager for the navigation bar
    city_name = QHBoxLayout()
    
    # Create city name line edit (textbox) object
    city_name.addWidget(widgets["api_textbox"])

    # Create city name sumbit button object
    city_name.addWidget(widgets["api_submit"])

    # Add the city name input layout to the settings layout manager
    return city_name

def create_unit_button_layout(widgets):
    """Call the add_widgets function to create a horizontal layout manager for the temeprature unit."""
    # Create a horizontal layout manager for the navigation bar
    unit_buttons = QHBoxLayout()
    
    # Create settings dialog box title label object
    unit_buttons.addWidget(widgets["celsius__button"])

    # Create settings dialog box title label object
    unit_buttons.addWidget(widgets["fahrenheit_button"])

    # Add the navigation bar to the settings layout manager
    return unit_buttons