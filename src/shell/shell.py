# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

class ShellError(Exception):
    pass

class Shell:
    """
    Выполнение shell комманд в блокирующем режиме.
    Если код завершения не равен 0 генерируется исключение ShellError с сообщением об ошибке
    self.out и self.err содержат текст вывода комманды в stdout и stderr
    self.retcode - код возврата выполненной комманды
    """
    def __init__(self, command, test=False):
        if not test:
            com = Popen(command,  shell=True, stdout=PIPE, stderr=PIPE)
            com.wait()
            self.out = com.stdout.read().strip()
            self.err = com.stderr.read().strip()
            self.retcode = com.returncode
            if self.retcode != 0:
                raise ShellError, "Command '%s' return with code = %s and message:\n%s" % (command, self.retcode, self.err)
        else:
            print command
        
    def __str__(self):
        return self.out

