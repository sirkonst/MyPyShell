# -*- coding: utf-8 -*-

"""
Выполнение shell комманд.

Пример:
    from shell import sh, ShellError
    try:
        print sh('ls -l')
    except ShellError, x:
        print x
"""

from shell import *

sh = Shell
