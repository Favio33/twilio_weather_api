# Modules
from api.weather import Weather
from data.preprocessing import get_whole_day_forecast
from data.processing import get_df, get_report
from utilities.variables import city, columns
from api.twilio import send_message
from dotenv import load_dotenv
import os

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')

load_dotenv()

def main():

    logging.info('App has been initialized...')
    api_request = Weather.get_url_request(city)
    weather_api = Weather(api_request)
    data = get_whole_day_forecast(weather_api.response)
    dfWeather = get_df(data, columns)
    dfRain = get_report(dfWeather)
    send_message(dfRain, os.getenv('PHONE_DESTINATION'))
    logging.info('App finished successfully!!')

if __name__ == '__main__':
    main()