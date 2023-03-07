import pyvisa
from time import sleep 


class toellner:

    def __init__(self):
        self.baudrate = 9600
        self.timout = None
        self.modelNumber = None 
        self.VI_PID = None

        rm = pyvisa.ResourceManager()
        #print(rm.list_resources())
        PSU = rm.open_resource()


    def getCurrentVal():
        None

    def getVoltageVal(): 
        None

    def getPowerVal(): 
        None

    def setVoltageVal(): 
        None

#done