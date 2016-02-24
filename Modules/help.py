# -*- coding: utf-8 -*-
import cast
import Modules

HELPTEXT = u"Модуль помощи в работе с ботом.\n\nВызов команды без параметров - отображение данного текста;\n/help ИМЯ_КОМАНДЫ - помощь по команде.\n\n Список доступных команд: %s" % Modules.__all__

def help(bot, update, args):
    helptext = ""
    if len(args) != 0:
        module = cast.cast_module(args[0])
        helptext = module.HELPTEXT
    else:
        helptext = HELPTEXT
    bot.sendMessage(update.message.chat_id, text=helptext)
