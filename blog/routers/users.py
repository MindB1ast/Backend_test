from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from blog import schemas, database
from blog.repository import users


router= APIRouter( prefix="/user", tags=["user"])


@router.post("/", response_model= schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(database.get_db)):
    return users.create(request, db)
    

@router.get("/{id}", response_model= schemas.ShowUser)
def get_user(id:int, db:Session=Depends(database.get_db)):
    return users.get(id, db)