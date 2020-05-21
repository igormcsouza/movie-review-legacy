from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)

# Prepare models and prediction
def make_a_prediction(phrase):
    regressor = load('/models/sklearn-logistc-regressor-model.joblib')
    return 'Positive' if regressor.predict(vectorizer.transform([phrase])) else 'Negative'

data=dict()

@app.route('/')
def main():
    data['reviewresponse'] = 'yet'
    return render_template('index.html', data=data)

@app.route('/resolve', methods=['POST'])
def resolve():
    review = request.form.get('review')
    data['reviewresponse'] = 'Positive'
    return render_template('index.html', data=data)