from typing import List
import pydantic as _pydantic
import datetime as _dt

class _PostBase(_pydantic.BaseModel):
    title : str
    content: str

class PostCreate(_PostBase):
    pass 

class Post(_PostBase):
    id  : int
    owner_id : _dt.datetime
    date_last_updated : _dt.datetime

    class Config:
        orm_mode = True


class _UserBase(_pydantic.BaseModel):
    email:str

class UserCreate(_UserBase):
    password : str

class User(_UserBase):
    id : int
    is_active:bool
    posts : list[Post] = []

    