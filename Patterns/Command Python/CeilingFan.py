class CeilingFan:
    def __init__(self):
        self.HIGH = 3
        self.MEDIUM = 2
        self.LOW = 1
        self.OFF = 0
        self.speed = self.OFF
    def high(self):
        self.speed = self.HIGH
        print('Ceiling Fan Speed', self.speed)
    def medium(self):
        self.speed = self.MEDIUM
        print('Ceiling Fan Speed', self.speed)
    def low(self):
        self.speed = self.LOW
        print('Ceiling Fan Speed', self.speed)
    def off(self):
        self.speed = self.OFF
        print('Ceiling Fan Off')
    def getSpeed(self):
        return self.speed