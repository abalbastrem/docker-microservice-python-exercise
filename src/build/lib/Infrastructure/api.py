from fastapi import FastAPI, Header, HTTPException

from Infrastructure.EnvEnum import Env
from Infrastructure.Repos.TipRepoMock import *
from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Domain.Tip import Tip
from Application.Request.GetTipsByRequest import GetTipsByRequest

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
    inserted = repo.insertOne(tip)
    return {"insertedId": str(inserted.inserted_id)}


@app.get("/list")
async def read_item(getTipsBy: GetTipsByRequest, env: Env = Header()):
    repo = TipRepoMongo(env)
    repo.fetchMany(getTipsBy)
    return # actual list