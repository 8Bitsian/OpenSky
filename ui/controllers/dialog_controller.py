# Third party imports
from PyQt6.QtWidgets import QMessageBox

def on_submit_click(self):
    """Validate the settings and accept the dialog if both feilds are filled."""
    print("Submit Clicked!")

    api_key = self.api_key_textbox.text().strip()

    if not api_key:
        QMessageBox.warning(self, "Missing API Key", "Please enter your API key.")
        self.api_key_textbox.setFocus()
        return

    city_name = self.city_name_textbox.text().strip()

    if not city_name:
        QMessageBox.warning(self, "Missing City", "Please enter a city.")
        self.city_name_textbox.setFocus()
        return

    self.api_key = api_key
    self.city_anme = city_name
    self.accept()

def on_unit_change(self, button_id):
    """Update the selected temperature unit."""
    self.selected_units = "imperial" if button_id == 1 else "metric"