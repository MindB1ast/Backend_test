

from fastapi import  FastAPI
from . import model
from . import database
 
from .routers import blog, users, login


app= FastAPI()

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(login.router)


model.Base.metadata.create_all(database.engine)








