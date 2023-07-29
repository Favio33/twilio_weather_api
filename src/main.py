# Modules
from api.weather import Weather
from api.exchange_rate import ExchangeRate
from data.processing import df_weather_report, currency_exchange_report, weather_rainy_report
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
    dfRain = df_weather_report(weather_api.response)
    rainy_weather_message = weather_rainy_report(dfRain)
    currency_exchange_message = currency_exchange_report(exchange_rate_api.response)
    final_message = rainy_weather_message + "\n" + currency_exchange_message
    send_message(final_message, phone_destination)
    logging.info('App finished successfully!!')

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print('The script needs a country and a phone destination')
    else:
        city = sys.argv[1]
        phone_destination = sys.argv[2]
        main(city, phone_destination)