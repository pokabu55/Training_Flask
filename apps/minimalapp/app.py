from crypt import methods
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flaskbook!"

@app.route("/hello",  # Rule
    methods=["Get"],  # Methods
    endpoint="hello-endpoint") # Endpoint
def hello():
    return "hello, world!!"

# Flask2 から @app.route(methods=["Get"]) を下記のように書けるようになった
@app.get("/flask2")
@app.post("/flask2")
def hello():
    return "flask2 specification"
