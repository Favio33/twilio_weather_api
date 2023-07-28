# Modules
import requests
import sys

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('api')


class Api():

    def __init__(self, base_url_api) -> None:
        self.base_url_api = base_url_api


    def request_api(self):

        try:
            logger.info("request_api method has been initialized...")
            response = requests.get(self.base_url_api, self.params)
            if response != None and response.status_code == 200:
                logger.info(f"Response {response.status_code} - Request has been successfully!")
                self.response = response.json()
            else:
                logger.error(f"Response {response.status_code}: Check the {__name__} method!", exc_info=True)
                sys.exit(1)
        except Exception as ex:
            logger.error(f"{__name__} executes incorrectly. Check the Stacktracer!", exc_info=True)
            raise ex