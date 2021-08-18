from CeilingFan import CeilingFan
from Command import Command

def setUndo(ceilingFan, prevSpeed):
    if prevSpeed==ceilingFan.HIGH:
        ceilingFan.high()
    elif prevSpeed==ceilingFan.MEDIUM:
        ceilingFan.medium()
    elif prevSpeed==ceilingFan.LOW:
        ceilingFan.low()
    elif prevSpeed==ceilingFan.OFF:
        ceilingFan.off()
    return ceilingFan

class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise Exception('Invalid class parameter')
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()
    def undo(self):
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)

class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise Exception('Invalid class parameter')
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()
    def undo(self):
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        if isinstance(ceilingFan, CeilingFan):
            self.ceilingFan = ceilingFan
        else:
            raise Exception('Invalid class parameter')
    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()
    def undo(self):
        self.ceilingFan = setUndo(self.ceilingFan, self.prevSpeed)