def validate_weather_data(data):
    """Check that the API response contains fields needed by the UI."""
    if not isinstance(data, dict):
        raise ValueError("The weather service returned an invalid response.")

    main = data.get("main")
    weather = data.get("weather")

    if not isinstance(main, dict) or main.get("temp") is None:
        raise ValueError("The weather response is missing temperature data.")

    if (
        not isinstance(weather, list)
        or not weather
        or not isinstance(weather[0], dict)
    ):
        raise ValueError("The weather response is missing conditions data.")

    return data

def get_current_conditions(data):
    """Extract commonly displayed values from a validated API response."""
    validate_weather_data(data)

    main = data["main"]
    condition = data["weather"][0]

    return {
        "city": data.get("name", "Unknown"),
        "temperature": main["temp"],
        "feels_like": main.get("feels_like"),
        "humidity": main.get("humidity"),
        "description": condition.get("description", "Unknown").capitalize(),
        "condition": condition.get("main", ""),
        "icon_code": condition.get("icon", ""),
    }