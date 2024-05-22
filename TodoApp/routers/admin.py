from fastapi import APIRouter, Depends, HTTPException, Path
from models.models import Todos
from .auth import get_current_user
from typing import Annotated
from utilities import utils
from starlette import status

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

db_dependency = utils.db_dependency
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user : user_dependency, db : db_dependency):
    if user is None or user.get("User_Role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Admin"
        )
    return db.query(Todos).all()

@router.delete("/delete/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user : user_dependency, db : db_dependency,
                      todo_id : int = Path(gt=0)):
    if user is None or user.get("User_Role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Admin"
        )
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not Found"
        )
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()