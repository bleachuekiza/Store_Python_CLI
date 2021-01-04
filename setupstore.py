import sqlite3
import time
def createdb():
       conn = sqlite3.connect('database_store.db')
       print("Connected to SQLite")

       time.sleep(2)
       # Create Table SQLite
       conn.execute('''CREATE TABLE store
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              BARCODE     INTEGER        NOT NULL,
              NAME        TEXT        NOT NULL,
              PRICE       INTEGER     NOT NULL);''')
       print('Create Table store Successfully')
       conn.close()