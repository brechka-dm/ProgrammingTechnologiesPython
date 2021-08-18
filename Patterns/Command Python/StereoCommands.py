from Stereo import Stereo
from Command import Command

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise Exception('Invalid class parameter')
    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)
    def undo(self):
        self.stereo.off()

class StereoOnWithRadioCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise Exception('Invalid class parameter')
    def execute(self):
        self.stereo.on()
        self.stereo.setRadio()
        self.stereo.setVolume(15)
    def undo(self):
        self.stereo.off()

class StereoOffCommand(Command):
    def __init__(self, stereo):
        if isinstance(stereo, Stereo):
            self.stereo = stereo
        else:
            raise Exception('Invalid class parameter')
    def execute(self):
        self.prevVolume = self.stereo.getVolume()
        self.prevState = self.stereo.getState()
        self.stereo.off()
    def undo(self):
        self.stereo.on()
        if self.prevState == self.stereo.CD:
            self.stereo.setCD()
        elif self.prevState == self.stereo.DVD:
            self.stereo.setDVD()
        elif self.prevState == self.stereo.RADIO:
            self.stereo.setRadio()
        self.stereo.setVolume(self.prevVolume)
