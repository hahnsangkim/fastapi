from fastapi import FastAPI
from models.user import User


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/user")
async def post_user(user: User):
    return {"request body": user}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
