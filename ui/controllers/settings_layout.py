# Third party imports
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt

# Local library imports


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

def create_nav_bar_layout(widgets):
    """Call the add_widgets function to create a horizontal layout manager for a navigation bar."""
    # Create a horizontal layout manager for the navigation bar
    nav_bar = QHBoxLayout()

    # Create light/dark mode button object
    nav_bar.addWidget(widgets["mode_button"])
    nav_bar.addStretch()
    
    # Create app title label object
    nav_bar.addWidget(widgets["main_title"], alignment=CENTER)
    nav_bar.addStretch()

    # Create settings button object
    nav_bar.addWidget(widgets["settings_button"])

    # # Create the background image object
    # widgets["weather_image"].setAlignment(Qt.AlignmentFlag.AlignCenter)
    # nav_bar.addWidget(widgets["weather_image"])

    # Add the navigation bar to the main layout manager
    return nav_bar

def create_forecast_layout(widgets):
    """Call the add_widgets function to create a vertical layout manager for the current weather forecast."""
    # Create a vertical layout manager for the current forecast information
    current_forecast = QVBoxLayout()
    current_forecast.setAlignment(CENTER)

    # Call the add_widgets function to create the label objects
    add_widgets(current_forecast,
                widgets,
                "city_title",   # Create the city name title label object
                "main_temp",    # Create the main currrent temperature label object
                "main_desc",    # Create the current weather description label object
                alignment=CENTER)

    return current_forecast

def create_fiveday_layout(widgets):
    """Call the add_widgets function to create a horizontal layout manager for the next five-day forecast."""
    pass

def create_detailed_layout(widgets):
    """Call the add_widgets function to create a grid layout manager for the current detailed weather forecast."""
    pass