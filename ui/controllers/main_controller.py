# Standard library imports
import sys, os
from pathlib import Path

# Local library imports
from ui.windows.main_window import Main_Window
from ui.dialogs.settings_dialog import Settings_Window
from services.weather_service import load_weather_data

def open_settings(self):
    """Inside the main window class open a settings dialog window"""
    dialog = Settings_Window(self)

    if dialog.exec() == QDialog.DialogCode.Accepted:
        username = dialog.username.text()
        print(username)

def on_submit_click(self):
    print("Submit Clicked!")

    api_key = self.api_key.text().strip()
    if not api_key:
        self.caption.setText("Please enter your API key.")
        return

    city_name = self.city_name.text().strip()
    if not city_name:
        self.caption.setText("Please enter a city.")
        return

    print(f"You submitted: {city_name}")

    request_key = city_name.casefold()
    if request_key == self.last_request:
        self.caption.setText("Data is already being displayed")
        return

    self.submit.setEnabled(False)
    self.caption.setText("Loading weather...")

    try:
        data = load_weather_data(city_name, api_key, "metric")
        self.last_weather_data = data
        self.last_request = request_key

        self.display_weather(data)

    except ValueError as error:
        self.caption.setText(str(error))

    finally:
        self.submit.setEnabled(True)

def on_mode_switch(self):
    pass

def on_dialog_click(self):
    pass

def on_unit_changed(self, button_id):
    self.units = "imperial" if button_id == 1 else "metric"
    if self.last_weather_data is None:
        self.caption.setText("Submit a city to load the weather.")
        return

    self.display_weather(self.last_weather_data)

def display_weather(self, data):
    main_data = data.get("main", {})
    weather_data = data.get("weather", [{}])[0]

    temperature = main_data.get("temp")
    description = weather_data.get("description", "Unknown").capitalize()
    condition = weather_data.get("main", "")

    if temperature is None:
        self.caption.setText("The weather response was incomplete.")
        return

    # If saved response was originally loaded in Celsius, convert it to Fahrenheit
    if self.units == "imperial":
        temperature = (temperature * 9 / 5) + 32
        unit_symbol = "°F"
    else:
        unit_symbol = "°C"

    self.temperature.setText(f"{temperature:.1f}{unit_symbol}")

    city_name = data.get("name", self.city_name.text().strip())
    self.caption.setText(f"{city_name}: {description}")

    icon_filename = {
        "Clear": "sun.svg",
        "Clouds": "cloud.svg",
        "Rain": "cloud-rain.svg",
        "Thunderstorm": "cloud-lightning.svg",
        "Snow": "cloud-snow.svg",
    }.get(condition, "cloud-drizzle.svg")

    update_picture(self.picture, icon_filename)

def update_picture(picture, filename, theme="light"):
    """Update the SVG file displayed by the weather image widget."""
    image_path = get_image_path(filename, theme)

    if not image_path.exists():
        print(f"Could not find image: {image_path}")
        return False

    loaded = picture.load(str(image_path))

    if not loaded:
        print(f"Could not load SVG: {image_path}")
        return False

    return True

def set_forecast_icons(self, filenames):
    """Update the five forecast icons from a list of SVG filenames."""
    for image, filename in zip(self.forecast_weather_images, filenames):
        image.load(str(get_icon_path(filename)))