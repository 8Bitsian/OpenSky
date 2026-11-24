# Standard library imports
import sys, os, requests
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

# Local-library imports
import images

# Third-party imports
from PyQt6.QtCore import QThread, pyqtSignal, QSize, QSettings
from PyQt6.QtWidgets import ( 
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QDialog,
    QDialogButtonBox
)

# Global Constants
BASE_URL = "https://api.openweathermap.org/data/2.5" # Add "weather" or "forecast"
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"

class SettingsWindow(QDialog):
    def __init__(self, settings, parent=None):
        super().__init__()
        self.setWindowTitle("API Test - Settings Dialog Window")
        self.settings = settings

        self.api_input = QLineEdit()
        self.api_input.setPlaceholderText("Enter your OpenWeatherMap API key")
        self.api_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.api_input.setText(settings.value("api_key", ""))

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter a city (e.g. London, GB)")
        self.city_input.setText(settings.value("city", ""))

        form = QFormLayout()
        form.addRow("API Key:", self.api_input)
        form.addRow("City:", self.city_input)

        self.unit_mode = settings.value("units", "metric")

        self.cunit_button = QPushButton("Celsius")
        self.funit_button = QPushButton("Fahrenheit")
        self.runit_button = QPushButton("Rankine")

        self.unit_buttons = {
            "metric": self.cunit_button,
            "imperial": self.funit_button,
            "standard": self.runit_button,
        }

        for units, button in self.unit_buttons.items():
            button.setCheckable(True)
            button.clicked.connect(lambda checked, units=units: self.set_units(units))

        self.unit_buttons[self.unit_mode].setChecked(True)

        row = QHBoxLayout()
        row.addWidget(self.cunit_button)
        row.addWidget(self.funit_button)
        row.addWidget(self.runit_button)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.save_settings)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(row)
        layout.addWidget(buttons)

    def set_units(self, units):
        self.unit_mode = units
        self.unit_buttons[units].setChecked(True)
    
    def save_settings(self):
        self.settings.setValue("api_key", self.api_input.text().strip())
        self.settings.setValue("city", self.city_input.text().strip())
        self.settings.setValue("units", self.unit_mode)
        self.accept()

class WeatherWorker(QThread):
    succeeded = pyqtSignal(dict, dict)
    failed = pyqtSignal(str)

    def __init__(self, city, api_key, units):
        super().__init__()
        self.city = city
        self.api_key = api_key
        self.units = units

    def run(self):
        try:
            geo_params = {
                "q": self.city,
                "limit": 5,
                "appid": self.api_key,
            }

            geocoder_response = requests.get(f"{GEOCODE_URL}", params=geo_params, timeout=10)
            geocoder_response.raise_for_status()

            matches = geocoder_response.json()
            if not matches:
                self.failed.emit(f"No location found for {self.city}.")
                return
            
            place = matches[0]
            lat = place["lat"]
            lon = place["lon"]

            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": self.units,
            }

            current_response = requests.get(f"{BASE_URL}/weather", params=params, timeout=10)
            current_response.raise_for_status()

            forecast_response = requests.get(f"{BASE_URL}/forecast", params=params, timeout=10)
            forecast_response.raise_for_status()

            self.succeeded.emit(
                current_response.json(),
                forecast_response.json(),
            )

        except requests.RequestException as error:
            self.failed.emit(str(error))
        except (KeyError, IndexError, TypeError):
            self.failed.emit("The location or weather response was unexpected.")

class WeatherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Weather - API Test")
        self.resize(460, 290)
        self.worker = None

        self.settings = QSettings("YourName", "DesktopWeather")
        self.unit_mode = self.settings.value("units", "metric")

        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)

        self.fetch_button = QPushButton("Get Weather")
        self.fetch_button.clicked.connect(self.fetch_weather)

        self.current_weather_image = images.create_current_weather_image(self, "drizzle.svg")

        self.current_label = QLabel("Enter a city and fetch weather.")
        self.current_label.setWordWrap(True)

        self.current_weather_image.setFixedSize(64, 64)

        current_row = QHBoxLayout()
        current_row.addWidget(self.current_weather_image)
        current_row.addWidget(self.current_label, 1)

        self.forecast_list = QListWidget()
        self.forecast_list.setIconSize(QSize(32,32))

        layout = QVBoxLayout(self)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.fetch_button)
        layout.addLayout(current_row)
        # layout.addWidget(self.current_label)
        layout.addWidget(QLabel("5 Day Forecast:"))
        layout.addWidget(self.forecast_list)

    def open_settings(self):
        dialog = SettingsWindow(self.settings, self)
        if dialog.exec():
            self.unit_mode = self.settings.value("units", "metric")

    def set_units(self, units):
        self.unit_mode = units
        self.fetch_weather()

    def fetch_weather(self):
        api_key = self.settings.value("api_key", "").strip()
        city_name = self.settings.value("city", "").strip()

        if not api_key:
            QMessageBox.warning(
                self, "Missing API Key",
                "Enter a valid OpenWeatherMap.org API key.",
            )
            return

        if not city_name:
            QMessageBox.warning(
                self, "Missing Location",
                "Enter a valid city name.",
            )
            return

        self.fetch_button.setEnabled(False)
        self.current_label.setText("Loading weather...")

        self.worker = WeatherWorker(city_name, api_key, self.unit_mode)
        self.worker.succeeded.connect(self.show_weather)
        self.worker.failed.connect(self.show_error)
        self.worker.finished.connect(lambda: self.fetch_button.setEnabled(True))
        self.worker.start()

    def display_temp(self, temp):
        if self.unit_mode == "standard": # API temperature is Kelvin
            return temp * 9 / 5
        return temp
    
    def temperature_unit(self):
        return {"metric": "°C", "imperial": "°F", "standard": "°R"}[self.unit_mode]

    def show_weather(self, current, forecast):
        condition = current["weather"][0]["description"]
        detailed = condition.capitalize()

        filename = images.weather_icon_filename(condition)
        self.current_weather_image.load(
            str(images.get_icon_path(filename))        
        )

        unit = self.temperature_unit()    
        temp = self.display_temp(current['main']['temp'])
        feels_like = self.display_temp(current["main"]["feels_like"])
        
        self.current_label.setText(
            f"{current['name']}: {temp:.1f} {unit}\n"
            f"{detailed}\n"
            f"Feels like {feels_like:.1f} {unit}\n"
        )

        # Forecast timestamps are UTC - shift to city's local time zone prior to grouping by date
        city_offset = timedelta(seconds=forecast["city"]["timezone"])
        days = defaultdict(lambda: {"temps": [], "conditions": []})

        for item in forecast["list"]:
            utc_time = datetime.strptime(
                item["dt_txt"], "%Y-%m-%d %H:%M:%S"
            ).replace(tzinfo=timezone.utc)

            local_date = (utc_time + city_offset).date()

            days[local_date]["temps"].append(item["main"]["temp"])
            condition = item["weather"][0]["description"].capitalize()
            days[local_date]["conditions"].append(condition)

        self.forecast_list.clear()

        for date in sorted(days)[:5]:
            day = days[date]
            high = max(day["temps"])
            low = min(day["temps"])
            forecast_w = Counter(day["conditions"]).most_common(1)[0][0]
            weekday = date.strftime("%a")
            display_date = date.strftime("%b-%d")

            filename = images.weather_icon_filename(forecast_w)
            icon = images.load_icon(filename)

            row_text = (
                f"{weekday} {display_date}   "
                f"{high:>7.1f} {unit}   "
                f"{low:>7.1f} {unit}   "
                f"{forecast_w}"
            )

            self.forecast_list.addItem(QListWidgetItem(icon, row_text))

    def show_error(self, message):
        self.current_label.setText("Could not load weather.")
        QMessageBox.critical(self, "Weather Request Failed", message)

def main():
    """API Test": How to use geocoding, current weather data, and five0-day forecast weather data APIs from OpenWeatherMap.org."""
    app = QApplication(sys.argv)

    window = WeatherWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    print(f"Running {__name__}\n")
    main()
    print("Closing program...")