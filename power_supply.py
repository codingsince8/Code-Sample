#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      zdouglas
#
# Created:     25/09/2018
# Copyright:   (c) zdouglas 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
sys.path.append('c:/python26/Lib/site-packages/python-vxi11-master/')
import vxi11

class PowerSupply(object):

    def __init__(self, ip_address):
        "Generic VISA Instrument"
        idn_head = 'abstract'
        try:
            self.inst = vxi11.Instrument(ip_address)
            print("Connected to instrument")
        except:
            print("Error connecting to instrument at: {0}".format(ip_address))
            return


class SPD3303(PowerSupply):

    def __init__(self, ip_address):
        idn_head = 'Siglent Technologies,SPD3303'
        self.inst = vxi11.Instrument(ip_address)
        idn = self.inst.ask("*IDN?")
        if not idn.startswith(idn_head):
            print("Not connected to the correct instrument")

        else:
            print("Connected to Siglent power supply at: {0}".format(ip_address))

    def getID(self):
        "Gets the IDN"
        device_id = self.inst.ask("*IDN?")
        print device_id
        return device_id

    def getChannel(self):
        "Gets the Active Channel"
        activeChannel = self.inst.ask("INST?")
        print(activeChannel)
        return activeChannel

    def setChannel(self, channel):
        "Sets Active Channel"
        self.inst.write("INST CH{0}".format(channel))
        print("Active Channel Set")

    def getCurrent(self, channel = 1):
        channelCurrent = self.inst.ask("MEAS:CURR? CH{0}".format(channel))
        print(channelCurrent)
        return channelCurrent

    def setCurrent(self, current = 0 , channel = 1):
        self.inst.write("CH{0}:CURR {1}".format(channel, current))
        print("Channel {0} Current set to: {1}".format(channel, current))

    def getVoltage(self, channel = 1):
        channelVoltage = self.inst.ask("MEAS:VOLT? CH{0}".format(channel))
        print(channelVoltage)
        return channelVoltage

    def setVoltage(self, voltage = 0 , channel = 1):
        self.inst.write("CH{0}:VOLT {1}".format(channel, voltage))
        print("Channel {0} Voltage set to: {1}".format(channel, voltage))

    def setOutputOn(self, onOff = 1, channel = 1):
        if onOff == 1:
            self.inst.write("OUTP CH{0},ON".format(str(channel)))
            print("OUTP CH{0},ON".format(str(channel)))

        else:
            self.inst.write("OUTP CH{0},OFF".format(str(channel)))

    def setOutputMode(self, mode = 0):
        self.inst.write("OUTP:TRACK {0}".format(mode))


def main():
    ip_address = '192.168.2.175'
    powerSupply = SPD3303(ip_address)
    print powerSupply.getID()
    powerSupply.getVoltage()
    powerSupply.getCurrent()
    powerSupply.getChannel()
    powerSupply.setChannel(2)
    powerSupply.getChannel()
    powerSupply.setCurrent(2.8, 1)
    powerSupply.setVoltage(13.8, 1)


if __name__ == '__main__':
    main()
