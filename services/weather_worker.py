# Third library imports
from PyQt6.QtCore import QObject, QThread, pyqtSignal, pyqtSlot

# Local library imports
from services.weather_service import load_weather_data

class weather_worker(QObject):
    succeeded = pyqtSignal(dict)
    failed = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, city_name, api_key, units="metric"):
        super().__init__()
        self.city_name = city_name
        self.api_kay = api_key
        self.units = units

    @pyqtSlot()
    def run(self):
        try:
            data = load_weather_data(
                self.city_name,
                self.api_key,
                self.units
            )
            self.succeeded.emit(data)
        except ValueError as error:
            self.failed.emit(str(error))
        except Exception:
            self.failed.emit("An unexpected error occurred while loading weather.")
        finally:
            self.finished.emit()
