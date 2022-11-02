from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    import requests
    return "Hello, World!"
