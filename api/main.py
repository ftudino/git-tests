from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()
products_router = APIRouter()
users_router = APIRouter()
comments_router = APIRouter()
commons_router = APIRouter()


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


@comments_router.get("/comments/1")
def read_comment():
    return {"comment": "comment 1"}

@comments_router.get("/comments/2")
def read_comment():
    return {"comment": "comment 2"}

@comments_router.get("/comments/3")
def read_comment():
    return {"comment": "comment 3"}

@comments_router.get("/comments/4")
def read_comment():
    return {"comment": "comment 4"}


@commons_router.get("/commons/1")
def read_common():
    return {"common": "common 1"}

@commons_router.get("/commons/2")
def read_common():
    return {"common": "common 2"}

@commons_router.get("/commons/3")
def read_common():
    return {"common": "common 3"}


app.include_router(router)
app.include_router(products_router)
app.include_router(users_router)
app.include_router(comments_router)
app.include_router(commons_router)