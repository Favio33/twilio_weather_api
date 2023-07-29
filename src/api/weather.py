# Modules
from api.api import Api
from utilities.variables import weather

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('weather')

class Weather(Api):

    base_url_api = weather['base_url_weather']

    def __init__(self, city:str):
        logger.info('Instance Weather object...')
        super().__init__(self.base_url_api)
        self.city = city
        self.params = self.__set_params(city)

    def __set_params(country: str, days = 1, aqi = 'no', alerts = 'no'):

        __api_key = weather['weather_api_key']

        try:

            logger.info('Initialized set_params() static method ...')
            params  = {
                "key":__api_key,
                "q":country,
                "days":days,
                "aqi":aqi,
                "alerts":alerts
            }
            logger.info('set_params static method has been completed successfully! \n')
            return params
        
        except Exception as ex:
            logger.error('__set_params method has failed! Check the stacktrace: ', exc_info=True)
            raise ex
