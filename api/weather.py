import requests

def get_current_weather():
    city = 'Taskent'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': 'fdbb38963e32212aebae7dae318c4af7'}
    response = requests.get(url, params=params)
    weather_data = response.json()
    return weather_data
