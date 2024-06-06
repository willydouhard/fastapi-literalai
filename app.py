from fastapi import APIRouter, FastAPI
from config import literal_client
from foo import foo

router = APIRouter()
app = FastAPI()

@router.get("/hello")
# @literal_client.thread
def hello():
    with literal_client.thread():
        literal_client.message(content="Hello, world!")
        foo()
        literal_client.message(content="Good bye, world!")

app.include_router(router)
