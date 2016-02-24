import Modules

def cast_module(string_name):
    from Modules import *
    command_object = getattr(Modules, string_name)
    return command_object


def cast_func(string_name):
    command_object = cast_module(string_name)
    func = getattr(command_object, string_name)
    return func
