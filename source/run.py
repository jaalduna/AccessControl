#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO #gpio libarry for raspberry pi import time #for make delays
import time
import os 
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
database1 = database("/var/www/webapp/database.db")


#Attaching card reader pins to the card object tarjeta1
GPIO.add_event_detect(CARD_READER_DATA0,GPIO.FALLING, callback=tarjeta1.function0)
GPIO.add_event_detect(CARD_READER_DATA1,GPIO.FALLING, callback=tarjeta1.function1)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=lambda x: apertura_manual(),bouncetime =TIME_OPEN*1000+1000)

def apertura_manual():
    database1.log(5,"Apertura Manual")
    puerta1.open()
        


menu = 0; #menu inde

while menu !=4:
    #display menu option
#    res = os.system('clear') 
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
        print "     ***** Logs *****"

        print "1. show Cards Table"
        print "2. show Users Table"
        print "3. show Event Logs"
        print "4. Back to main menu"
        print ""
        menu3 = input("Choose an option: ")
        if(menu3 == 1): #show Card Table
            database1.show_card_table()
            res =  raw_input("continue...")
        elif (menu3 ==  2): #show Users Table
            database1.show_user_table()
            res = raw_input("continue...")
        elif (menu3 == 3):
            database1.show_log_table()
            res = raw_input("continue...")
        elif (menu3 == 4):
            print "Going back to main menu"
        else:
            print "Numero desconocido"

    elif (menu == 1):
        print ""
        print "**** Configuración ****"
        print "1. Create Database"
        print "2. Add User"
        print "3. Add Card"
        print "4. Enable/Disable User"
        print "5. Link User to Card"
        print "6. Back to main manu"
        print ""
        menu2 = input("Choose an option: ")
        if( menu2 == 1):
            res = input("data will be erased, are u shure to proceed?:(0/1) ")
            if(res == 1):
                print "Create Database"
                print "1. Create card table"
                print "2. Create Users table"
                print "3. Create Log table"
                print "4. Back to main menu"
                menu4 = input("Choose an option: ")
                if(menu4 == 1):
                    database1.create_card_table()
                    res =  raw_input("continue...")
                elif(menu4 == 2):
                    database1.create_users_table()
                    res =  raw_input("continue...")
                elif(menu4 == 3):
                    database1.create_log_table() 
                    res =  raw_input("continue...")
                else:
                    print "Going back to main menu" 

        elif (menu2 == 2):
            database1.add_user()
            res =  raw_input("continue...")
        elif (menu2 == 3):
            print "presentar tarjeta..."
            tarjeta1.get_code()
            print "codigo obtenido ... "
            database1.add_card(tarjeta1.id_number)
            res =  raw_input("continue...")
        elif (menu2 == 4):
            enable = input("enable/disable?: (0/1)")
            user_id = input("user_id: ")
            if(enable == 1):
                database1.user_enable(user_id) 
                res =  raw_input("continue...")
            else:
                database1.user_disable(user_id)
                res =  raw_input("continue...")
        elif (menu2 == 5):
            card_id = input("card id: ")
            user_id = input("user id: ")
            database1.link_user2card(card_id, user_id)
            res =  raw_input("continue...")
        elif (menu2 == 6):
            print "going back to main menu"
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
            
            

