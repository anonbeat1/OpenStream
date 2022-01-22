import logging
import time

import telegram.error
import telegram.ext
from telegram.ext import Updater

TELEGRAM_TOKEN = "<TELEGRAM_TOKEN>"
CHAT_ID = "<CHAT_ID>"

class TelegramCaller:
    def __init__(self):
        self.u = Updater(TELEGRAM_TOKEN, use_context=True)
        self.j = self.u.job_queue
    
    def send_message(self,message,count=0):
        try:
            
            if count < 3:
                try:
                    response = self.u.bot.send_message(CHAT_ID, message,timeout=5)
                    if not response :
                        raise  telegram.error.TelegramError
                except Exception as e:
                    logging.info("Handling first exception",e)
        except telegram.error.TelegramError as e:
            logging.warning("An error occured while sending message retrying... {}".format(count))
            time.sleep(1)
            self.send_message(message,count=+1)
        
        except Exception as e:
            logging.info("Failed to send message due to : ",e)
    
    def send_photo(self,photo,count=0):
        try:
            if count < 3:
                self.u.bot.send_photo(CHAT_ID, photo=open(photo, 'rb'))
        except telegram.error.TelegramError as e:
            logging.warning("An error occured while sending photo message retrying... {}".format(count))
            time.sleep(1)
            self.send_photo(photo,count=+1)
        
        except Exception as e:
            logging.info("Failed to send photo message due to : ",e)
