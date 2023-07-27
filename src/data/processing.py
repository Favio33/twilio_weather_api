# Modules
import pandas as pd

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('data')


def get_df (data, cols) -> pd.DataFrame:

    try:

        df = pd.DataFrame(data, columns= cols)
        return df
    
    except Exception as ex:
        logger.error(f"get_df method has failed! Check the stack trace {str(ex)}")
        raise ex

def get_report (df: pd.DataFrame) -> pd.DataFrame:

    try:

        logger.info('Method get_report has been initialized...')
        dfRain = df[ (df['rainy_day'] == 1) & (df['hour'] > 6) & (df['hour'] < 23) ]
        logger.info("Dataframe has been filtered!")
        dfRain = dfRain[['hour', 'condition', 'date']].sort_values( by = 'hour', ascending= True).copy()
        logger.info('Dataframe has been orderes by hour')
        dfRain.set_index('hour', inplace=True)
        logger.info(f"Dataframe proccess successfully! Total of rows: {dfRain.shape[0]}", exc_info=True)
        return dfRain

    except Exception as ex:
        logger.error(f"get_df method has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex