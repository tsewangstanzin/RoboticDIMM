'''
read_AWS.py
@Tsewang Stanzin,IAO
'''
import serial
import argparse
from time import sleep
from datetime import datetime, timedelta


class Weather:
	def __init__(self, port='/dev/ttyS0'):
		self.port = port
		self.ser = serial.Serial(self.port,baudrate=9600,bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE,parity=serial.PARITY_NONE,timeout=4,write_timeout=4)
		self.ser.reset_input_buffer()
		self.ser.reset_output_buffer()
		self.WorkingDir=''
		return None
	def readAWS(self):
		self.ser.flush()
		cmd = '\x02XX\x03'
		#print("\nRS232 command:", cmd)
		self.ser.write(cmd.encode())
		out = self.ser.readline()
		recc = str(out.decode())
		print("\n",recc)
		self.ser.flush()
		cmd = '\x02mm\x03'
		self.ser.write(cmd.encode())
		out = self.ser.readline()
		recc=str(out.decode())
		arrc_rec=recc.split()
		if(len(arrc_rec)==13):
			return arrc_rec[11],arrc_rec[12],arrc_rec[1],arrc_rec[2],arrc_rec[3],arrc_rec[4],arrc_rec[5],arrc_rec[6],arrc_rec[7]
		else:
			print("TimeOUT,Might be waking up after sometime, wait")
			sleep(3)
			self.ser.flush()
			cmd = '\x02mm\x03'
			self.ser.write(cmd.encode())
			out = self.ser.readline()
			recc = str(out.decode())
			arrc_rec = recc.split()
			return arrc_rec[11], arrc_rec[12], arrc_rec[1], arrc_rec[2], arrc_rec[3], arrc_rec[4], arrc_rec[5],arrc_rec[6], arrc_rec[7]


def main():
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("-f",help="port",default='/dev/ttyS0')
	args = parser.parse_args()
	fw = Weather(port=args.f)
	while(1):
                dte,tme,ws,w_dr,tem,humi,prec,press,radia=fw.readAWS()
                f2 = open('Weather/Latest.txt', 'w')
                now = datetime.now()
                f2.write("%s %s %.2f %.2f %.2f %.2f %.2f %.2f %.2f %s\n" % (dte,tme,float(ws),float(w_dr),float(tem),float(humi),float(prec),float(press),float(radia),now))
                print("Date                :", dte)
                print("Time (IST)          :", tme)
                print("Wind Speed (m/s)    :", ws)
                print("Wind Direction(°)   :", w_dr)
                print("Temperature(°C)     :", tem)
                print("Relative Humidity(%):", humi)
                print("Precipitation (mm)  :", prec)
                print("Air Pressure  (hPa) :", press)
                print("Radiation     (W/sm):", radia)
                wd=str(dte)
                f3 = open(str('Weather/'+wd+'.txt'), 'a')
                f3.write("%s %s %.2f %.2f %.2f %.2f %.2f %.2f %.2f %s\n" % (dte,tme,float(ws),float(w_dr),float(tem),float(humi),float(prec),float(press),float(radia),now))
                sleep(5)
                
        
	
if __name__ == "__main__":
	main()
