import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY_WAPI')
base_url_weather = 'http://api.weatherapi.com/v1/forecast.json?key='
city = 'Lima'
columns = ['time', 'temperature', 'condition', 'rainy_day', 'prob_rain', 'date']
