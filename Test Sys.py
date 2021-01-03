barcode = int(input('Bar Code :'))
name = input('Name :')
price = int(input('Price :'))
stock = int(input('Stock :'))
def insertVaribleIntoTable(ID, BARCODE, NAME, PRICE, STOCK):
    try:
        sqliteConnection = sqlite3.connect('database_store.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        sqlite_insert_with_param = """INSERT INTO store
                          (ID, BARCODE, NAME, PRICE, STOCK) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (ID, BARCODE, NAME, PRICE, STOCK)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Variables inserted successfully into store table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable(1, barcode, name, price, stock)