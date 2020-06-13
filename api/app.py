from flask import Flask, request, jsonify, render_template, redirect
from flask_pymongo import PyMongo

from joblib import load
import pickle
import random
import os

app = Flask(__name__)

mongo = PyMongo(
    app,
    "mongodb+srv://igorsouza:{}@myapps-z1d9g.mongodb.net/movie-review?retryWrites=true&w=majority".format(os.getenv('MONGO_PASSWORD', '1234'))
)

movie_review_collection = mongo.db.movie_review

# Prepare models and prediction


def make_a_prediction(phrase):
    regressor = load('/models/sklearn-logistc-regressor-model.joblib')
    vectorizer = pickle.load(open("/models/vectorizer.pickle", "rb"))

    return 'pos' if regressor.predict(vectorizer.transform([phrase]))[0] else 'neg'


data = dict(reviewresponse='', review='', truth='', movie_banner_path=1)

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

    try:
        movie_review_collection.insert(data)
    except Exception as e:
        print('[ERROR]', e)
        return redirect('/')

    return render_template('index.html', data=data)
