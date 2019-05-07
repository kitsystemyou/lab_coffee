import sqlite3

#connect database
conn = sqlite3.connect('items.db')
c = conn.cursor()

#make table
c.execute("create table itemtable(id,name)")

#add items
c.execute("insert into itemtable values(1,'りんご')")
c.execute("insert into itemtable values(2,'ばなな')")
c.execute("insert into itemtable values(3,'すいか')")

conn.commit()
conn.close
