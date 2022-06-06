from fastapi import FastAPI
from typing import List
from config import Config
from classifier import classify
from models.blogText import BlogText
from preprocessor import preprocess

app = FastAPI()


@app.post("/predict")
async def classify_blog_text(blog_text_list: List[BlogText]):
    """
        네이버 블로그 맛집 리뷰 텍스트의 광고 여부를 predict
    """
    blog_text_list = sorted(blog_text_list, key=lambda blog_text: blog_text.id)
    lines_for_predict = []
    for blog_text in blog_text_list:
        lines_for_predict.append(preprocess(blog_text.text))
    config = Config(model_fn="./trained_model/bert_clean.tok.slice.pth", gpu_id=-1, batch_size=8,
                    lines=lines_for_predict)
    classified_lines = classify(config)
    classification_result = []
    for i, classified_line in enumerate(classified_lines):
        blog_text = BlogText(
            id=blog_text_list[i].id,
            text=classified_line[2]
        )
        blog_text.probability = classified_line[0]
        blog_text.ad = classified_line[1]
        classification_result.append(blog_text)
    return classification_result
