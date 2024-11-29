from fastapi import FastAPI
from items import items_router
from products import products_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(items_router)
app.include_router(products_router)