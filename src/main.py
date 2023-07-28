# Modules
from api.weather import Weather
from api.exchange_rate import ExchangeRate
from data.preprocessing import get_whole_day_forecast
from data.processing import get_df, get_report
from utilities.variables import weather
from api.twilio import send_message
import sys

# Logging
import logging.config
logging.config.fileConfig('./src/config/loggingFile.conf')


def main(city:str, phone_destination:str):

    logging.info('App has been initialized...')
    weather_api = Weather(city)
    exchange_rate_api = ExchangeRate("USD", "PEN,MXN")
    weather_api.request_api()
    exchange_rate_api.request_api()
    data = get_whole_day_forecast(weather_api.response)
    dfWeather = get_df(data, weather['columns'])
    dfRain = get_report(dfWeather)
    send_message(dfRain, phone_destination)
    logging.info('App finished successfully!!')

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print('The script needs a country and a phone destination')
    else:
        city = sys.argv[1]
        phone_destination = sys.argv[2]
        main(city, phone_destination)