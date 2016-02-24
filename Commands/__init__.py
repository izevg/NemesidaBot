import os

__all__ = []
class commands_dispatcher(object):
    def __init__(self, logger):
        self.logger = logger
        self.commans_list = self.get_commands_list()



    def execute_command(self, command_name, args):
        reply = ""
        try:
            reply = command_name.command_name(*args)
        except Exception:
            self.logger.error(u"Exception in %s function [args: %s]" % (function.__name__, str(args)))


    def get_commands_list(self):
        global __all__
        for file in os.listdir("./Commands"):
            if file.endswith(".py") and file != "__init__.py":
                file = file[:-3]
                __all__.append(file)
        self.logger.info(__all__)
