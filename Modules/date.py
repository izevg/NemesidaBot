# -*- coding: utf-8 -*-

import utils

HELPTEXT = u"Модуль даты и времени.Отображает текущее время на сервере.\n\nФормат: /date"

def get_date():
    result = utils.c_exec(["date"])
    return result

def date(bot, update):
    reply = get_date()
    bot.sendMessage(update.message.chat_id, text=reply)
