# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
import Modules
import logging
import cast

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)
c_handler = Modules.commands_dispatcher(logger=logger)

# def command_handler(bot, update, args):
#     Modules.execute_command(command_name=)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def error(bot, update, error):
    logger.info('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token="197147060:AAGnUFbiFuW77NnXjFUEAHp95OMNmq2xJgI")
    logger.info("Updater created")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    logger.info("Dispatcher created")

    # on different commands - answer in Telegram
    for command in Modules.__all__:
        func = cast.cast_func(command)
        dp.add_handler(CommandHandler(command, func, pass_args=True))
        logger.info("Handler added")


    # main starting function
    dp.add_handler(CommandHandler("start", start))
    logger.info("Start Handler added")

    # log all errors
    dp.add_error_handler(error)
    logger.info("Error Handler added")

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
