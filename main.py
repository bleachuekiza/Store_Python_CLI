import sqlite3
import time

n = 1

while n > 0:
    print('What do you want?')
    print('[1]Create Database')
    print('[2]SetOwner')
    print('[3]Store')
    print('[4]Exit')

    want = int(input())

    if want == 1:
        import SetupStore
    if want == 2:
        import SetOwner
    if want == 3:
        import Store
    if want == 4:
        time.sleep(0.2)
        n = -1
        print('Exit Program')