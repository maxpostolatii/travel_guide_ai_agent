from datetime import date

import requests

weathercode_map = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing rain (light)",
    67: "Freezing rain (heavy)",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    80: "Rain showers (slight)",
    81: "Rain showers (moderate)",
    82: "Rain showers (violent)",
    95: "Thunderstorm",
    96: "Thunderstorm with hail (light)",
    99: "Thunderstorm with hail (heavy)"
}


def get_weather(city: str, day: date = None) -> dict:
    # Step 1: Get coordinates
    geo = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city, "count": 1}).json()
    if not geo.get("results"):
        return {"error": f"Could not find location for '{city}'"}

    loc = geo["results"][0]
    lat, lon = loc["latitude"], loc["longitude"]

    # Step 2: Build params
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": "auto",
    }

    if day and day > date.today():
        params["daily"] = "weathercode,temperature_2m_max,temperature_2m_min"
        params["start_date"] = params["end_date"] = day.isoformat()
    else:
        params["current_weather"] = True

    # Step 3: Get weather data
    resp = requests.get("https://api.open-meteo.com/v1/forecast", params=params).json()

    if "current_weather" in resp:
        code = resp["current_weather"]["weathercode"]
        desc = weathercode_map.get(code, f"Unknown ({code})")
        return {
            "city": city,
            "temperature": resp["current_weather"]["temperature"],
            "conditions": desc,
            "geo": {"lat": lat, "lon": lon},
            "date": day or date.today()
        }
    elif "daily" in resp and "temperature_2m_max" in resp["daily"]:
        code = resp["daily"]["weathercode"][0]
        desc = weathercode_map.get(code, f"Unknown ({code})")
        return {
            "city": city,
            "temperature": resp["daily"]["temperature_2m_max"][0],
            "conditions": desc,
            "geo": {"lat": lat, "lon": lon},
            "date": day or date.today()
        }

    return {"error": "Unable to retrieve weather data."}