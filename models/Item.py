from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    id: Union[int, None] = None
    title: str
    link: str
    description: str
    bloggername: str
    bloggerlink: str
    postdate: str
    text: Union[str, None] = None
    fullText: str
    ad: Union[int, None] = None
    probability: Union[float, None] = None