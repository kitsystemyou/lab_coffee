from bottle import route, run, template, request, redirect, static_file
import sqlite3
import os

@route("/")
def index():
    return "<h1>TestHTML</h1>"

#load css files
@route("/<filename:path>")
def static(filename):
    return static_file(filename, root="./")

#show item list
@route("/list")
def view_list():
    conn = sqlite3.connect('members.db')
    c = conn.cursor()
    c.execute("select id,name,money,lucky from members order by id")
    member_list = []
    member_list.append({"id":"id", "name":"名前","money":"残額","lucky":"未実装"})
    for row in c.fetchall():
        member_list.append({"id":row[0],"name":row[1],"money":row[2],"lucky":row[3]})
    conn.close()

    return template("list_tmpl", item_list=member_list)

@route("/add", method=["GET","POST"])
def add_item():
    if request.method =="POST": 
        member_name = request.POST.getunicode("item_name")  #get item name
        conn = sqlite3.connect("members.db")
        c = conn.cursor()
        new_id = c.execute("select max(id) + 1 from members").fetchone()[0] #max index+1
        c.execute("insert into members values(?,?,?,?)",(new_id, member_name,0,0))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return template("add_tmpl")

@route("/update", method=["GET","POST"])
def update_item():
    if request.method =="POST":
        new_id = request.POST.getunicode("item_id")
        new_money = request.POST.getunicode("item_money")
        conn = sqlite3.connect("members.db")
        c = conn.cursor()
        #para = [new_money, int(new_id)]
        print(new_id, new_money)
        print(type(new_money))
        c.execute("update members set money=money+? where id= ?",(new_money,int(new_id),))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return template("update_tmpl")

@route("/charge/<charger_id:int>", method=["GET", "POST"])
def drink_calc(charger_id):
    if request.method =="POST":
        update_id = request.POST.getunicode("id")
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return template("drink", id = charger_id)

#example
#/del/100 -> item_id = 100
#/del/one -> HTTPError 404
@route("/del/<item_id:int>")  #delete item <item_id=input data
def del_item(item_id):
    conn = sqlite3.connect("members.db")
    c = conn.cursor()
    c.execute("delete from members where id=?",(item_id,))
    conn.commit()
    conn.close
    return redirect("/list")

# user view
# not yet
@route("/member_page")
def view_member_list():
    conn = sqlite3.connect('members.db')
    c = conn.cursor()
    c.execute("select id,name,money,lucky from members order by id")
    member_list = []
    member_list.append({"id":"id", "name":"名前","money":"残額","lucky":"未実装"})
    for row in c.fetchall():
        member_list.append({"id":row[0],"name":row[1],"money":row[2],"lucky":row[3]})
    conn.close()

    return template("member_page", item_list=member_list)


run(host="localhost", reloader=True, port=8000)
# run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
