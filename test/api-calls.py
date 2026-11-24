# Standard library imports
import sys, os, requests
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

# Third-party imports
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import ( 
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)

# Global Constants
BASE_URL = "https://api.openweathermap.org/data/2.5" # Add "weather" or "forecast"
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"

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

        self.api_input = QLineEdit()
        self.api_input.setPlaceholderText("Enter your OpenWeatherMap API key")
        self.api_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter a city (e.g. London, GB)")

        form = QFormLayout()
        form.addRow("API Key:", self.api_input)
        form.addRow("City:", self.city_input)

        self.unit_mode = "metric"

        self.cunit_button = QPushButton("Celsius")
        self.funit_button = QPushButton("Fahrenheit")
        self.runit_button = QPushButton("Rankine")

        self.cunit_button.clicked.connect(lambda: self.set_units("metric"))
        self.funit_button.clicked.connect(lambda: self.set_units("imperial"))
        self.runit_button.clicked.connect(lambda: self.set_units("standard"))

        row = QHBoxLayout()
        row.addWidget(self.cunit_button)
        row.addWidget(self.funit_button)
        row.addWidget(self.runit_button)

        self.fetch_button = QPushButton("Get Weather")
        self.fetch_button.clicked.connect(self.fetch_weather)

        self.current_label = QLabel("Enter a city and fetch weather.")
        self.current_label.setWordWrap(True)

        self.forecast_list = QListWidget()

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(row)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.current_label)
        layout.addWidget(QLabel("5 Day Forecast:"))
        layout.addWidget(self.forecast_list)

    def set_units(self, units):
        self.unit_mode = units
        self.fetch_weather()

    def fetch_weather(self):
        api_key = self.api_input.text().strip()
        city_name = self.city_input.text().strip()

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
        detailed = current["weather"][0]["description"].capitalize()

        unit = self.temperature_unit()
        temp = self.display_temp(current['main']['temp'])
        feels_like = self.display_temp(current["main"]["feels_like"])

        self.current_label.setText(
            f"{current['name']}: {temp:.1f} {unit}\n"
            f"{detailed} · Feels like "
            f"{current['main']['feels_like']:.1f} {unit}\n"
            f"Humidity: {current['main']['humidity']}%"
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
            common_w = Counter(day["conditions"]).most_common(1)[0][0]
            weekday = date.strftime("%a")
            display_date = date.strftime("%b-%d")

            self.forecast_list.addItem(
                f"{weekday}   "
                f"{display_date}   "
                f"{high:>7.1f} {unit}   "
                f"{low:>7.1f} {unit}   "
                f"{common_w}"
            )

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