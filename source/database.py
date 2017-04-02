import sqlite3 as lite
import sys

class  database(object):
    def __init__(self,db_name = "database.db"):
        self.db_name =db_name

    def create_card_table(self):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Cards")
            cur.execute("CREATE TABLE Cards(Id INTEGER PRIMARY KEY, Number TEXT, Usada INT, IdUsuario INT)") 

    def create_users_table(self):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Users")
            cur.execute("CREATE TABLE Users(Id INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT, Rut TEXT, Habilitado INT)") 

    def add_card(self,card_number):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            
            # Check if the number is already in the table
            cur.execute("SELECT * FROM Cards WHERE Number=:Number",{"Number":card_number})
            row = cur.fetchone()
            
            
            if (row != None): 
                print "Esta tarjeta ya esta registrada!, su Id es: %s" % row[0]
            else:
                print "registrando tarjeta"
                cur.execute("INSERT INTO Cards(Number,Usada,IdUsuario) VALUES (?,?,?)", ((card_number,0,-1)))
                con.commit()
                print "Numero de registro: %d" %cur.lastrowid

    def add_user(self):
        #get User Name
        print 'Sistema de registro de usuarios'
        print ''
        user_name = input('Nombre: ')
        user_second = input('Apellido: ')
        rut = input ('rut: ')
        user_enabled = 1 #new users are enables by default
            
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            
            #Check if there is not user with the same rut
            cur.execute("SELECT * FROM Users WHERE Rut=:Rut",{"Rut":rut})
            row = cur.fetchone()
            
            if (row != None):
                print 'El usuario ya existe, su Id es: %s' % row[0]
            else:
                print 'registrando Usuario'
                cur.execute("INSERT INTO Users(Nombre, Apellido, Rut, Habilitado) VALUES (?, ?, ?, ?)", ((user_name,user_second,rut,user_enabled))) 
                con.commit()
                print "numero de registro: %d" %cur.lastrowid
                

#    def link_user2card(self,card_id,user_id):
#    def enable_user(self,user_id):
#    def disable_user(self,user_id):

