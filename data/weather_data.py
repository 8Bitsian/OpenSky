def validate_weather_data(current, forecast):
    """Check that both the current and forecast API responses contains fields needed by the UI."""
    if not isinstance(current, dict):
        raise ValueError("The weather service returned an invalid response.")

    main = current.get("main")
    weather = current.get("weather")

    if not isinstance(main, dict) or main.get("temp") is None:
        raise ValueError("The weather response is missing temperature data.")

    if (
        not isinstance(weather, list)
        or not weather
        or not isinstance(weather[0], dict)
    ):
        raise ValueError("The current-weather response is missing conditions data.")

    if not isinstance(forecast, dict):
        raise ValueError("The forecast response is invalid.")

    entries = forecast.get("list")
    if not isinstance(entires, list) or not entries:
        raise ValueError("A forecast entry is missing required weather data.")

    for entry in entries:
        if (
            not isinstance(entry, dict)
            or not isinstance(entry.get("main"), dict)
            or entry["main"].get("temp") is None
            or not isinstance(entry.get("weather"), list)
            or not entry["weather"]
            or not isinstance(entry["weather"][0], dict)
        ):
            raise ValueError("A forecast entry is missing reuired weather data.")

    return current, forecast

def get_current_conditions(data):
    """Extract commonly displayed values from a validated API response."""
    validate_weather_data(data)

    main = data["main"]
    condition = data["weather"][0]
    sys_data = data.get("sys", {})

    return {
        "city": data.get("name", "Unknown"),
        "temperature": main["temp"],
        "feels_like": main.get("feels_like"),
        "humidity": main.get("humidity"),
        "description": condition.get("description", "Unknown").capitalize(),
        "condition": condition.get("main", ""),
        "icon_code": condition.get("icon", ""),
        "sunrise": sys_data.get("sunrise"),
        "sunset": sys_data.get("sunset"),
        "timezone": data.get("timezone", 0)
    }

def get_forecast_entries(data):
    """Return list of forecast time slots from a forecast response."""
    if not isinstance(data, dict) or not isinstance(data.get("list"), list):
        raise ValueError("The forecast response is invalid.")
    
    return data["list"]