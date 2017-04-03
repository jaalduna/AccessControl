#card object
import time
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

    def get_code(self):
        while len(self.id_number) < self.id_number_length:
            time.sleep(0.1)


