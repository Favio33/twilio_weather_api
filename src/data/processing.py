# Modules
import pandas as pd

# Logging
import logging.config

logging.config.fileConfig('./src/config/loggingFile.conf')
logger = logging.getLogger('data')


def get_df (data, cols) -> pd.DataFrame:

    df = pd.DataFrame(data, columns= cols)

    return df

def get_report (df: pd.DataFrame) -> pd.DataFrame:

    df = df.sort_values( by = 'Time', ascending= True)