import sqlite3
import time
# Module Store
import SetupStore
import SetOwner
import Store
# Module Store

n = 1

while n > 0:
    print('What do you want?')
    print('[1]Create Database')
    print('[2]SetOwner')
    print('[3]Store')
    print('[4]Exit')

    want = int(input())

    if want == 1:
        SetupStore.createdb()
    if want == 2:
        SetOwner.menu()
    if want == 3:
        Store.menu()
    if want == 4:
        time.sleep(0.2)
        n = -1
        print('Exit Program')