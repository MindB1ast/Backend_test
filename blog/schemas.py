from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title:str
    body:str


class Blog(BlogBase):
    class Config:
        from_attributes=True


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    class Config:
        from_attributes=True
    name:str
    email:str
    blogs: List[Blog]

class ShowBlog(Blog):
    class Config:
        from_attributes=True
    creator: ShowUser

class Login(BaseModel):
    username: str
    password: str
    class Config:
        from_attributes=True
    

class Token(BaseModel):
    acces_token:str
    token_type:str

class TokenData(BaseModel):
    username: Optional[str] = None