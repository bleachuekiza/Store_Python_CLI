import sqlite3
import time

def item():
    def insertVaribleIntoTable(BARCODE, NAME, PRICE):
        try:
            time.sleep(1)
            sqliteConnection = sqlite3.connect('database_store.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
                        
            time.sleep(0.2)
            sqlite_insert_with_param = """INSERT INTO store
                            (BARCODE, NAME, PRICE) 
                            VALUES (?, ?, ?);"""

            data_tuple = (BARCODE, NAME, PRICE)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Variables inserted successfully into store table")

            cursor.close()

        except sqlite3.Error as error:
            time.sleep(0.2)
            print("Failed to insert variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                time.sleep(0.2)
                sqliteConnection.close()
                print("The SQLite connection is closed")
    def check_name_dup(name):
        conn = sqlite3.connect('database_store.db')
        c = conn.cursor()
        c.execute('SELECT * FROM store WHERE NAME=?', (name,))

        if c.fetchone():
            print('Error : Barcode or Name Duplicate')
        else:
            insertVaribleIntoTable(barcode, name, price)
    def check_barcode_dup(barcode):
        conn = sqlite3.connect('database_store.db')
        c = conn.cursor()
        c.execute('SELECT * FROM store WHERE BARCODE=?', (barcode,))

        if c.fetchone():
            print('Error : Barcode or Name Duplicate')
        else:
            check_name_dup(name)
    time.sleep(0.2)
    barcode = int(input('Bar Code :'))
    name = input('Name :')
    price = int(input('Price :'))
    check_barcode_dup(barcode)