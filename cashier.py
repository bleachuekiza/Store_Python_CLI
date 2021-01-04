import sqlite3

def calculate():
    item_list = []
    price_list = []
    print('Enter 0 for Calculate product prices!')
    nbc = int(input('Enter Barcode Number :'))
    def search_barcode(barcode_num):
        conn = sqlite3.connect('database_store.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM store WHERE BARCODE=?", (barcode_num,))

        rows = cur.fetchall()

        for row in rows:
            ubarcode = row
            name = ubarcode[2]
            price = ubarcode[3]
            item_list.append(name)
            price_list.append(price)

    while nbc > 0:
        search_barcode(nbc)
        nbc = int(input('Enter Barcode Number :'))

    a = len(item_list)
    iname = 'Item Name'
    iprice = 'Price'
    print('{iname:<9}    {iprice:>6}'.format(iname=iname,iprice=iprice))
    print('------------------------------')
    for i in range(a):
        print('{sitem:<9}    {sprice:>3}'.format(sitem=item_list[i-1],sprice=price_list[i-1]))
    print('------------------------------')
    print('Total:',sum(price_list))