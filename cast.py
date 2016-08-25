import Modules

def cast_module(string_name):
    modules = __import__('Modules.%s' % string_name)
    command_object = getattr(modules, string_name)
    return command_object


def cast_func(string_name):
    command_object = cast_module(string_name)
    func = getattr(command_object, string_name)
    return func
