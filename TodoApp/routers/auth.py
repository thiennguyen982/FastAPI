from datetime import timedelta, datetime
from models.Auth import CreateUserRequest, Token
from models.models import Users
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from utilities import utils
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from os import environ as env
from utilities import create_logger

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

SECRET_KEY = env.get("SECRET_KEY")
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

db_dependency = utils.db_dependency

auth_logger = create_logger("auth_logger","logging/auth.log", "INFO")

def authenticate_user(username : str, password : str, 
                      db : db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    
    if not user:
        return False
    
    if not bcrypt_context.verify(password, user.hased_password):
        return False
    
    return user

def username_exists_in_database(username : str,
                             db : db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    
    if not user:
        return False
    
    return True

def create_access_token(user_id : int, username : str, first_name : str, last_name : str, role : str,
                        expired_date : timedelta):
    encode = {
        "User_Id": user_id,
        "Username": username,
        "First Name": first_name,
        "Last Name": last_name,
        "Role": role
    }
    expires = datetime.utcnow() + expired_date
    encode.update({"Expired": str(expires)})
    return jwt.encode(encode, SECRET_KEY, ALGORITHM)

async def get_current_user(token : Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username : str = payload.get("Username")
        user_id : int = payload.get("User_Id")
        user_role : str = payload.get("Role")
        first_name : str = payload.get("First Name")
        last_name : str = payload.get("Last Name")
        
        if username is None or user_id is None:
            msg = "Failed Validation Current Request From Users"
            auth_logger.info(f"Failed Valiation - {msg}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=msg
            )
            
        return {
            "Username": username,
            "User_Id": user_id,
            "User_Role": user_role,
            "First_Name": first_name,
            "Last_Name": last_name
        }
    except JWTError as e:
        auth_logger.info(f"JWT Error - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Couldn't Validate"
        )
        
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db : db_dependency, 
                      create_user_request : CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hased_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    
    if not username_exists_in_database(username=create_user_model.username,
                                       db=db):
        db.add(create_user_model)
        db.commit()
        auth_logger.info(f"User Created - {create_user_request.username}")
        
    else:
        msg = "Username already existed in the database!"
        auth_logger.info(f"User Created Process Failed In Operation: {create_user_request.username} - Message: {msg}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    
@router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db : db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    auth_logger.info(f"User Login - {form_data.username}")
    
    if not user:
        auth_logger.info(f"User Login Failed In Authentication - {form_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed Validation"
        )
        
    token = create_access_token(user.id, user.username, user.first_name, user.last_name, user.role, timedelta(minutes=20))
    auth_logger.info(f"Login Success - {form_data.username}")
    
    return {
        "access_token": token,
        "token_type": "Bearer"
    }