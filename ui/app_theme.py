# Standard-library imports
from pathlib import Path

# Third-party imports
from PyQt6.QtCore import QFile, QIODevice, QTextStream
from PyQt6.QtGui import QFontDatabase

# Global variables
BASE_DIR = Path(__file__).resolve().parent.parent

COLORS = {
    "BRICK_EMBER": "#B80C09",
    "YALE_BLUE": "#0B4F6C",
    "BRIGHT_SKY": "#01BAEF",
    "GHOST_WHITE": "#FBFBFF",
    "INK_BLACK": "#040F16"
}

def load_fonts():
    """Load the application fonts."""
    font_dir = BASE_DIR / "resources" / "fonts"

    for font_path in font_dir.glob("*.ttf"):
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id == -1:
            print(f"Could not load font: {font_path}")

# Load the QSS Style sheet
def load_stylesheet(app, file_path=None):
    """Load the style sheet and replace color keywords."""
    if file_path is None:
        file_path = BASE_DIR / "resources" / "qss" / "styles.qss"

    file = QFile(str(file_path))
    mode = QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text

    if not file.open(mode):
        print(f"Could not load stylesheet: {file_path}")
        return

    try:
        stylesheet = QTextStream(file).readAll()
    finally:
        file.close()

    for color_name, hex_color in COLORS.items():
        stylesheet = stylesheet.replace(f"{{{{{color_name}}}}}", hex_color)
    
    app.setStyleSheet(stylesheet)