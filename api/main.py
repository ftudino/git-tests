from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/")
def read_items():
    return {"items": "items"}

app.include_router(router)