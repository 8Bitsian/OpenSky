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