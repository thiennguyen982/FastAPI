from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models.models import Todos
from routers.auth import get_current_user
from utilities.utils import db_dependency
from models.Todos import TodoRequest
from utilities import create_logger

router = APIRouter(
    tags=["Todos"]
)

user_dependency = Annotated[dict, Depends(get_current_user)]

todos_logger = create_logger("todos_logger","logging/todos.log", "INFO")

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user : user_dependency, db : db_dependency):
    todos_logger.info(f"User Execute Read All Function - {user}")
    if user is None:
        todos_logger.error(f"User Not Existed In Database - {user}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed Authentication"
        )
    return db.query(Todos).filter(Todos.owner_id == user.get("User_Id")).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo_by_id(user : user_dependency, db : db_dependency, todo_id : int = Path(gt=0)):
    todos_logger.info(f"User raed todo by id = {todo_id} - {user}")
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed Authentication"
        )
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("User_Id")).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(
        status_code=404,
        detail="Not Found"
    )

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user : user_dependency, db : db_dependency, 
                      todo_request : TodoRequest):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed Authorization"
        )
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("User_Id"))
    db.add(todo_model)
    db.commit()

@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_to(user : user_dependency, 
                    db : db_dependency, 
                    todo_request : TodoRequest, 
                    todo_id : int = Path(gt=0)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed Authorization"
        )
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("User_Id")).first()
    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user : user_dependency, 
                      db : db_dependency,
                      todo_id : int = Path(gt=0)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed Authorization"
        )
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("User_Id")).first()
    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    db.query(Todos).filter(Todos.id == todo_id).delete()
    
    db.commit()
    