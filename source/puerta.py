import time
import RPi.GPIO as GPIO
#door object
class puerta(object):
    def __init__(self,state=0,time_open=1,port=25):
        self.state =state #open/close
        self.time_open =time_open
        self.port = port
    #open: open the doopuertar
    def open(self):
       GPIO.output(self.port,1)
       time.sleep(self.time_open)
       GPIO.output(self.port,0)
    #close: close the door
    def close(self):
       GPIO.output(self.port,0)


