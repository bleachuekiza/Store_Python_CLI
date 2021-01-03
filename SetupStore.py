import sqlite3
import time
def createdb():
       conn = sqlite3.connect('database_store.db')
       print("Connected to SQLite")

       time.sleep(2)
       # Create Table SQLite
       conn.execute('''CREATE TABLE user
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              USERNAME        TEXT    NOT NULL,
              PASSWORD        TEXT    NOT NULL,
              PERMISSION      TEXT    NOT NULL);''')
       print('Create Table user Successfully')
       time.sleep(2)
       conn.execute('''CREATE TABLE store
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              BARCODE     TEXT        NOT NULL,
              NAME        TEXT        NOT NULL,
              PRICE       INTEGER     NOT NULL,
              STOCK       INTEGER     NOT NULL);''')
       print('Create Table store Successfully')
       conn.close()