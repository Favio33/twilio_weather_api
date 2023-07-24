# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('data')


def get_forecast(response, itr):

    try:

        logger.info('get_forecast function has been initialized...')
        time = int(response['forecast']['forecastday'][0]['hour'][itr]['time'].split()[1].split(':')[0])
        logger.info('time get successfully!')
        temperature_c = float(response['forecast']['forecastday'][0]['hour'][itr]['temp_c'])
        logger.info('temperatue in celsius get successfully!')
        condition = response['forecast']['forecastday'][0]['hour'][itr]['condition']['text']
        logger.info("weather's condition get successfully!")
        rainy_day = response['forecast']['forecastday'][0]['hour'][itr]['will_it_rain']
        logger.info("rainy_day get successfully!")
        prob_rain = response['forecast']['forecastday'][0]['hour'][itr]['chance_of_rain']
        logger.info("probability of rain get successfully!")
        logger.info("get_forecast functions has been executed succesfully!")
        return [time, temperature_c, condition, rainy_day, prob_rain]

    except Exception as ex:
        logger.error(f"get_forecast has failed! Check the Stacktrace: \n", exc_info=True)


def get_whole_day_forecast(response):

    try:
        data_forecast = []
        date = response['forecast']['forecastday'][0]['date']
        logger.info("get_whole_day_forecast functionas has been initialized...")
        for itr in range(len(response['forecast']['forecastday'][0]['hour'])):
            forecast = get_forecast(response, itr)
            forecast.append(date)
            data_forecast.append(forecast)
        logger.info('get_whole_day_forecast has been executed successfully!')
        return data_forecast
    except Exception as ex:
        logger.error(f"get_whole_day_forecast has failed! Check the Stacktrace: \n", exc_info=True)