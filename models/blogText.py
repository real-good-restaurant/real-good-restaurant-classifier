from pydantic import BaseModel
from typing import Union


class BlogText(BaseModel):
    id: int
    text: str
    ad: Union[int, None] = None
    probability: Union[float, None] = None