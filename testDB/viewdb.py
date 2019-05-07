import sqlite3

conn = sqlite3.connect('items.db')
c = conn.cursor()

c.execute("select id,name from itemtable order by id")
item_list = []
for row in c.fetchall():
    print({"id":row[0],"name":row[1]})
conn.close()
