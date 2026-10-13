# Standard library imports
import sys, os
from pathlib import Path

# Third-party imports
from PyQt6.QtCore import QThread, QSettings

# Local library imports
from ui.dialogs.settings_dialog import Settings_Window
from data.weather_data import get_current_conditions
from services.weather_worker import WeatherWorker

def on_mode_switch(self):
    """Toggle the app theme between light mode and dark mode."""
    pass

def open_settings(self):
    """Open the settings dialog window and apply changes if the user accets the dialog."""
    dialog = Settings_Window(
        parent=self,    # Self should be the main_window instance
        api_key=getattr(self, "api_key", ""),
        city_name=getattr(self, "city_name", ""),
        units=getattr(self, "units", "metric"),
    )

    # Each successful submit emits this signal
    dialog.settingsChanged.connect(
        lambda: reload_weather(self)
    )

    # Waits until user closes settings dialog
    dialog.exec() 

def reload_weather(self):
    """Read saved settings and request updated weather."""
    settings = QSettings("OpenSky", "openSky")

    api_key = settings.value("api_key", "", type=str).strip()
    city_name = settings.value("city_name", "", type=str).strip()
    units = settings.value("units", "metric", type=str)

    if not api_key or not city_name:
        self.main_desc_label.setText(
            "Enter an API key and city in Settings."
        )
        return

    self.api_key = api_key
    self.city_name = city_name
    self.units = units

    load_weather(self, api_key, city_name, units)

def load_weather(self, api_key, city_name, units):
    """Fetch weather in a worker thread."""
    self.main_desc_label.setText("Loading weather data...")

    self.weather_thread = QThread(self)
    self.weather_worker = WeatherWorker(api_key, city_name, units)
    self.weather_worker.moveToThread(self.weather_thread)

    self.weather_thread.started.connect(self.weather_worker.run)

    # Controller functions, so pass the window explicitly
    self.weather_worker.succeeded.connect(
        lambda data: show_weather(self, data)
    )

    self.weather_worker.failed.connect(
        lambda message: show_weather_error(self, message)
    )

    self.weather_worker.finished.connect(self.weather_thread.quit)
    self.weather_worker.finished.connect(self.weather_worker.deleteLater)
    self.weather_thread.finished.connect(self.weather_thread.deleteLater)

    self.weather_thread.start()

def show_weather(self, data):
    """Update the main-window labels from the API response."""
    try:
        conditions = get_current_conditions(data)
    except ValueError as error:
        show_weather_error(self, str(error))
        return
    
    unit_symbol = "°F" if self.units == "imperial" else "°C"
    self.main_temp_label.setText(f"{conditions['temperature']:.1f}{unit_symbol}")
    self.main_desc_label.setText(conditions["description"])
    self.city_name_label.setText(conditions["city"])

    # self.weather_icon_label.setText(conditions["condition"])

def show_weather_error(self, message):
    """Show a request or response error in the main window."""
    self.main_desc_label.setText(message)

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