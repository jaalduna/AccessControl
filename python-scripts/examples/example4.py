import sqlite3 as lite
import sys

import RPi.GPIO as GPIO #gpio libarry for raspberry pi
import time #for make delays


#Parameters
TIME_OPEN = 10 # time (seconds) the door remains open after a succesfull login


#GPIO configurations#
GPIO.setmode(GPIO.BCM) #use the physical nomenclature
GPIO.setup(23,GPIO.IN, pull_up_down = GPIO.PUD_UP) #DATA0 card reader weingand Interface
GPIO.setup(24,GPIO.IN, pull_up_down = GPIO.PUD_UP) #DATA1 card reader weingand Interface
GPIO.setup(25,GPIO.OUT) # door actuator output
####################

#card object
class tarjeta(object):
	def __init__(self,id_number="",id_number_length=32):
		self.id_number = id_number #card unique identifier
		self.id_number_length = id_number_length #expected length for id number

	#function0: append a 0 to id_number
	def function0(self,channel):
		self.id_number = self.id_number + "0"
	#function1: append a 1 to id_number
	def function1(self,channel):
		self.id_number = self.id_number + "1"
    
	#validar: check if id_number is on the database. If the test is positive the function return 1, else it return 0.
	def validar(self):
		if(self.id_number == "00110001000100100111011100000010"):
			return 1
		else:
			return 0


#door object
class puerta(object):
	def __init__(self,state=0,time_open = 1):
		self.state = state #open/close
		self.time_open = time_open #the time the door remains open after a successful login
	#open: open the door
	def open(self):
		GPIO.output(25,1)
		time.sleep(self.time_open)
		GPIO.output(25,0)
	#close: close the door
	def close(self):
		GPIO.output(25,0)

#Object Instances
tarjeta1 =  tarjeta("",32)
puerta1  =  puerta(0,TIME_OPEN)


#Attaching card reader pins to the card object
GPIO.add_event_detect(23,GPIO.FALLING, callback=tarjeta1.function0)
GPIO.add_event_detect(24,GPIO.FALLING, callback=tarjeta1.function1)



#main loop
while True:
	#Close the door by default
	puerta1.close()
	#wait for a card number
	while len(tarjeta1.id_number) < tarjeta1.id_number_length:
		time.sleep(0.1)

	#Check if card is not already in the databse
    if(card.db_exist() == 0):
       card.db_add() 

GPIO.cleanup()
	
	

cars = (
    (1, '',1,1),
    (
)

con = lite.connect('test.db')

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
