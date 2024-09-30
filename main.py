from fastapi import FastAPI
from app.models import task, user
from app.routers import task1, user1

app = FastAPI()


@app.get("/")
async def main_():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user1.router)
app.include_router(task1.router)
app.include_router(user.router)
app.include_router(task.router)

