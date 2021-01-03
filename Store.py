import sqlite3
import time

n = 1
time.sleep(1)
while n > 0:
    print('What do you want?')
    print('[1]Add Store')
    print('[2]Add Stock')
    print('[3]Check Stock')
    print('[4]Exit')

    want = int(input())

    if want == 1:
        import addstore
    if want == 2:
        import addstock    
    if want == 3:
        time.sleep(0.2)
        conn = sqlite3.connect('database_store.db')
        cursor = conn.execute("SELECT ID,NAME,STOCK  from store")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("STOCK = ", row[2])
        time.sleep(5)
    if want == 4:
        time.sleep(0.2)
        n = -1
        print('Exit Program')