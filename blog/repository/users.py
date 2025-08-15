from sqlalchemy.orm import Session
from blog import model, schemas, hashing 
from fastapi import HTTPException, status


def create(request:schemas.User, db:Session):
    new_user= model.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    

def get(id:int, db:Session):
    user= db.query( model.User).filter(model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no user with id {id}")
    return user