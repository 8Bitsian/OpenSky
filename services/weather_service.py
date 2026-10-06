# Standard library imports
import requests

# Global Variables
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# Reuse one HTTP connection instead of creating a new one
SESSION = requests.Session()
# Prevent repeated requests for the same city/unit combo
_CACHE = {}

def load_weather_data(city_name, api_key, units="metric"):
    """Get request from openweathermap.org via your API key to get access to real-time weather"""

    city_name = city_name.strip()
    if not city_name:
        raise ValueError("Please enter a city.")

    api_key = api_key.strip()
    if not api_key:
        raise ValueError("Please enter your OpenWeather API key.")

    cache_key = (city_name.casefold(), units, api_key)
    if cache_key in _CACHE:
        return _CACHE[cache_key]

    params = {
        "q": city_name,
        "appid": api_key,
        "units": units
    }

    try:
        response = SESSION.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

    except requests.HTTPError as error:
        status = error.response.status_code if error.response else None
        if status == 401:
            raise ValueError("The API key was rejected.") from error
        if status == 404:
            raise ValueError("City not found.") from error
        raise ValueError(f"Weather service returned HTTP {status}.") from error

    except requests.Timeout as error:
        raise ValueError("The weather request timed out.") from error

    except requests.RequestException as error:
        raise ValueError("Unable to connect to the weather service.") from error

    except requests.exceptions.JSONDecodeError as error:
        raise ValueError("The weather service returned an invalid response.") from error

    _CACHE[cache_key] = data
    return data