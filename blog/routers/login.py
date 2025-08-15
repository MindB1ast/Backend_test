from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import schemas, database, model, hashing
from blog.JWTtoken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


router= APIRouter(prefix="/login", tags=["login"])

@router.post("/")
def login( request:OAuth2PasswordRequestForm= Depends(), db: Session= Depends(database.get_db)):
    user=db.query(model.User).where(model.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user or password is incorect")
    
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user or password is incorect")

    #acces_token_expires= timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    acces_token = create_access_token( data={"sub": user.email})
    return {"access_token": acces_token, "token_type": "bearer"}