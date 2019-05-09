import sqlite3

#connect database
conn = sqlite3.connect('members.db')
c = conn.cursor()

#make table
c.execute("create table members(id,name,money,lucky)")

#add items
c.execute("insert into members values(1,'榎田',0,0)")
c.execute("insert into members values(2,'川端',0,0)")
c.execute("insert into members values(3,'倉重',0,0)")
c.execute("insert into members values(4,'山田',0,0)")

conn.commit()
conn.close
