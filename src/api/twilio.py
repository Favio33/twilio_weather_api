# Modules
from twilio.rest import Client
from dotenv import load_dotenv
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


def send_message (message: str, phone_destination: str):

    try:

        logger.info("send_message method has been initialized...")
        client = twilio_auth()
        logger.info("Twilio autorization succesful")
        message = client.messages.create(
            from_ = 'whatsapp:'+os.environ['PHONE_NUMBER'],
            body = "Hola estas suscrito al reporte del dia!\n" + message,
            to = 'whatsapp:'+phone_destination)
        logger.info("Message has been created...")
        print("SMS Send: " + message.sid)
    
    except Exception as ex:
        logger.error(f"send_message has failed! Check the stack trace {str(ex)}", exc_info=True)
        raise ex
