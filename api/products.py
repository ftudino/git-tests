from fastapi import APIRouter

products_router = APIRouter()

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