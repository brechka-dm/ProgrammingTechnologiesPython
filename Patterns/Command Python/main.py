from RemoteControl import RemoteControl
from Light import Light
from Stereo import Stereo
from CeilingFan import CeilingFan
import LightCommands
import StereoCommands
import CeilingFanCommands

remote = RemoteControl()

livingRoomLight = Light()
bedRoomLight = Light()
bedRoomCeilingFan = CeilingFan()
stereo = Stereo()

livingRoomLightOn = LightCommands.LightOnCommand(livingRoomLight)
livingRoomLightOff = LightCommands.LightOffCommand(livingRoomLight)

bedRoomLightOn = LightCommands.LightOnCommand(bedRoomLight)
bedRoomLightOff = LightCommands.LightOffCommand(bedRoomLight)

ceilingFanMedium = CeilingFanCommands.CeilingFanMediumCommand(bedRoomCeilingFan)
ceilingFanHigh = CeilingFanCommands.CeilingFanHighCommand(bedRoomCeilingFan)
ceilingFanOff = CeilingFanCommands.CeilingFanOffCommand(bedRoomCeilingFan)

stereoCD = StereoCommands.StereoOnWithCDCommand(stereo)
stereoRadio = StereoCommands.StereoOnWithRadioCommand(stereo)
stereoOff = StereoCommands.StereoOffCommand(stereo)

remote.setCommand(0, livingRoomLightOn, livingRoomLightOff)
remote.setCommand(1, bedRoomLightOn, bedRoomLightOff)
remote.setCommand(2, ceilingFanMedium, ceilingFanOff)
remote.setCommand(3, ceilingFanHigh, ceilingFanOff)
remote.setCommand(4, stereoCD, stereoOff)
remote.setCommand(5, stereoRadio, stereoOff)

remote.onButtonPress(0)
remote.offButtonPress(0)
remote.undoButtonPress()

remote.onButtonPress(2)
remote.offButtonPress(2)
remote.undoButtonPress()

remote.onButtonPress(5)
remote.offButtonPress(5)
remote.undoButtonPress()
