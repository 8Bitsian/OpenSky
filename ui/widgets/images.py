# Standard library imports
from pathlib import Path

# Third party imports
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSizePolicy
from PyQt6.QtSvgWidgets import QSvgWidget

# Global variables
PROJECT_DIR = Path(__file__).resolve().parent.parent
ICON_DIR = PROJECT_DIR / "resources" / "icons"

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

    svg = QSvgWidget(str(svg_path), parent)
    svg.setObjectName(object_name)
    svg.setFixedSize(QSize(width, height))
    svg.setSizePolicy(
        QSizePolicy.Policy.Fixed,
        QSizePolicy.Policy.Fixed
    )

    if not svg.renderer().isValid():
        print(f"Could not load SVG: {svg_path}")

    return svg

def create_current_weather_image(parent, filename):
    """Create a large image for current weather conditions."""
    return create_svg_widget(parent, filename, "current_weather_image", 180, 180)

def create_forecast_weather_image(parent, filename, day_index):
    """Create a small image for forecast day conditions"""
    return create_svg_widget(parent, filename, "forecast_weather_image", 48, 48)