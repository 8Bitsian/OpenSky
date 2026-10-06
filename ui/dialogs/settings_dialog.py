# Third-party limports
from PyQt6.QtWidgets import QDialog

# Local library imports
from controllers.main_controller import open_settings
from ui.widgets.layouts import create_settings_layout
from ui.widget.buttons import create_temp_unit_buttons

# Ex. from ui.window import Main_Window
class Settings_Window(QDialog):
    def __init__(self):
        super().__init__()
        # Basic window description
        self.setWindowTitle("Settings")
        self.setMinimumSize(200, 300)
        # Image sourced from https://feathericons.com/
        self.setWindowIcon(load_icon("settings.svg"))

        # Create a generic widget for the layout manager
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create title label object
        self.setting_title = create_app_title(central_widget)

        # Create OpenWeatherMapAPI key line edit (textbox) object

        # Create temperature conversiopn radio buttons

        # Create theme radio buttons

        # Create dictionary of all widgets
        settings_widgets = {
            "app_title": self.title
        }

        # Apply the layout manager to widget dictionary
        create_main_layout(central_widget, settings_widgets)