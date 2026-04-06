from pydantic import BaseModel

class LocalBook(BaseModel):
    id:int
    name:str
    author:str
    year:int
    