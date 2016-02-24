# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import Modules

def c_exec(args):
    result = Popen(args, stdout=PIPE).communicate()
    return result[0]
