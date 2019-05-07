from bottle import route, run, template, request, redirect
import sqlite3

@route("/")
def index():
    return "<h1>TestHTML</h1>"

#show item list
@route("/list")
def view_list():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("select id,name from itemtable order by id")
    item_list = []
    for row in c.fetchall():
        item_list.append({"id":row[0],"name":row[1]})
    conn.close()
    # item_list = [
    # {"id":1, "name": "りんご"},
    # {"id":2, "name": "ばなな"},
    # {"id":3, "name": "すいか"},
    # ]
    return template("list_tmpl", item_list=item_list)

@route("/add", method=["GET","POST"])
def add_item():
    if request.method =="POST":  #if POST
        item_name = request.POST.getunicode("item_name")  #get item name
        conn = sqlite3.connect("items.db")
        c = conn.cursor()
        new_id = c.execute("select max(id) + 1 from itemtable").fetchone()[0] #max index+1
        c.execute("insert into itemtable values(?,?)",(new_id, item_name))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return template("add_tmpl")

@route("/update", method=["GET","POST"])
def update_item():
    if request.method =="POST":
        new_id = request.POST.getunicode("item_id")
        new_name = request.POST.getunicode("item_name")
        conn = sqlite3.connect("items.db")
        c = conn.cursor()
        para = [new_name, int(new_id)]
        c.execute("update itemtable set name= ? where id= ?",para)
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return template("update_tmpl")

#/del/100 -> item_id = 100
#/del/one -> HTTPError 404
@route("/del/<item_id:int>")  #delete item <item_id=input data
def del_item(item_id):
    conn = sqlite3.connect("items.db")
    c = conn.cursor()
    c.execute("delete from itemtable where id=?",(item_id,))
    conn.commit()
    conn.close
    return redirect("/list")

run(host="localhost", reloader=True, port=8000)
