# -*- coding: utf-8 -*-
import utils

HELPTEXT = u"Плагин пинга. Пингует определённый адрес определённым количеством запросов\nФормат: /ping [АДРЕС] [КОЛИЧЕСТВО_ЗАПРОСОВ]"

def c_ping(source, destination, requests_amount=1):
    result = []
    if requests_amount > 5:
        result.append(u"Превышен лимит запросов (максимум - 5, запрошено: %s)" % requests_amount)
    else:
        result = utils.c_exec(["ping", destination, "-c", str(requests_amount)])
    return result


def ping(bot, update, args=""):
    reply = ""
    length = len(args)
    if length > 2:
        reply = u"Не могу пинговать больше одного адреса =("
    elif length == 0:
        reply = u"Укажите адрес для пинга ;-)"
    elif length == 2:
        reply = c_ping(0, args[0], int(args[1]))
    else:
        reply = c_ping(0, args[0])
    bot.sendMessage(update.message.chat_id, text=reply)
