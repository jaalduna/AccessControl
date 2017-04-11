import sqlite3 as lite
import sys

con = lite.connect('test.db')

uId = 4


with con:
    
    cur = con.cursor()

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", {"Id": uId})
    con.commit()

    row = cur.fetchone()
    print row[0], row[1]
    print "Number or fows updated: %d" % cur.rowcount
