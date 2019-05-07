from bottle import route, run, get, post, request

# routeデコレーター
# これを使用してURLのPathと関数をマッピングする。
@route('/hello')
def hello():
  return "Hello World!!"

# @route('/resource', method='POST')と同じ意味
@post('/resource')
"""def post_resource():
    print("aaa")
    return ""
"""

# ビルトインの開発用サーバーの起動
# ここでは、debugとreloaderを有効にしている
run(host='localhost', port=8080, debug=True, reloader=True)
#http://localhost:8080/hello に繋ぐとHello World!
