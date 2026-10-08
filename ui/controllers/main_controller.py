# Standard library imports
import sys, os
from pathlib import Path

# Local library imports
from ui.dialogs.settings_dialog import Settings_Window
from data.weather_data import get_current_conditions
from services.weather_service import load_weather_data
from services.weather_worker import weather_worker

def on_mode_switch(self, checked=False):
    """Toggle the app theme between light mode and dark mode."""
    pass

def on_dialog_click(self, checked=False):
    pass

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

def open_settings(self, checked=False):
    """Open the settings dialog window and apply changes if the user accets the dialog."""
    dialog = Settings_Window(
        parent=main_window,
        api_key=main_window.api_key,
        city_name=main_window.city_name,
        units=main_window.units
    )

    if dialog.exec() == Settings_Window.DialogCode.Accepted:
        self.api_key = dialog.api_key
        self.city_name = dialog.city_name
        self.units = dialog.selected_units

    # Call weather-loading method since settings refreshes the main window

def load_weather(self, city_name, api_key, units):
    self.weather_thread = QThread(self)
    self.weather_worker = WeatherWorker(city_name, api_key, units)
    self.weather_worker.moveToThread(self.weather_thread)

    self.weather_thread.started.connect(self.weather_worker.run)
    self.weather_worker.succeeded.connect(self.show_weather)
    self.weather_worker.failed.connect(self.show_weather_error)

    self.weather_worker.finished.connect(self.weather_thread.quit)
    self.weather_worker.finished.connect(self.weather_worker.deleteLater)
    self.weather_thread.finished.connect(self.weather_thread.deleteLater)

    self.weather_thread.start()

def show_weather(self, data):
    conditions = get_current_conditions(data)
    self.main_temp_label.setText(f"{conditions['temperature']:.1f}")
    self.main_desc_label.setText(conditions["description"])
    self.city_name_label.setText(conditions["city"])

def show_weather_error(self, message):
    self.main_desc_label.setText(message)