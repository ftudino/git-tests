from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()
products_router = APIRouter()
users_router = APIRouter()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/1")
def read_items():
    return {"items": "1"}

@router.get("/items/2")
def read_items():
    return {"items": "2"}

@router.get("/items/3")
def read_items():
    return {"items": "3"}

@router.get("/items/4")
def read_items():
    return {"items": "4"}


@products_router.get("/products/1")
def read_product():
    return {"product": "product 1"}

@products_router.get("/products/2")
def read_product():
    return {"product": "product 2"}

@products_router.get("/products/3")
def read_product():
    return {"product": "product 3"}

@products_router.get("/products/4")
def read_product():
    return {"product": "product 4"}


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


app.include_router(router)
app.include_router(products_router)
app.include_router(users_router)