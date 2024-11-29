from fastapi import APIRouter

users_router = APIRouter()

@users_router.get("/users/1")
def read_user():
    return {"user": "user 1"}

@users_router.get("/users/2")
def read_user():
    return {"user": "user 2"}

@users_router.get("/users/3")
def read_user():
    return {"user": "user 3"}

@users_router.get("/users/4")
def read_user():
    return {"user": "user 4"}