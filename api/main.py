from fastapi import FastAPI
from items import items_router
from products import products_router
from users import users_router

app = FastAPI()
router = APIRouter()
products_router = APIRouter()
users_router = APIRouter()
comments_router = APIRouter()
commons_router = APIRouter()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(items_router)
app.include_router(products_router)
app.include_router(users_router)
