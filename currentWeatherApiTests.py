from apiUtils import open_weather_api_call


def test_get_location_ok():

    current_weather_valid_location = open_weather_api_call("Cambridge")

    assert current_weather_valid_location.status_code == 200


def test_invalid_location():

    current_weather_invalid_location = open_weather_api_call("Non Existing")

    assert current_weather_invalid_location.status_code == 404




