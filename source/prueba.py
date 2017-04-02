import RPi.GPIO as GPIO #gpio libarry for raspberry pi import time #for make delays
import time
#Parameters
TIME_OPEN = 1 # time (seconds) the door remains open after a succesfull login
PUERTA1_PORT = 25 #port pin
CARD_READER_DATA0 = 23 #Card reader DATA0 port
CARD_READER_DATA1 = 24 #Card reader DATA1 port


#GPIO configurations#
GPIO.setmode(GPIO.BCM) #use the physical nomenclature
GPIO.setup(CARD_READER_DATA0,GPIO.IN, pull_up_down = GPIO.PUD_UP) #DATA0 card reader weingand Interface
GPIO.setup(CARD_READER_DATA1,GPIO.IN, pull_up_down = GPIO.PUD_UP) #DATA1 card reader weingand Interface
GPIO.setup(PUERTA1_PORT,GPIO.OUT) # door actuator output
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

#lets initialize database
database1.create_card_table()
database1.create_users_table()

#lets add some users
database1.add_user()
database1.add_user()

#main loop
while True:
    #Close the door by default
    puerta1.close()
    #wait for a card number
    while len(tarjeta1.id_number) < tarjeta1.id_number_length:
        time.sleep(0.1)

    #Validate user
    database1.add_card(tarjeta1.id_number)
    print tarjeta1.validar()

    #If user is validated then open the door
    if(tarjeta1.validar()):
        puerta1.open()  
        #log valid user entry
    #else:
        #log invalid user entry
            
    
    #Clear card information
    tarjeta1.id_number = ""
GPIO.cleanup()
    
    

