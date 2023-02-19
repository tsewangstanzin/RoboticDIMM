import serial
import time
class PowerController:
    def __init__(self):
        self.port2 = '/dev/ttyACM0'
        self.ser2 = serial.Serial(self.port2, baudrate=9600)
        time.sleep(2)
        return None
    def poweron(self):
        commandVal = "o\n"
        co = str.encode(commandVal)
        self.ser2.write(co)
        out = self.ser2.readline()
        print(out.decode())
    def poweroff(self):
        commandVal = "f\n"
        co= str.encode(commandVal)
        self.ser2.write(co)
        out = self.ser2.readline()
        print(out.decode())
def main():
    pw = PowerController()
    print("-----------Power  Control ----------")
    #pw.poweron()
    pw.poweroff()
if __name__ == '__main__':
    main()
