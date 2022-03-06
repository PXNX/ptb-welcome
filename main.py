"""
This file serves as an entry point to the program.
Here all the stuff is initialized and updates being handled.
"""

import logging

from telegram import ParseMode
from telegram.ext import (
    Updater, Defaults, Filters, MessageHandler,
)

import config
from message import greet_member

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    updater = Updater(config.TOKEN, defaults=Defaults(parse_mode=ParseMode.HTML))
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, greet_member))

    # Commands have to be added above
    # dp.add_error_handler(error)  # comment this one out for full stacktrace

    updater.start_webhook(
        "0.0.0.0",
        config.PORT,
        config.TOKEN,
        webhook_url=f"https://YOUR-PROJECT-NAME.herokuapp.com/{config.TOKEN}")
    updater.idle()
