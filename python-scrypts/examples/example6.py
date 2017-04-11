import sqlite3 as lite
import sys

con = lite.connect('test.db')

uId = 1
uPrice = 62300

with con:
    
    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?",(uPrice,uId))
    con.commit()

    print "Number or fows updated: %d" % cur.rowcount
