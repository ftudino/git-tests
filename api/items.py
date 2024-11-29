from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/items/1")
def read_item():
    return {"item": "item 1"}

@items_router.get("/items/2")
def read_item():
    return {"item": "item 2"}

@items_router.get("/items/3")
def read_item():
    return {"item": "item 3"}

@items_router.get("/items/4")
def read_item():
    return {"item": "item 4"}