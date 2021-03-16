# CurrentWeatherGNexercise

Purpose: This is an API testing exercise.

Description: A small suite of API tests against the
Open Weather API - Current Weather feature.

How to run:

- Clone the project.
- Download and install _Pytest_ framework.
- Open the project in your favorite _IDE_ (I have used _PyCharm_).
- (An OpenWeather API key is required to be able to make 
  requests to CurrentWeather feature endpoints, which 
  can be retrieved from here: ​https://openweathermap.org/api​)
- In ```api_utils.py```, replace _"Please place your API key here."_, in the```api_key```variable,
  with your Open Weather API key.
- Tests can then be individually run by hitting the "play" button on 
  each of the tests in _test_current_weather_data_feature.py_.
  
Finally, you can run all tests in the test suite by opening a command line interface
and navigating to the path of the project directory and entering the following in the command line:
```python -m pytest```
