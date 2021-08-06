from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


cv = pickle.load('cv_vec_02082021.pkl')
model = pickle.load('final_model_02082021.pkl')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        message= request.form['message']
        data=[message]
        vect= cv.transform(data).toarray()
        my_prediction= model.predict(vect)
    return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
