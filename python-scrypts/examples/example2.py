import sqlite3 as lite
import sys

con = None

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()
    
    print "SLITE version: %s" % data

