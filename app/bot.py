from telegram.ext import (Updater, CommandHandler,
                          InlineQueryHandler, Dispatcher, run_async)
from app.utils import load_data
from datetime import datetime
import logging


# you can place your token here
MY_TOKEN = '984695585:AAHE0knIkpzxo6SkeK55bgemJLz4L_elTHk'  

# use logging module to know when things don't work as expected
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\
                    - %(message)s',
                    level=logging.INFO)


@run_async
def news(update, context):
    # load data from database
    info = load_data(datetime.utcnow())
    chat_id = update.message.chat_id

    if info is None:
        context.bot.send_message(chat_id=chat_id,
                                 text="Sorry! There is no content!")

    # print(info)
    # if content is None then pass
    for i in info:
        if i.content is None:
            continue
        else:
            message = (i.content + ' - ' + i.link)
            context.bot.send_message(chat_id=chat_id, text=message)


def main():
    updater = Updater(MY_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('news', news))
    updater.start_polling()
    updater.idle()
