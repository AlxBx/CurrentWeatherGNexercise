import requests

api_key = "Please place your API key here."
url = "http://api.openweathermap.org/data/2.5/weather"


def open_weather_api_call(location):
    params = {"q": location, "appid": api_key}
    open_weather_endpoint = requests.get(url, params=params)
    return open_weather_endpoint


def open_weather_api_call_by_id(city_id):
    params = {"id": city_id, "appid": api_key}
    open_weather_endpoint = requests.get(url, params=params)
    return open_weather_endpoint


def open_weather_api_call_by_geo_location(lat, lon):
    params = {"lat": lat, "lon": lon, "appid": api_key}
    open_weather_endpoint = requests.get(url, params=params)
    return open_weather_endpoint


def open_weather_api_call_with_language_support(id, lang):
    params = {"id": id, "lang": lang, "appid": api_key}
    open_weather_endpoint = requests.get(url, params=params)
    return open_weather_endpoint


def response_body(location):
    return open_weather_api_call(location).json()
