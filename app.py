from flask import Flask
app = Flask(__name__)
import requests
from datetime import datetime
import re
import pandas as pd
from bs4 import BeautifulSoup


@app.route("/")
def hello():
r = requests.get('https://db.netkeiba.com/race/202004030801/')
soup = BeautifulSoup(r.content,"html.parser")

name = []
odds = []

t = datetime.now().strftime("%Y/%m/%d %H:%M")
for i in soup.find_all(href=re.compile("/horse/")):
    name.append(i.string)

for o in soup.find_all(class_="txt_r",nowrap="nowrap")[3::5]:
    odds.append(o.string)


df = pd.DataFrame({"name":name,t:odds})

print(df)
    return "Hello, World!"
