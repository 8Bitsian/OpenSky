# OpenSky
OpenSky is a desktop weather application built with Python and PyQt5. It uses the [OpenWeatherMap API](https://openweathermap.org/api) to retrieve and display current weather information for a city selected by the end user.

The application is designed to provide a simple graphical interface for viewing weather conditions, temperature, and other relevant data.

## Project Status

OpenSky is currently under active development. The core weather display functionality is available, while additional features are planned for future releases.

## Acknowledgements

- @BroCodez on YouTube for providing the 12 hour Python tutorial that included the Weather API Project that started it all.
- OpenWeatherMap for providing the real-time weather data that this application is based on
- PyQt5 for the graphical user interface framework
- The Python community for useful libraries and documentation
- My Twitch community that watched me learn Python and stayed for the development of this project!

## Contributing

Suggestions, bug reports, and contributions are welcome!

1. Fork the repository
2. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes
```bash
git commit -m "Add your feature description"
``*
```
4. Push the branch*
```bash
git push origin feature/your-feature-name
```
5. Open a pull request*

## Features

### Current Features

- Desktop graphical user interface built with PyQt5
- Display the current temperature
- Convert temperature between Celsius and Fahrenheit
- Display the current weather condition
- Display a weather icon and condition caption
- Display the current city
- Retrieve weather data through the OpenWeatherMap API

### Planned Features

- Prompt users to enter their OpenWeatherMap API key through a dialog window
- Store the API key for use in future sessions
- Store API credentials using secure operating-system credential storage
- Display additional weather information, including:
  - Wind speed and direction
  - Humidity
  - Air quality
  - Feels-like temperature
  - Atmospheric pressure
  - Visibility
  - Sunrise and sunset times
- Save multiple cities
- Display current weather conditions for saved cities
- Automatically refresh weather data at regular intervals
- Display a multi-day weather forecast
- Add improved loading indicators and error messages
- Add customizable application settings

## Preview

A preview image or animated GIF can be added here:

```markdown
![OpenSky Application Preview](images/preview.png)
```

## Technologies

- Python
- PyQt5
- QSS
- OpenWeatherMap API
- Requests
- JSON
- HTTP

## Requirements

- Python 3.8 or newer
- An OpenWeatherMap API key
- An active internet connection

### Known Limitations

- An internet connection is required to retrieve weather data
- A valid OpenWeatherMap API key is required*
- Weather data depends on the availability and accuracy of the OpenWeatherMap service
- API request limits may apply depending on the selected OpenWeatherMap plan*

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR\_USERNAME/OpenSky.git
```
2. Navigate to the project directory:
```bash
cd OpenSky
```
3. Create the virtual environment:
```bash
python -m venv venv
```
5. Activate the virtual environment
   - For Windows end users:
   ```bash
   venv\Scripts\activate
   ```
   - For Linux or macOS end users:
   ```bash
   source venv/bin/activate
   ```
6. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## OpenWeatherMap API Key Setup

OpenSky requires an API Key from OpenWeatherMap to retrieve weather data

1. Create an account on [OpenWeatherMap API](https://openweathermap.org/api)
2. Generate an API key from your account dashboard
3. Configure the key according to the application's setup instructions
4. Start OpenSky

For development, the API key may be provided through an environment variable:
```bash
OPENWEATHER\_API\_KEY=your\_api\_key\_here
```

On Windows Powershell:
```powershell
\$env:OPENWEATHER\_API\_KEY = "your\_api\_key\_here"
```

The planned version of OpenSky will allow users to enter their API key through an in-app dialog and save it for future sessions.

Where possible, API keys should be stored using the operating system's secure credential manager. The application should not implement custom encryption for sensitive credentials.

## Running the Application

Run the application with:
```bash
python main.py
```

## License
## License

OpenSky is licensed under the GNU General Public License v3.0.

See the [LICENSE](LICENSE) file for the complete license text.

This project uses PyQt5, which is available under the GNU GPL or a commercial license. OpenSky is distributed as an open-source GPL-licensed application.
