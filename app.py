from flask import Flask, render_template,request
import requests
from datetime import datetime
import re
import pandas as pd
from bs4 import BeautifulSoup
name = []
odds = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Python練習")

@app.route('/result', methods=["GET"])
def result_get():
    year = request.args.get("year","")
    corse = request.args.get("corse","")
    number = request.args.get("number","")
    day = request.args.get("day","")
    race = request.args.get("race","")
    url = 'https://db.netkeiba.com/race/'+ year + corse + number + day + race
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    t = datetime.now().strftime("%Y/%m/%d %H:%M")

    for i in soup.find_all(href=re.compile("/horse/")):
        name.append(i.string)

    for o in soup.find_all(class_="txt_r",nowrap="nowrap")[3::5]:
        odds.append(o.string)

    df = pd.DataFrame({"name":name,t:odds})

    return render_template('result.html', message = df)

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')
