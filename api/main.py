from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


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


app.include_router(router)