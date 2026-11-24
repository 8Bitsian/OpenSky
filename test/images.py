# Standard library imports
from pathlib import Path

# Third party imports
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtSvgWidgets import QSvgWidget

# Global variables
PROJECT_DIR = Path(__file__).resolve().parents[2]
ICON_DIR = PROJECT_DIR / "OpenSky" / "test" / "resources"

def get_icon_path(filename):
    """Return the path to an icon."""
    return ICON_DIR / filename

def load_icon(filename):
    """Load an SVG file into as a QIcon."""
    icon_path = get_icon_path(filename)
    icon = QIcon(str(icon_path))

    if icon.isNull():
        print(f"Could not load icon: {icon_path}")

    return icon

def create_svg_widget(parent, filename, object_name, width, height):
    """Create an SVG Widget w/specified parameters."""
    svg_path = get_icon_path(filename)
    
    if not svg_path.is_file():
        raise FileNotFoundError(f"SVG not found at: {svg_path}")

    svg = QSvgWidget(parent)
    svg.load(str(svg_path))
    svg.setObjectName(object_name)
    svg.setFixedSize(QSize(width, height))
    svg.setSizePolicy(
        QSizePolicy.Policy.Fixed,
        QSizePolicy.Policy.Fixed
    )

    if not svg.renderer().isValid():
        print(f"Could not load SVG: {svg_path}")
    else:
        print("SVG path:", svg_path)

    return svg

def create_current_weather_image(parent, filename):
    """Create a large image for current weather conditions."""
    return create_svg_widget(parent, filename, "current_weather_image", 180, 180)

def create_forecast_weather_image(parent, filename, day_index):
    """Create a small image for forecast day conditions"""
    return create_svg_widget(parent, filename, "forecast_weather_image", 32, 32)

def weather_icon_filename(condition):
    """Determine which svg image to load depending on the weather condition."""
    condition = condition.lower()

    if "thunder" in condition:
        return "thunderstorm.svg"
    if "drizzle" in condition:
        return "drizzle.svg"
    if any(word in condition for word in ("rain", "squalls")):
        return "rainy.svg"
    if "snow" in condition:
        return "snowy.svg"
    if any(word in condition for word in ("mist", "haze", "fog")):
        return "foggy.svg"
    if any(word in condition for word in ("few clouds", "scattered clouds", "broken clouds")):
        return "partly-cloudy-day.svg"
    if "overcast" in condition:
        return "cloudy.svg"
    if "clear sky" in condition:
        return "clear-day.svg"

    return "drizzle.svg"
