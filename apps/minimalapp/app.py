from cgitb import reset
from crypt import methods
from unicodedata import is_normalized
# import 文が長くなるため改行
from flask import (
    Flask,
    render_template,
    url_for,
    current_app,
    g,
    request,
    redirect,
    flash
)
from email_validator import validate_email, EmailNotValidError

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
        # form 属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]
        # 入力をチェック
        is_valid = True

        if not username:
            flash("ユーザーネームは必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る（後に実装）

        # 問い合わせ完了エンドポイントへリダイレクトする
        flash("お問い合わせありがとうございました。")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")

# SECRET_KEY を追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
