import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25,GPIO.OUT)


class tarjeta(object):
	def __init__(self,id_number="",id_number_length=32):
		self.id_number = id_number
		self.id_number_length = id_number_length


	def function0(self,channel):
		self.id_number = self.id_number + "0"

	def function1(self,channel):
		self.id_number = self.id_number + "1"
	def validar(self):
		if(self.id_number == "00110001000100100111011100000010"):
			return 1
		else:
			return 0



class puerta(object):
	def __init__(self,state=0,time_open = 1):
		self.state = state
		self.time_open = time_open

	def open(self):
		GPIO.output(25,1)
		time.sleep(self.time_open)
		GPIO.output(25,0)
	def close(self):
		GPIO.output(25,0)

tarjeta1 =  tarjeta("",32)
puerta1  =  puerta(0,1)



GPIO.add_event_detect(23,GPIO.FALLING, callback=tarjeta1.function0)
GPIO.add_event_detect(24,GPIO.FALLING, callback=tarjeta1.function1)

while True:
	#Close the door by default
	puerta1.close()
	#wait for a card number
	while len(tarjeta1.id_number) < tarjeta1.id_number_length:
		time.sleep(0.1)
	#Validate user
	print tarjeta1.validar()

	#If user is validated then open the door
	if(tarjeta1.validar()):
		puerta1.open()	
			
	
	#Clear card information
	tarjeta1.id_number = ""
GPIO.cleanup()
	
	

