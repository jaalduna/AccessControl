#!/usr/bin/env python
# -*- coding: utf-8 -*-
#print "hola mundo"
import RPi.GPIO as GPIO #gpio libarry for raspberry pi import time #for make delays
import time
import os 
GPIO.setwarnings(False)
#Parameters
TIME_OPEN = 2 # time (seconds) the door remains open after a succesfull login
PUERTA1_PORT = 25 #port pin
CARD_READER_DATA0 = 23 #Card reader DATA0 port
CARD_READER_DATA1 = 24 #Card reader DATA1 port
BUTTON = 8 #Manual button

#GPIO configurations#
GPIO.setmode(GPIO.BCM) #use the physical nomenclature
GPIO.setup(CARD_READER_DATA0,GPIO.IN, pull_up_down = GPIO.PUD_UP) #DATA0 card reader weingand Interface
GPIO.setup(CARD_READER_DATA1,GPIO.IN, pull_up_down = GPIO.PUD_UP) #DATA1 card reader weingand Interface
GPIO.setup(PUERTA1_PORT,GPIO.OUT) # door actuator output
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Manual button input
####################

from tarjeta import tarjeta #import tarjeta class
from puerta import puerta#import door class
from database import database #import database class

#Create object Instances
tarjeta1 =  tarjeta("",32)
puerta1  =  puerta(0,TIME_OPEN,25)
database1 = database("database.db")


#Attaching card reader pins to the card object tarjeta1
GPIO.add_event_detect(CARD_READER_DATA0,GPIO.FALLING, callback=tarjeta1.function0)
GPIO.add_event_detect(CARD_READER_DATA1,GPIO.FALLING, callback=tarjeta1.function1)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=lambda x: apertura_manual(),bouncetime =TIME_OPEN*1000+1000)

def apertura_manual():
    database1.log(5,"Apertura Manual")
    puerta1.open()
        
text_file = open("Output.txt", "w")
text_file.write( tarjeta1.get_code())
text_file.close()

