# Modules
from api.api import Api
from utilities.variables import exchange_rate

# Logging
import logging.config


logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('exchange_rate')


class ExchangeRate(Api):

    base_url_api = exchange_rate['base_url_er']

    def __init__(self, base_currency:str, exchange_currency:str):

        logger.info("Exchange Rate object...")
        super().__init__(self.base_url_api)
        self.base_currency = base_currency
        self.exchange_currency = exchange_currency
        self.params = self.__set_params(base_currency, exchange_currency)

    def __set_params(self, base_currency, exchange_currency):

        __api_key = exchange_rate['exchange_rate_api_key']

        try:
            logger.info('Initialized set_params() static method ...')
            params  = {
                "app_id":__api_key,
                "base":base_currency,
                "symbols":exchange_currency
            }
            logger.info('set_params static method has been completed successfully! \n')
            return params
        except Exception as ex:
            logger.error(f"__set_params method has failed! Check the Stack Trace: {str(ex)}", exc_info=True)
