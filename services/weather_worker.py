# Third library imports
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

# Local library imports
from services.weather_service import load_weather_data

class WeatherWorker(QObject):
    succeeded = pyqtSignal(dict)
    failed = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, api_key, city_name, units="metric"):
        super().__init__()
        self.api_key = api_key
        self.city_name = city_name
        self.units = units

    @pyqtSlot()
    def run(self):
        try:
            data = load_weather_data(
                self.api_key,
                self.city_name,
                self.units
            )
            self.succeeded.emit(data)
        except ValueError as error:
            self.failed.emit(str(error))
        except Exception as error:
            print(f"Unexpected weather error: {error}")
            self.failed.emit("An unexpected error occurred while loading weather.")
        finally:
            self.finished.emit()
