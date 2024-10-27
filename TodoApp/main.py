from fastapi import FastAPI
import uvicorn
from models import models
from database import engine
from routers import todos, auth, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=8000, app=app)