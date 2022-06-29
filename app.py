from fastapi import FastAPI
from typing import List
from config import Config
from classifier import classify
from models.Item import Item
from preprocessor import preprocess

app = FastAPI()


@app.post("/predict")
async def classify_blog_text(item_list: List[Item]):
    """
        네이버 블로그 맛집 리뷰 텍스트의 광고 여부를 predict
    """
    # item_list = sorted(item_list, key=lambda item: item.id)
    lines_for_predict = []
    for item in item_list:
        lines_for_predict.append(preprocess(item.fullText))
    config = Config(model_fn="./trained_model/bert_clean.tok.slice.pth", gpu_id=-1, batch_size=8,
                    lines=lines_for_predict)
    classified_lines = classify(config)
    for i, classified_line in enumerate(classified_lines):
        item_list[i].probability = classified_line[0]
        item_list[i].ad = classified_line[1]
    return item_list
