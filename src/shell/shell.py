# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

class ShellError(Exception): pass

class Shell:
    """
    Выполнение shell комманд в блокирующем режиме.
    Если код завершения не равен 0 генерируется исключение ShellError с сообщением об ошибке
    self.out и self.err содержат текст вывода комманды в stdout и stderr
    self.retcode - код возврата выполненной комманды
    self.command - исходная комманда
    """
    def __init__(self, command):
        com = Popen(command,  shell=True, stdout=PIPE, stderr=PIPE)
        com.wait()
        self.command = command
        self.out = com.stdout.read().strip()
        self.err = com.stderr.read().strip()
        self.retcode = com.returncode
        if self.retcode != 0:
            raise ShellError, self.err
    def __str_(self):
        return self.out
    def __repr__(self):
        return self.out

def shell(cmd, *cmds):
    """ Выполнить набор комманд и вернуть Shell объект """
    if cmds:
        return [Shell(cmd) for cmd in cmds]
    else:
        return Shell(cmd)

if __name__ == '__main__':
    try:
        print '\n'.join(sh.out for sh in shell('ls -l', 'who'))
        print shell('ls')
    except ShellError, x:
        print x
    