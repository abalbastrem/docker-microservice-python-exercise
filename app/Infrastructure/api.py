from fastapi import FastAPI, Header, HTTPException

from Infrastructure.EnvEnum import Env
from Infrastructure.TipRepoMock import *
from Infrastructure.TipRepoMongo import TipRepoMongo
from Domain.Tip import Tip

app = FastAPI(title="Tips API")

@app.get("/")
async def read_root(env: Env = Header()):
    if env == Env.TEST:
        return {"Hello": "Test"}
    if env == Env.PROD:
        return {"Hello": "World"}

@app.post("/new")
async def new_tip(tip: Tip, env: Env = Header()):
    repo = TipRepoMongo(env)
    inserted = repo.insertTip(tip)
    return {"insertedId": str(inserted.inserted_id)}


@app.get("/list")
async def read_item(env: Env = Header()):
    if env == Env.TEST:
        return [mock_tip1_ok]
    return # actual list