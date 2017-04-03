# -*- coding: utf-8 -*-
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

menu = 0; #menu inde

while menu !=4:
    #display menu options
    print "****** Menu *****"
    print "1. Configuration"
    print "2. Logs"
    print "3. Run"
    print "4. Exit"
    print ""
    menu = input("Choose an option: ")
     
    if(menu == 4):
        print "cerrando programa"
    elif (menu == 3):
        while True:
            #Close the door by default
            puerta1.close()
            #wait for a card number
            print "esperando tarjeta ..."
            tarjeta1.get_code()
            
            #Validate user
            if(database1.validate_user(tarjeta1.id_number)):
                puerta1.open()  
                #log valid user entry
            #else:
                #log invalid user entry
                    
            #Clear card information
            tarjeta1.id_number = ""
        GPIO.cleanup()
    elif (menu == 2):
        print "submenu 2"
        print "1. show Cards Table"
        print "2. show Users Table"
        print "3. show Event Logs"
        print ""
        menu3 = input("Choose an option: ")
        if(menu3 == 1): #show Card Table
            database1.show_card_table()
        elif (menu3 ==  2): #show Users Table
            database1.show_user_table()
        elif (menu3 == 3):
            print "showing log event..."
        else:
            print "Numero desconocido"

    elif (menu == 1):
        print "submenu 1"
        print "**** Configuración ****"
        print "1. Create Database"
        print "2. Add User"
        print "3. Add Card"
        print "4. Enable/Disable User"
        print "5. Link User to Card"
        print ""
        menu2 = input("Choose an option: ")
        if( menu2 == 1):
            res = input("data will be erased, are u shure to proceed?:(0/1) ")
            if(res == 1):
                database1.create_card_table()
                database1.create_users_table()
        elif (menu2 == 2):
            database1.add_user()
        elif (menu2 == 3):
            tarjeta1.get_code()
            database1.add_card(tarjeta1.id_number)
        elif (menu2 == 4):
            enable = input("enable/disable?: (0/1)")
            user_id = input("user_id: ")
            if(enable == 1):
                database1.user_enable(user_id) 
            else:
                database1.user_disable(user_id)
        elif (menu2 == 5):
            card_id = input("card id: ")
            user_id = input("user id: ")
            database1.link_user2card(card_id, user_id)
        else:
            print "Numero desconocido"

    else:
        print "Numero desconocido"
     
#        #lets initialize database
#        database1.create_card_table()
#        database1.create_users_table()
#
#        #lets add some users
#        database1.add_user()
#
#        #main loop
#        while True:
#            #Close the door by default
#            puerta1.close()
#            #wait for a card number
#            tarjeta1.get_code()
#
#            #Validate user
#            database1.add_card(tarjeta1.id_number)
#            print tarjeta1.validar()
#            #If user is validated then open the door
#            if(tarjeta1.validar()):
#                puerta1.open()  
#                #log valid user entry
#            #else:
#                #log invalid user entry
#                    
#            
#            #Clear card information
#            tarjeta1.id_number = ""
#        GPIO.cleanup()
            
            

