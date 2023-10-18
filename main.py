from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    station =pd.read_csv('003 data-small/stations.txt',skiprows=17)
    station=station[['STAID','STANAME                                 ']][0:100]

    return render_template('home.html',context=station.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filename = '003 data-small/TG_STAID' + str(station).zfill(6)+'.txt'
    df = pd.read_csv(filename,skiprows =20,parse_dates=['    DATE'])
    temperature=df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    context = {
        station:station,
        'date': date,
        'temperature': temperature
    }
    return context

@app.route("/api/v1/yearly/<station>/<year>")
def get_all_year(station,year):
    filename = '003 data-small/TG_STAID' + str(station).zfill(6)+'.txt'
    df = pd.read_csv(filename,skiprows=20)
    df['    DATE'] =df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startwith(str(year))].to_dict()
    return result

@app.route("/api/v1/<station>/")
def get_statiom(station,year):
    filename = '003 data-small/TG_STAID' + str(station).zfill(6)+'.txt'
    df = pd.read_csv(filename,skiprows=20,parse_dates=['    DATE'])
    result= df.to_dict(orient='records')
    return result


if __name__=='__main__':
    app.run(debug=True,port=5000)