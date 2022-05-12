from flask import Flask, jsonify, request

from config import Config
from classify import main
from preprocessor import preprocess

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    """블로그 텍스트를 받으면 분류 결과를 return"""
    if request.method == 'POST':
        data = request.get_json()
        lines = []
        for json in data:
            text = json['text']
            text = preprocess(text)
            lines.append(text)
        print(lines)
        config = Config("./models/bert_clean.tok.slice.pth", -1, 8, lines)
        result = main(config)
        result_list = []
        for i in range(len(lines)):
            r = result[i]
            tmp = {}
            tmp['id'] = data[i]['id']
            tmp['probability'] = r[0]
            tmp['ad'] = r[1]
            tmp['text'] = r[2]
            result_list.append(tmp)
        return jsonify(result_list)