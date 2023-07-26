# Modules
from twilio.rest import Client
from dotenv import load_dotenv
from utilities.variables import city
import pandas as pd
import os

# Logging
import logging.config

logging.config.fileConfig("./src/config/loggingFile.conf")
logger = logging.getLogger('twilio')

load_dotenv()

def twilio_auth ():

    try:

        logger.info("twilio_auth has been initialized...")
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        logger.info("Credentials has been found successfully")
        return Client(account_sid, auth_token)

    except Exception as ex:
        logger.error(f"twilio_auth has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex

def generate_text (df: pd.DataFrame):

    try:

        logger.info('generate_text has been initialized...')
        text_part1 = f"\nHola! \n\n El pronóstico de lluvia de hoy {df['date'].values[0]} en {city} es: \n\n"
        text_part2 = str(df[['condition']])
        return text_part1 + text_part2

    except Exception as ex:
        logger.error(f"generate_text has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex


def send_message (df: pd.DataFrame, phone_destination: str):

    try:

        logger.info("send_message method has been initialized...")
        client = twilio_auth()
        logger.info("Twilio autorization succesful")
        message = client.messages.create(
            from_ = 'whatsapp:'+os.environ['PHONE_NUMBER'],
            body = generate_text(df),
            to = 'whatsapp:'+phone_destination)
        logger.info("Message has been created...")
        print("SMS Send: " + message.sid)
    
    except Exception as ex:
        logger.error(f"send_message has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex
