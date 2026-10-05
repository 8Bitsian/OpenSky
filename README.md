# OpenSky
OpenSky is a desktop weather application built with Python and PyQt5.
It uses the [OpenWeatherMap API](https://openweathermap.org/api) to retrieve and display current weather information for a city selected by the end user.

The application is designed to provide a simple GUI for viewing weather conditions, temperature, and other relevant data. 

## Acknowledgements
- @BroCodez on YouTube for providing the 12 hour Python tutorial that included the Weather API Project that started it all.
- OpenWeatherMap for providing the real-time weather data that this application is based on
- PyQt5 for the graphical user interface framework
- The Python community for useful libraries and documentation
- My Twitch community that watched me learn Python and stayed for the development of this project!

## Features

### Current Features

- Simple graphical user interface built with PyQt5
- Display the current temperature
- Convert temperature between Celsius and Fahrenheit
- Display current weather condition via icon and caption
- Display current city

### Planned Features

- Prompt end users to enter their OpenWeatherMap API key via pop up window
- Store API key so it remains available after the application closes
  - Store the API key securely via an encryption algorithm built-into the app
- Display additional weather information, including:
  - Wind speed and direction
  - Humidity
  - Air quality
  - Feel-like temperature
  - Atmospheric pressure
  - Visibility
  - Sunrise and sunset times
- Save multiple cities data
- Display multiplies cities current weather conditions
- Add real-time weather updates
- Add forecast for next week

## Preview

A preview image or animated GIF can be added here:

```markdown
![OpenSky Application Preview](images/preview.png)
```

## Technologies

- Python
- PyQt5
- OpenWeatherMap API
- JSON
- HTTP requests

## Requirements

- Python 3.8+
- An OpenWeatherMap API key
- Internet connection

### OpenWeatherMap API Key Setup

OpenSky requires an API Key from OpenWeatherMap to retrieve weather data

1. Create an account on [OpenWeatherMap API](https://openweathermap.org/api)
2. Generate an API key from your account dashboard
3. Start OpenSky
4. Enter the API key when prompted by the application

The planned version of OpenSky will allow users to enter their API key through a pop-up window and save it for future sessions.
The key should be stored using an operating-system-appropriate secure storage mechanism where possible.

## Security Notes

**DO NOT COMMIT YOUR PERSONAL API KEY TO GITHUB OR PLACE IN THE SOURCE CODE!**

API keys are sensitive credentials. Never commit them to the repository.
Before publishing the project, make sure that:
- API keys are excluded from Git with `.gitignore`
- Example configuration files contain placeholder values only
- API keys are not printed in error messages
- Existing exposed keys are revoked and regenerated
- Saved keys are protected as securely as possible for the target operating system

For development purposes, you may temporarily use an environment variable:
```bash
OPENWEATHER\_API\_KEY=your\_api\_key\_here
```

## License
This project is licensed under the _ Licenses. See the `LICENSE` file for more information.
