import serial
import time
from datetime import datetime
import time
import numpy
from astropy.coordinates import SkyCoord

class Telescope:
    def __init__(self, timeOut, serialPort, baud=9600, test=False):
        print("Telescope Found: ",serialPort)

        if (test == False):
            self.ser = serial.Serial(
                port=serialPort,
                baudrate=baud,
                parity=serial.PARITY_NONE,
                bytesize=serial.EIGHTBITS,
                stopbits=serial.STOPBITS_ONE,
                timeout=timeOut
            )
        else:
            self.ser = None

    def getSerialPort(self):
        print(self.ser)
        return self.ser
    #Homing
    def findHome(self):
        commandVal = ":hF#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
    def HomeStatus(self):
        commandVal = ":h?#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    #GET funtions:
    def getSlewStatus(self):
        commandVal = ":D#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def gettelescopeTime(self):
        commandVal = ":Ga#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def getUpperLimit(self):
        commandVal = ":Gh#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def getLowerLimit(self):
        commandVal = ":Go#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def getTelAlt(self):
        commandVal = ":GA#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def getTelAz(self):
        commandVal = ":GZ#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def getTelRA(self):
        commandVal = ":GR#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    def getTelDEC(self):
        commandVal = ":GD#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        return s
    #SET funtions:
    def setPrecision(self):
        commandVal = ":U#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
    def setGPS(self):
        # :gps to turn on gps
        commandValSetGPS = ":g+#"
        commandValSetGPS = str.encode(commandValSetGPS)
        self.ser.write(commandValSetGPS)
        #s = self.ser.read(20)
        #return s
        time.sleep(2)
        commandValSetGPS = ":gT#"
        commandValSetGPS = str.encode(commandValSetGPS)
        self.ser.write(commandValSetGPS)
        s = self.ser.read(20)
        return s
    def setUpperLimit(self):
        # :gps to turn on gps
        commandValSetGPS = ":So85.6*#"
        commandValSetGPS = str.encode(commandValSetGPS)
        self.ser.write(commandValSetGPS)
        time.sleep(1)
        s = self.ser.read(20)
        return s
    def setLoweLimit (self):
        commandValSetGPS = ":Sh20*#"
        commandValSetGPS = str.encode(commandValSetGPS)
        self.ser.write(commandValSetGPS)
        time.sleep(1)
        s = self.ser.read(20)
        return s
    def setSpeed(self, num):
        commsList = [":RG#", ":RC#", ":RM#", ":RS#"]
        if (num in [0, 1, 2, 3]):
            commandValSpeed = commsList[num]
            commandValSpeed = str.encode(commandValSpeed)
            self.ser.write(commandValSpeed)
    def setGuideRate(self):

        commandValSetRArate = ":RA0.00416667#"
        commandValSetRArate = str.encode(commandValSetRArate)
        self.ser.write(commandValSetRArate)
        commandValSetDECrate = ":RE0.00416667#"
        commandValSetDECrate = str.encode(commandValSetDECrate)
        self.ser.write(commandValSetDECrate)
    def setPointRate(self):
        commandValSetRArate = ":RA0.04#"
        commandValSetRArate = str.encode(commandValSetRArate)
        self.ser.write(commandValSetRArate)
        commandValSetDECrate = ":RE0.04#"
        commandValSetDECrate = str.encode(commandValSetDECrate)
        self.ser.write(commandValSetDECrate)

    def setPointRateSlow(self):
        commandValSetRArate = ":RA0.01#"
        commandValSetRArate = str.encode(commandValSetRArate)
        self.ser.write(commandValSetRArate)
        commandValSetDECrate = ":RE0.01#"
        commandValSetDECrate = str.encode(commandValSetDECrate)
        self.ser.write(commandValSetDECrate)
    def telescopeAutoAlign(self):
        commandVal = ":Aa#"
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        time.sleep(1)
        s = self.ser.read(20)
        return s

    def telescopeMoveWest(self, moveTime):
        print("Moving West by second: ", moveTime)
        commandValStartSlew = ":Mw#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qw#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()

    def telescopeMoveNorth(self, moveTime):
        print("Moving North by second: ", moveTime)
        commandValStartSlew = ":Mn#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qn#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()

    def telescopeMoveSouth(self, moveTime):
        print("Moving South by second: ", moveTime)
        commandValStartSlew = ":Ms#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qs#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()

    def telescopeMoveEast(self, moveTime):
        print("Moving East by second: ", moveTime)
        commandValStartSlew = ":Me#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
        print("Moving")
        time.sleep(moveTime)
        commandValStopSlew = ":Qe#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
        print("Ending Movement")
        print()
    def Park(self):
        print("Parking")
        commandValStartSlew = ":hP#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)
    def RADECPointing(self,rh,rm,rs,decs,dd,dm,ds):
        commandVal = ":Sr"+str(rh)+"*"+str(rm)+":"+str(rs)+"#"
        print("RA command received: %s"%(commandVal))
        commandVal = str.encode(commandVal)
        self.ser.write(commandVal)
        s = self.ser.read(20)
        commandVal2 = ":Gr#"
        commandVal2 = str.encode(commandVal2)
        self.ser.write(commandVal2)
        s = self.ser.read(20)
        commandVal2 = ":Sd"+str(decs)+str(dd)+"*"+str(dm)+":"+str(ds)+"#"
        print("DEC command received: %s" % (commandVal2))
        commandVal2 = str.encode(commandVal2)
        self.ser.write(commandVal2)
        s = self.ser.read(20)
        commandVal2 = ":Gd#"
        commandVal2 = str.encode(commandVal2)
        self.ser.write(commandVal2)
        s = self.ser.read(20)
        #time.sleep(10)
        commandVal3 = ":MS#"
        commandVal3 = str.encode(commandVal3)
        self.ser.write(commandVal3)
        s = self.ser.read(20)
        return s

    def startEast(self):
        commandValStartSlew = ":Me#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endEast(self):
        commandValStopSlew = ":Qe#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
    def startWest(self):
        commandValStartSlew = ":Mw#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endWest(self):
        commandValStopSlew = ":Qw#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)

    def startNorth(self):
        commandValStartSlew = ":Mn#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endNorth(self):
        commandValStopSlew = ":Qn#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)
    def startSouth(self):
        commandValStartSlew = ":Ms#"
        commandValStartSlew = str.encode(commandValStartSlew)
        self.ser.write(commandValStartSlew)

    def endSouth(self):
        commandValStopSlew = ":Qs#"
        commandValStopSlew = str.encode(commandValStopSlew)
        self.ser.write(commandValStopSlew)


def main():
    print("-----------Meade Telescope Control ----------")
    '''
    # sudo chmod 666 /dev/ttyUSB0
    # lsusb
    # ls -l /sys/bus/usb-serial/devices
    t1 = Telescope(3, '/dev/ttyUSB0')
    t1.telescopeTime()
    #t1.telescopeAutoAlign()
    #t1.WakeUp()
    t1.setSpeed(3)

    t1.telescopeMoveSouth(2)
    time.sleep(2)
    t1.telescopeMoveNorth(5)
    time.sleep(2)

    t1.telescopeMoveEast(5)
    time.sleep(2)
    t1.telescopeMoveWest(5)
    time.sleep(2)

    #t1.Park()
    # t1.setGPS()
    t1.ser.close()
    '''


if __name__ == '__main__':
    main()
