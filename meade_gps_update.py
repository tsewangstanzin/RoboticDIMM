from meade_tel_control import Telescope
import time
def main():
    print("Updating Meade time and location (From GPS)")
    t1=Telescope(3, '/dev/ttyUSB0')
    t1.setGPS()
    time.sleep(60)
    print("GPS updated succesfully")
if __name__ == '__main__':
    main()