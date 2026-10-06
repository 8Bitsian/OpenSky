# Standard library imports
from pathlib import Path

# Third party imports
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtSvgWidgets import QSvgWidget

# Global variables
PROJECT_DIR = Path(__file__).resolve().parent.parent
ICON_DIR = PROJECT_DIR / "resources" / "icons"

def get_icon_path(filename):
    """Return the path to an icon."""
    return ICON_DIR / filename

def load_icon(filename):
    """Load an SVG file into as an icon."""
    icon_path = get_icon_path(filename)
    icon = QIcon(str(icon_path))

    if icon.isNull():
        print(f"Could not load icon: {icon_path}")

    return icon