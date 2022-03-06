from telegram import Update
from telegram.ext import CallbackContext

from constant import greetings


def greet_member(update: Update, context: CallbackContext):
    greeting = greetings.random()

    update.message.reply_text(greeting.format(update.message.from_user.name if not "Telegram" else "new member"))
    # if the name is "Telegram" to member has no name defined.. you can also just not send anything then
