from flask import Flask
app = Flask(__name__)
import requests
from datetime import datetime
import re
import pandas as pd
from bs4 import BeautifulSoup


@app.route("/")
def hello():
    return "Hello, World!"
