from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    return "Hello, World!"
