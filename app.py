from flask import Flask, render_template,request
import requests
from datetime import datetime
import re
import pandas as pd
from bs4 import BeautifulSoup
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary
name = []
odds = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Python練習1")

@app.route('/result', methods=["GET"])
def result_get():
    year = request.args.get("year","")
    corse = request.args.get("corse","")
    number = request.args.get("number","")
    day = request.args.get("day","")
    race = request.args.get("race","")
    url = 'https://db.netkeiba.com/race/'+ year + corse + number + day + race
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    found = soup.select('td')

    return render_template('result.html', message = found)

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')
