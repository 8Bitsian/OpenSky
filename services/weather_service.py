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

    city_name = city_name.strip().lower()
    if not city_name:
        raise ValueError("Please enter a city.")

    api_key = api_key.strip()
    if not api_key:
        raise ValueError("Please enter your OpenWeather API key.")

    cache_key = (city_name.casefold(), units)
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

    except requests.HTTPError as error:
        if response.status_code == 401:
            raise ValueError("The API Key is invalid.") from error

        if response.status_code == 404:
            raise ValueError("City not found.") from error

        raise ValueError(f"Weather service returned HTTP {response.status_code}.") from error

    except requests.Timeout as error:
        raise ValueError("The weather reruest timed out.") from error

    except requests.RequestException as error:
        raise ValueError("Unable to connect to the weather services.") from error
    
    data = response.json()
    _CACHE[cache_key] = data
    return data