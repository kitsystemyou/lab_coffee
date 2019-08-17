import sqlite3

conn = sqlite3.connect('members.db')
c = conn.cursor()

c.execute("select id,name,money,lucky from members order by id")
item_list = []
for row in c.fetchall():
    print({"id":row[0],"name":row[1],"money":row[2],"lucky":row[3]})
conn.close()
