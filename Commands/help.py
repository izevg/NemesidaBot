
helptext = "Some help text here"

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text=helptext)
