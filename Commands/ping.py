# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

def c_ping(source, destination):
    result = Popen(["ping", destination, "-c", "1"], stdout=PIPE).communicate()
    return result[0]


def ping(bot, update, args):
    reply = ""
    if len(args) != 1:
        reply = u"Не могу пинговать больше одного адреса =("
    else:
        reply = c_ping(0, args[0])
    bot.sendMessage(update.message.chat_id, text=reply)
