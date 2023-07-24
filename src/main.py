# Modules
from api.weather import Weather
from data.preprocessing import get_whole_day_forecast
from data.processing import get_df
from utilities.variables import city, columns

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')


def main():

    logging.info('App has been initialized...')
    api_request = Weather.get_url_request(city)
    weather_api = Weather(api_request)
    data = get_whole_day_forecast(weather_api.response)
    dfWeather = get_df(data, columns)
    logging.info('App finished successfully!!')

if __name__ == '__main__':
    main()