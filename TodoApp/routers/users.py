from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from models.Users import ChangePasswordRequest
from models.models import Users
from routers.auth import get_current_user
from utilities import utils
from starlette import status
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

db_dependency = utils.db_dependency
user_dependency = Annotated[dict, Depends(get_current_user)]

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user : user_dependency):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authenticated"
        )
    return user

@router.put("/change-password", status_code=status.HTTP_202_ACCEPTED)
async def change_password(user : user_dependency, db : db_dependency,
                          changeRequest : ChangePasswordRequest):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authenticated"
        )
    
    user_model = db.query(Users).filter(Users.id == user.get("User_Id")).first()
    
    if not bcrypt_context.verify(changeRequest.old_password, user_model.hased_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong CurrentPassword"
        )
        
    user_model.hased_password = bcrypt_context.hash(changeRequest.new_password)
    db.add(user_model)
    db.commit()