# Modules
from api.weather import Weather
from data.preprocessing import get_whole_day_forecast
from data.processing import get_df, get_report
from utilities.variables import city, columns
from api.twilio import send_message
import sys

# Logging
import logging.config
logging.config.fileConfig('./src/config/loggingFile.conf')


def main(city:str, phone_destination:str):

    logging.info('App has been initialized...')
    api_request = Weather.get_url_request(city)
    weather_api = Weather(api_request)
    weather_api.request_api()
    data = get_whole_day_forecast(weather_api.response)
    dfWeather = get_df(data, columns)
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