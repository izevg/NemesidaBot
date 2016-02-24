# -*- coding: utf-8 -*-

from telegram import Updater
import Commands
import logging

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)
c_handler = Commands.commands_dispatcher(logger=logger)

# def command_handler(bot, update, args):
#     Commands.execute_command(command_name=)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("197147060:AAGnUFbiFuW77NnXjFUEAHp95OMNmq2xJgI")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    for command in Commands.__all__:
        from Commands import *
        command_object = getattr(Commands, command)
        func = getattr(command_object, command)
        dp.addTelegramCommandHandler(command, func)
        logger.info(func)


    # main starting function
    dp.addTelegramCommandHandler("start", start)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
