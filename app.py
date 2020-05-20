from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('Power.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/login',methods = ['post','get'])
def login():
    get_WD = float(request.form['Wind_Direction'])
    get_WS = float(request.form['Wind_Speed'])
    get_AP = float(request.form['Active_Power'])
    
    final_data = [[get_WD,get_WS,get_AP]]
    y_pred = model.predict(np.array(final_data))
    result = str(y_pred[0][0])
    return render_template("index.html",show = str(result)+" KWh")


if __name__== '__main__':
    app.run(debug = True)