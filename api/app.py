import pickle
from joblib import load
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Prepare models and prediction
def make_a_prediction(phrase):
    regressor = load('/models/sklearn-logistc-regressor-model.joblib')
    vectorizer = pickle.load(open("/models/vectorizer.pickle", "rb"))

    return 'pos' if regressor.predict(vectorizer.transform([phrase])) else 'neg'

data=dict(reviewresponse='', review='', truth='')

@app.route('/')
def main(): 
    data['reviewresponse'] = 'yet'
    data['truth'] = 'yet'
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
            data['review'], data['reviewresponse'], data['truth']
        ))
    
    return render_template('index.html', data=data)