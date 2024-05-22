from pydantic import BaseModel, Field
from typing import Optional

class Book:
    id : int
    title : str
    author : str
    description : str
    rating : str
    published_date : int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id : Optional[int] = None
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str = Field(min_length=1, max_length=250)
    rating : int = Field(gt = 0, lt = 6)
    published_date :int = Field(gt = 0, lt=3000)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "New Book",
                "author": "Coding ThrowBy",
                "description": "New Description",
                "rating": 5,
                "published_date": 2012 
            }
        }