# Modules
import pandas as pd
from tabulate import tabulate
import sys
from data.preprocessing import get_whole_day_forecast
from utilities.variables import weather

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('data')


def get_df (data, cols) -> pd.DataFrame:

    try:
        logger.info("get_df method has been initialized...")
        df = pd.DataFrame(data, columns= cols)
        logger.info(f"Dataframe has been created. Num Rows {df.shape[0]}")
        return df
    
    except Exception as ex:
        logger.error(f"get_df method has failed! Check the stack trace {str(ex)}")
        raise ex

def df_weather_report (api_response:dict) -> pd.DataFrame:

    try:
        data = get_whole_day_forecast(api_response)
        dfWeather = get_df(data, weather['columns'])
        logger.info('Method weather_report has been initialized...')
        dfRain = dfWeather[ (dfWeather['rainy_day'] == 1) & (dfWeather['hour'] > 6) & (dfWeather['hour'] < 23) ]
        logger.info("Dataframe has been filtered!")
        dfRain = dfRain[['hour', 'condition', 'date']].sort_values( by = 'hour', ascending= True).copy()
        logger.info('Dataframe has been orderes by hour')
        dfRain.set_index('hour', inplace=True)
        logger.info(f"Dataframe proccess successfully! Total of rows: {dfRain.shape[0]}", exc_info=True)
        return dfRain

    except Exception as ex:
        logger.error(f"weather_report method has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex


def weather_rainy_report(dfRain: pd.DataFrame) -> str:

    try:
        logger.info("weather_rainy_report has been initialized...")
        if dfRain.shape[0] == 0:
            return "Hoy es muy probable que no llueva!"
        else:
            weather_report_introduction = f"\nEl pronóstico de lluvia de hoy {dfRain['date'].values[0]} en {sys.argv[1]} es:\n"
            weather_report_data = tabulate(dfRain[['condition']], headers='keys', tablefmt='presto')
            return weather_report_introduction + weather_report_data
    except Exception as ex:
        logger.error(f"weather_rainy_report method has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex


def currency_exchange_report(exchange_currency_response: dict) -> str:

    try:
        logger.info("currency_exchange_report methos has been initialized...")
        rate = exchange_currency_response['rates']
        if len(rate) == 0:
            return "No se econtró información"
        elif len(rate) == 1:
            return f"\nEl cambio de {exchange_currency_response['base']} a {list(rate)[0]} es {list(rate.values()[0])}"
        else:
            report_str = f"El cambio de {exchange_currency_response['base']} para las divisas seleccionadas son:\n"
            for key, value in rate.items():
                report_str = report_str + f"\t {key} -> {value} \n"
            return report_str
    except Exception as ex:
        logger.error(f"currency_exchange_report method has failed! Check the Stack Trace: {str(ex)}", exc_info=True)