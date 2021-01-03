import sqlite3
import time

time.sleep(0.2)
conn = sqlite3.connect('database_store.db')
cursor = conn.execute("SELECT ID,NAME,STOCK  from store")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("STOCK = ", row[2])
time.sleep(2)
uid = int(input('ID :'))
ustock = int(input('Stock :'))
def updateVaribleIntoTable(USTOCK, UID):
    try:
        sqliteConnection = sqlite3.connect('database_store.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update store set STOCK = ? where ID = ?"""
        data = (ustock, uid)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The sqlite connection is closed")
updateVaribleIntoTable(ustock, uid)