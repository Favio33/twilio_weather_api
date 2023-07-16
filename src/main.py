# Modules
from api.weather import Weather

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')


def main():

    logging.info('App has been initialized!')
    api_request = Weather.get_url_request('Perú')
    weather_api = Weather(api_request)
    print(weather_api.response)
    print(api_request)

if __name__ == '__main__':
    main()