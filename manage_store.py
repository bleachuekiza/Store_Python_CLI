import sqlite3
import time
# Module
import setupstore
import addstore
# Module

def menu():

    n = 1
    time.sleep(1)

    while n > 0:
        print('What do you want?')
        print('[1]Create Database')
        print('[2]Add Item')
        print('[3]Check Item List')
        print('[4]Exit')

        want = int(input())

        if want == 1:
            setupstore.createdb()
        if want == 2:
            addstore.item()
        if want == 3:
            time.sleep(0.2)
            conn = sqlite3.connect('database_store.db')
            cursor = conn.execute("SELECT ID,NAME,PRICE  from store")
            for row in cursor:
                print("ID = ", row[0])
                print("NAME = ", row[1])
                print("PRICE = ", row[2])
            time.sleep(5)
        if want == 4:
            time.sleep(0.2)
            n = -1
            print('Exit Program')