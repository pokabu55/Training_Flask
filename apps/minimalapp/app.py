from crypt import methods
from flask import Flask, render_template

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

# Flask2 から @app.route(methods=["Get","Post"]) を下記のように書けるようになった
@app.get("/flask2")
@app.post("/flask2")
def hello():
    return "flask2 specification"
