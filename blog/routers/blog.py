from fastapi import APIRouter,  status, HTTPException
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from blog import schemas, model, database
from blog.repository import blog
from blog.database import get_db
from blog.oauth2 import get_current_user


router= APIRouter( prefix="/blog", tags=["blog"])



@router.get("/", response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db), get_current_user: schemas.User= Depends(get_current_user) ):
    return blog.get_blogs(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db:Session= Depends(database.get_db), get_current_user: schemas.User= Depends(get_current_user)):
    return blog.create(request, db)



@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= schemas.ShowBlog)
def get(id:int, db:Session=Depends(get_db), get_current_user: schemas.User= Depends(get_current_user)):
    return blog.get_by_index(id, db)
        
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,  db:Session=Depends(database.get_db), get_current_user: schemas.User= Depends(get_current_user)):
    return blog.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request: schemas.Blog, db:Session=Depends(get_db), get_current_user: schemas.User= Depends(get_current_user)):
    return blog.update(id, request, db)