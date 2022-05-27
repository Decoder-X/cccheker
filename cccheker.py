import logging
import requests
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

utl = "https://lookup.binlist.net/"
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)
BIN = range(1)
c = b'\xf0\x9f\x92\xb3'
b = b'\xf0\x9f\x92\xb0'
m = b'\xf0\x9f\x93\xb1'
w = b'\xf0\x9f\x8c\x90'
x = b'\xe2\x9d\x8c'
r = b'\xe2\x9c\x85'
def start(update, context):
  user = update.message.from_user
  update.message.reply_text("Hey "+ user.name +" , Hoppefully you are fine. To start this bot You need to command like this /check 48********* Thank You. ")

def check(update, context):
    try:
        bin = context.args[0].split("|")[0]
        p = requests.get(f"{utl}{bin}")
        js = json.loads(p.text)
        update.message.reply_text(r.decode() + "  Valid Card  " + "\n\n" +
                                  c.decode() + "BIN      " + bin + "\n\n" +
                                  c.decode() + "Card Brand    " +
                                  js["scheme"] + "\n\n" + c.decode() +
                                  "Card Type     " + js["type"] + "\n\n" +
                                  b.decode() + "Bank Name     " +
                                  js["bank"]["name"] + "\n\n" + c.decode() +
                                  "Card Level    " + js["brand"] + "\n\n" +
                                  w.decode() + "Country       " +
                                  js["country"]["name"] +
                                  js["country"]["emoji"] + "\n\n" +
                                  m.decode() + "Phone         " +
                                  js["bank"]["phone"] + "\n\n")
    except :
        update.message.reply_text(x.decode() + "Your card Is not valid\n"
                                 "Or You type Wrong\n"
                                 "Example /check 48***********")


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Exmaple /check Your_card_Number' + "\n"+ +
                              '/check 548*******')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this wil=  no longer be necessary
    updater = Updater("5331483753:AAFmKsk_Qwv6EzSyfOnWGg-liMs3ZmN1a3M",
                      use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    try:
      dp.add_handler(CommandHandler("start", start))
      dp.add_handler(CommandHandler("check", check))
      dp.add_handler(CommandHandler("help", help))
    except Exception as e:
      print(e)

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    try:
      main()
    except Exception as e:
      print(e)