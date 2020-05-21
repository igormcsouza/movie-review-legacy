import pickle
from joblib import load
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Prepare models and prediction
def make_a_prediction(phrase):
    regressor = load('/models/sklearn-logistc-regressor-model.joblib')
    vectorizer = pickle.load(open("/models/vectorizer.pickle", "rb"))

    return 'Positivo' if regressor.predict(vectorizer.transform([phrase])) else 'Negativo'

data=dict()

@app.route('/')
def main(): 
    data['reviewresponse'] = 'yet'
    return render_template('index.html', data=data)

@app.route('/resolve', methods=['POST'])
def resolve():
    review = request.form.get('review')
    data['reviewresponse'] = make_a_prediction(review)
    return render_template('index.html', data=data)