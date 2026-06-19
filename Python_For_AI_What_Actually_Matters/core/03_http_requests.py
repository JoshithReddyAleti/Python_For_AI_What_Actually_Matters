"""
core/03_http_requests.py
===========================
AI Engineering Roadmap 2026 · Episode 2

Pattern 3: HTTP Requests — Calling External APIs

Tool calling = calling APIs. This is the skill.
Run: python core/03_http_requests.py
"""

import requests
import os


def get_weather(city: str) -> dict:
    """
    Call the Open-Meteo API (free, no API key) and return weather data.
    This is exactly how weather_api.py in Episode 3 works.
    """
    # Step 1: Geocode the city name → coordinates
    geo_resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "format": "json"},
        timeout=10,
    )
    geo_resp.raise_for_status()
    geo = geo_resp.json()

    if not geo.get("results"):
        return {"error": f"City not found: {city}"}

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]
    name = geo["results"][0]["name"]

    # Step 2: Fetch current weather for those coordinates
    weather_resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "weather_code"],
            "timezone": "auto",
        },
        timeout=10,
    )
    weather_resp.raise_for_status()
    weather = weather_resp.json()

    current = weather.get("current", {})
    return {
        "location": name,
        "temperature": current.get("temperature_2m"),
        "unit": "C",
        "error": None,
    }


if __name__ == "__main__":
    print("\n=== HTTP Request Demo ===\n")
    print("Fetching weather for London...")
    try:
        result = get_weather("London")
        print(f"Result: {result}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    print("\n✅ Pattern 3 complete. Move to core/04_environment_variables.py")
