# -*- coding: utf-8 -*-

"""
Пример использования модуля:

from shell import ShellError, shell as sh

try:
    # run one command and print stdout
    print sh('ls -l')
    # run two and many command
    shell('ls -l', 'who')
    # run two and many command and print stdout
    print '\n'.join(sh.out for sh in shell('ls -l', 'who'))
    # or
    print shell('ls -l', 'who') # but in tuple
except ShellError, x:
    print x # Print stderr message

"""

from shell import *