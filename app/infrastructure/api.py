from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Tip API", openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
