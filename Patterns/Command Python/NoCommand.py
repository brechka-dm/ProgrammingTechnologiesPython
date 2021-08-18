from Command import Command

class NoCommand(Command):
    def execute(self):
        return None
    def undo(self):
        return None
