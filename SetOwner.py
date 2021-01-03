import sqlite3
import time

n = 1
time.sleep(0.2)

while n > 0:

    checkowner = int(input('Code Check Owner :'))

    if checkowner == 18622089:
        usernameowner = input('Username Owner :')
        passowner = input('Password :')
        n = -1
    else:
        time.sleep(0.5)
        print('Code Wrong!!!')
        print('Contact me 0900410409')
        time.sleep(2)

def insertVaribleIntoTable(USERNAME, PASSWORD, PERMISSION):
    try:
        time.sleep(1)
        sqliteConnection = sqlite3.connect('database_store.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        time.sleep(0.2)
        sqlite_insert_with_param = """INSERT INTO user
                          (USERNAME, PASSWORD, PERMISSION) 
                          VALUES (?, ?, ?);"""

        data_tuple = (USERNAME, PASSWORD, PERMISSION)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Variables inserted successfully into user table")

        cursor.close()

    except sqlite3.Error as error:
        time.sleep(0.2)
        print("Failed to insert variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            time.sleep(0.2)
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable(usernameowner, passowner, 'Owner')