from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()


@app.get("/")
def page():
    return {"data": "blog list"}

@app.get("/blog")
def get_blog(limit:int=10, published:bool=True, sort:Optional[int]=None):
    return {"data": f"this is blog {limit} and {published}"}

@app.get("/blog/unpublished")
def get_unpublished():
    return {"unpublished blogs"}


@app.get("/blog/{id}")
def get_blog(id:int):
    return {"blog": id}




@app.get("/blog/{id}/comments")
def get_blog_commetns(id:int):
    return {"blog": f"comments {id}"}


class Blog(BaseModel):
    title:str
    body:str
    published_at: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": "blog created"}



#if __name__ == "__main__":
#    uvicorn.run(app, host="localhost", port=9000)