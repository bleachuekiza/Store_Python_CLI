import sqlite3
import time

def stock():
    time.sleep(0.2)
    conn = sqlite3.connect('database_store.db')
    cursor = conn.execute("SELECT ID,NAME,STOCK  from store")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("STOCK = ", row[2])
    time.sleep(2)
    uuid = int(input('ID :'))
    uustock = int(input('Stock :'))
    def search_id(uuid):
        conn = sqlite3.connect('database_store.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM store WHERE ID=?", (uuid,))

        rows = cur.fetchall()

        for row in rows:
            scid = row
            uid = scid[0]
            ustock = scid[4]+uustock
            def updateVaribleIntoTable(USTOCK, UID):
                try:
                    sqliteConnection = sqlite3.connect('database_store.db')
                    cursor = sqliteConnection.cursor()
                    print("Connected to SQLite")

                    sql_update_query = """Update store set STOCK = ? where ID = ?"""
                    data = (ustock, uid)
                    cursor.execute(sql_update_query, data)
                    sqliteConnection.commit()
                    print('UPDATE STOCK')
                    print('ID :',uid)
                    print('Stock :',ustock)
                    print("Record Updated successfully")
                    cursor.close()

                except sqlite3.Error as error:
                    print("Failed to update sqlite table", error)
                finally:
                    if (sqliteConnection):
                        sqliteConnection.close()
                        print("The sqlite connection is closed")
            updateVaribleIntoTable(ustock, uid)
    search_id(uuid)
stock()