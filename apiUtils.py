import requests


def open_weather_api_call(location):

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": "Please insert your API key here"}
    open_weather_endpoint = requests.get(url, params=params)

    return open_weather_endpoint


def response_body():
    return open_weather_api_call("Cambridge").json()
