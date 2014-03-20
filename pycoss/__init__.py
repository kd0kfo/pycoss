import readline
import code
import atexit
import os.path

class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console_history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except IOError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.write_history_file(histfile)


class ArgumentError(Exception):
    pass


class CommandRunner(object):
    def __init__(self, commands):
        self.commands = commands

    def run_command(self, command, args):
        if not command:
            return
        if command not in self.commands:
            raise ArgumentError("Unknown Command: %s" % command)

    def help(self, command):
        if not command in self.commands:
            return None
        return self.commands[command]

    def list_commands(self):
        if not self.commands:
            return []
        return sorted(self.commands.keys())

    def argcount_assert(self, args, size, can_have_more=False):
        errmsg = "Invalid number of arguments"
        numargs = len(args)
        if numargs < size:
            raise ArgumentError(errmsg)
        if not can_have_more and numargs != size:
            raise ArgumentError(errmsg)