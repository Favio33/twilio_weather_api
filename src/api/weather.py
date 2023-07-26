# Modules
from utilities.variables import api_key, base_url_weather
import requests

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('api')

class Weather:

    def __init__(self, url_request):
        
        logger.info('Instance Weather object...')
        self.url_request = url_request
        # self.response = self.request_api()

    @staticmethod
    def get_url_request(country: str, days = 1, aqi = 'no', alerts = 'no'):

        __api_key = api_key
        __base_url_weather = base_url_weather

        try:

            logger.info('Initialized get_url_request() static method ...')
            query  = f'&q={country}&days={days}&aqi={aqi}&alerts={alerts}'
            url_weather = f"{__base_url_weather}{__api_key}{query}"
            logger.info('get_url_request static method has been completed successfully! \n')
            return url_weather
        
        except Exception as ex:

            logger.error('Static method get_url_request has failed! Check the stacktrace: ', exc_info=True)
    

    def request_api(self):

        try:
            logger.info('Request Weather API...')
            response = requests.get(self.url_request)
            if response.status_code == 200:
                logger.info(f"Response {response.status_code} - Request has been executed successfully! \n")
                self.response =  response.json()
            else:
                logger.warning(f"Response {response.status_code}: Check the {__name__} method!", exc_info=True)
        except Exception as ex:
            logger.error(f"{__name__} executes incorrectly. Check the Stacktracer!", exc_info=True)
    