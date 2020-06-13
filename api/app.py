import pickle
from joblib import load
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Prepare models and prediction
def make_a_prediction(phrase):
    regressor = load('/models/sklearn-logistc-regressor-model.joblib')
    vectorizer = pickle.load(open("/models/vectorizer.pickle", "rb"))

    return 'pos' if regressor.predict(vectorizer.transform([phrase]))[0] else 'neg'

data=dict(reviewresponse='', review='', truth='', movie_banner_path=1)

movie_banner_list = [
    'static/img/1.png',
    'static/img/2.png',
    'static/img/3.png',
    'static/img/4.png',
    'static/img/5.png',
    'static/img/6.png',
    'static/img/7.png',
    'static/img/8.png',
    'static/img/9.png',
    'static/img/10.png',
]

@app.route('/')
def main(): 
    data['reviewresponse'] = 'yet'
    data['truth'] = 'yet'
    data['movie_banner_path'] = random.choice(movie_banner_list)
    return render_template('index.html', data=data)

@app.route('/resolve', methods=['POST'])
def resolve():
    data['review'] = request.form.get('review')
    data['reviewresponse'] = make_a_prediction(data['review'])

    return render_template('index.html', data=data)

@app.route('/store', methods=['POST'])
def store():
    data['truth'] = request.form.get('truth')

    with open('newbase.csv', 'a+') as f:
        f.writelines("{},{},{}\n".format(
            '"'+ data['review'] + '"', data['reviewresponse'], data['truth']
        ))
    
    return render_template('index.html', data=data)