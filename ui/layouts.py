# Third party imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

def create_main_layout(parent, widgets):
    """
    Create a layout manager for the Widgets dictionary.

    Widgets order:
        0 - app title label
    """

    # Create a vertical layout manager
    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignTop)
    
    # Create app title label object
    widgets["app_title"].setAlignment(Qt.AlignCenter)
    vbox.addWidget(widgets["app_title"])

    # Set the layout manager to organize widgets
    parent.setLayout(vbox)

    return vbox