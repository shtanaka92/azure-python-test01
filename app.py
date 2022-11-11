from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Python練習")

@app.route('/result.html', methods=["GET"])
def result_get():
    year = request.args.get("year","")
    corse = request.args.get("corse","")
    number = request.args.get("number","")
    day = request.args.get("day","")
    race = request.args.get("race","")
    url = 'https://race.netkeiba.com/race/shutuba.html?race_id='+ year + corse + number + day + race

    return render_template('result.html', message = url)

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')
