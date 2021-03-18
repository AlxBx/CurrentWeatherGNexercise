from utils.api_utils import open_weather_api_call
from utils.api_utils import open_weather_api_call_by_id
from utils.api_utils import open_weather_api_call_by_geo_location
from utils.api_utils import open_weather_api_call_by_zip_code
from utils.api_utils import open_weather_api_call_with_language_support


# Positive path tests
# cw = current weather

def test_get_current_weather_by_city_name():
    current_weather_valid_city_name = open_weather_api_call("Cambridge")
    assert current_weather_valid_city_name.status_code == 200


def test_cw_by_city_name_response_body_is_not_empty():
    cw_by_city_name = open_weather_api_call("Cambridge")
    assert cw_by_city_name.json() == {}


def test_get_cw_by_city_id():
    current_weather_location_by_id = open_weather_api_call_by_id(2172677)
    assert current_weather_location_by_id.status_code == 200


def test_get_cw_by_city_geo_coord():
    assert open_weather_api_call_by_geo_location(35, 139).status_code == 200


def test_by_zip_code():
    assert open_weather_api_call_by_zip_code("94040,us").status_code == 200


def test_get_cw_by_language():
    assert open_weather_api_call_with_language_support(2172677, "fr").status_code == 200


# Negative path tests
def test_invalid_city_name():
    current_weather_invalid_location = open_weather_api_call("Non Existing")
    assert current_weather_invalid_location.status_code == 404


def test_invalid_city_id():
    current_weather_invalid_city_id = open_weather_api_call(76554435)
    assert current_weather_invalid_city_id.status_code == 404


def test_invalid_language():
    current_weather_invalid_language = open_weather_api_call_with_language_support("Cambridge", "Vulcan")

    # This API call still returns 200 Ok even with an invalid language,
    # because the language parameter is optional.
    assert current_weather_invalid_language.status_code == 200


