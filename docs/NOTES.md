1. `main.py` starts the app by creating the main window and controller, then runs the Qt event loop
2. `main_window.py` builds the main window and exposes UI elements or small methods for updating them
3. `main_controller.py` connects button clicks and coordinates actions, such as requesting weatehr data or opening settings
4. `settings_dialog.py` contains the settings window
5. `ui/widgets/` cotnains reusable widget-creation code
6. `weather_service.py` makes the weather API request and handles its response
7. `weather_api_data.py` hold weather data structures, parsing, or constants
8. `resources` holds images and other files the app displays or uses
9. `qss` holds the stylesheet