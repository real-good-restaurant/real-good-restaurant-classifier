from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    """블로그 텍스트를 받으면 분류 결과를 return"""
    if request.method == 'POST':
        test_request = request.files()
    return "Hello World"
