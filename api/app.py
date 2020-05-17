from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Prepare models and prediction
def make_a_prediction(phrase):
    return 'Positive' if regressor.predict(vectorizer.transform([phrase])) else 'Negative'

@app.route('/')
def main():
    return render_template('index.html')