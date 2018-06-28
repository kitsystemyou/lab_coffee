# -*- oding: cp932 -*-
# sqlite3はPython2.5から以降から標準であるはず.
import sqlite3
conn = sqlite3.connect('test.sqlite3')
sql = '''CREATE TABLE  IF NOT EXISTS  t01prefecture(
                         pref_cd INTEGER,
                         pref_name TEXT);'''
conn.execute(sql)

conn.execute(u"DELETE FROM t01prefecture")

#コミットの試験
pref_cd = 100
pref_name = u"カモメ"
conn.execute(u"""INSERT INTO t01prefecture(PREF_CD, PREF_NAME)
            VALUES (?, ?)""" , (pref_cd, pref_name))

pref_cd = 101
pref_name = u"ネコ"
conn.execute(u"""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
            VALUES (?, ?)""" , (pref_cd, pref_name,))
conn.commit()

pref_cd = 103
pref_name = u"ふぁあ"
conn.execute(u"""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
            VALUES (?, ?)""" , (pref_cd, pref_name,))
conn.commit()

# ロールバックの試験
pref_cd = 105
pref_name = u"back"
conn.execute(u"""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
            VALUES (?, ?)""" , (pref_cd, pref_name,))
conn.rollback()

rows = conn.execute(u'SELECT * FROM t01prefecture WHERE pref_cd > ?', (0,))
for row in rows:
    print(u"%d %s" % (row[0], row[1]))

# ユーザ定義
# 文字を連結するのみ
class UserDef:
    def __init__(self):
        self.values = []
    def step(self, value):
        self.values.append(value)
    def finalize(self):
        return "/".join(map(str, self.values))

conn.create_aggregate("userdef", 1, UserDef)
rows = conn.execute(u'SELECT userdef(PREF_NAME) FROM t01prefecture')
for row in rows:
    print(u"%s" % (row[0]))

conn.close()
