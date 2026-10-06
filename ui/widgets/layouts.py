# Third party imports
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt

def create_main_layout(parent, widgets):
    """
    Create a vertical layout manager for the main window.

    Widgets dictionary order:
        0 - app_title label object
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
        0 - api_key lineedit (textbox) object
    """
    pass