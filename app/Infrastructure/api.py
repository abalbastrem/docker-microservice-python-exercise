from fastapi import FastAPI, Header, HTTPException
from Infrastructure.repo_mock import *
from Domain.Tip import Tip

app = FastAPI(title="Tip API")

@app.get("/")
async def read_root(test: str = Header()):
    if test:
        return {"Hello": "Test"}
    return {"Hello": "World"}

@app.post("/new/")
async def new_tip(tip: Tip, test: str = Header()):
    if test:
        return {"status": 201}
    return {"status": 200}


@app.get("/list/")
async def read_item(test: str = Header()):
    if test:
        return [mock_tip1_ok]
    return # actual list
