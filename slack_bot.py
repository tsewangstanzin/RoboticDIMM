
import subprocess
import os

class Messenger:
    def __init__(self):
        return None
    def txtmessage(self,message):
        #process = subprocess.Popen(["pacmd unload-module module-loopback"], shell=True,
        #                           stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        #output, err = process.communicate()
        #process = subprocess.Popen(["pactl load-module module-loopback"], shell=True,
        #                           stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        #os.system("gnome-terminal -- 'cheese'")
        #output, err = process.communicate()



        cmd="slack chat send '"+message+"' '#seeing-plot-daily'"
        #os.system(cmd)
        process = subprocess.Popen([cmd], shell=True)
        output, err = process.communicate()
        print(output)
        '''
        process = subprocess.Popen(["sudo service rts2 start"], shell=True)
        output, err = process.communicate()
        os.system("gnome-terminal -- 'rts2-mon'")
        process = subprocess.Popen(["sudo rts2-camd-alta -d C1 -i"], shell=True)
        output, err = process.communicate()
        '''
    def filemessage(self, fileuploadname):

        cmd = "slack file upload "+fileuploadname+" '#seeing-plot-daily'"
        # os.system(cmd)
        process = subprocess.Popen([cmd], shell=True)
        output, err = process.communicate()
        print(output)


def main():
    print("\n :::::::::::::::::::::::::AUTOMATED OBSERVATION UPDATE BOT:::::::::::::::::::::: \n")
    messenger = Messenger()
    #mm = "Julley...Observation Over. tonights efficiency  from bot update : "
    #messenger.txtmessage(mm)
    #from datetime import datetime
    #Messenger().txtmessage("Ya Julley, Good Evening. Its flat time. Starting automated flat acquisition process.  \n\nSystem Date and Time (UTC): %s \n\nCORRECT ME IF MY TIME WRONG " % (
    #        datetime.now()))

    #messenger.filemessage("HA_Coeff_clicked.dat")
if __name__ == '__main__':
    main()
