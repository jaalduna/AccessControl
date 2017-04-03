import sqlite3 as lite
import sys
import texttable as tt
from time import gmtime, strftime

#LOG_CARD_NOT_FOUND = 1
#LOG_CARD_NOT_ASSIGNED = 2
#LOG_USER_DISABLED = 3
#LOG_ACCESS_SUCCED = 4
#LOG_APERTURA_MANUAL = 5


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

    def create_log_table(self):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Log")
            cur.execute("CREATE TABLE log(Id Integer PRIMARY KEY, LogId, Date TEXT, Details TEXT)")


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
        user_name = raw_input('Nombre: ')
        user_second = raw_input('Apellido: ')
        rut = raw_input ('rut: ')
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
                

    def link_user2card(self,card_id,user_id):
        #Check if the card exist
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Cards WHERE Id=:Id",{"Id":card_id})
            row = cur.fetchone()
            if (row == None):
                print "El numero de tarjeta no existe"
            else:
                print "tarjeta encontrada"
                #Check if the User exist
                cur.execute("SELECT * from Users WHERE Id=:Id",{"Id":user_id})
                row = cur.fetchone()
                if (row == None):
                    print "El Usuario no existe"
                else:
                    print "Usuario encontrado"
                cur.execute("UPDATE Cards SET idUsuario=?  WHERE Id=?",(user_id,card_id))
                cur.execute("UPDATE Cards SET Usada=?  WHERE Id=?",(1,card_id))
                con.commit()
                print "Number of row updated: %d" % cur.rowcount
    def user_enable(self,user_id):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Users SET Habilitado=1 WHERE Id=:Id",{"Id":user_id})
            con.commit()
            print "Number of row updated: %d" % cur.rowcount
#    def disable_user(self,user_id):
    def user_disable(self,user_id):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("UPDATE Users SET Habilitado=0 WHERE Id=:Id",{"Id":user_id})
            con.commit()
            print "Number of row updated: %d" % cur.rowcount
    def show_card_table(self):
        con = lite.connect(self.db_name)
        tab = tt.Texttable() #texttable object
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Cards")
            col_names = [cn[0] for cn in cur.description]
            tab.header(col_names)
            rows = cur.fetchall()
            for row in rows:
                tab.add_row(row)  

            tab.set_cols_width([10,32,10,10])
            tab.set_cols_dtype(["t", "t","t","t"])
            print tab.draw() 

    def show_user_table(self):
        con = lite.connect(self.db_name)
        tab = tt.Texttable() #texttable object
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Users")
            col_names = [cn[0] for cn in cur.description]
            tab.header(col_names)
            rows = cur.fetchall()
            for row in rows:
                tab.add_row(row)  

            tab.set_cols_width([10,10,10,10,10])
            tab.set_cols_dtype(["t", "t","t","t","t"])
            print tab.draw() 

    def show_log_table(self):
        con = lite.connect(self.db_name)
        tab = tt.Texttable() #texttable object
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Log")
            col_names = [cn[0] for cn in cur.description]
            tab.header(col_names)
            rows = cur.fetchall()
            for row in rows:
                tab.add_row(row)  

            tab.set_cols_width([8,8,20,70])
            tab.set_cols_dtype(["t", "t","t","t"])
            print tab.draw() 


    def log(self,LogId,details):
        con = lite.connect(self.db_name)
        date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Log(Date,LogId,Details) VALUES (?,?,?)", ((date,LogId,details)))
            con.commit()
            print "Numero de registro: %d" %cur.lastrowid

    def validate_user(self,card_number):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Cards WHERE Number=:Number",{"Number":card_number})
            row = cur.fetchone()
            if(row == None):
                print "card not present in database"
                self.log(1, str("Card %s not present in database"% card_number))


                return 0
            else:
                if(row[3] == -1):
                    print "card not assigned"
                    return 0
                else:
                    user_id = row[3]
                    cur.execute("SELECT * FROM Users WHERE Id=:Id",{"Id":user_id})
                    row = cur.fetchone()
                    if(row == None):
                        print "User not found"
                        return 0
                    elif(row[4] == 0):
                        print "Access Denied"
                        return 0
                    else:
                        print "Access succeded"
                        return 1
                            

