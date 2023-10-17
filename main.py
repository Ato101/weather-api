from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temperature =50
    context = {
        station:station,
        date : date,
        'temperature': temperature
    }
    return context


if __name__=='main':
    app.run(debug=True,port=5001)