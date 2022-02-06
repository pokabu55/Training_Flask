from cgitb import reset
from crypt import methods
from flask import Flask, render_template, url_for, current_app, g, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flaskbook!"

@app.route("/hello/<name>",  # Rule
    methods=["Get","Post"],  # Methods
    endpoint="hello-endpoint") # Endpoint
def hello(name):
    # f-string による書き方
    return f"Hello, {name}!"

# show_name エンドポイントの作成
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートに渡す
    return render_template("index.html", name=name)

# url_for 関数でurlを出力してみる
with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=ichiro
    print(url_for("show_name", name="ichiro", page="1"))

# Flask2 から @app.route(methods=["Get","Post"]) を下記のように書けるようになった
@app.get("/flask2")
@app.post("/flask2")
def hello():
    return "flask2 specification"

# この呼び方はエラー
# print(current_app)

# アプリケーションコンテキストを取得してスタックへプッシュ
ctx = app.app_context()
ctx.push()

# current_app にアクセス可能になる
print(current_app.name)

# グローバルなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=true"):
    # true が出力される
    print(request.args.get("updated"))

# 1.3章 問い合わせフォームを作成する
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # メールを送る（後に実装）

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
