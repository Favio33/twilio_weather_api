import os
from dotenv import load_dotenv

load_dotenv()

weather = {
    "weather_api_key" : os.environ['API_KEY_WAPI'],
    "base_url_weather" : 'http://api.weatherapi.com/v1/forecast.json',
    "columns" : ['hour', 'temperature', 'condition', 'rainy_day', 'prob_rain', 'date']
}

exchange_rate = {
    "exchange_rate_api_key" : os.environ['API_KEY_ERAPI'],
    "base_url_er" : "https://openexchangerates.org/api/latest.json"
}