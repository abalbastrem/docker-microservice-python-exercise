from fastapi import FastAPI, Header, HTTPException

from Infrastructure.EnvEnum import Env
from Infrastructure.Repos.TipRepoMock import *
from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Domain.Tip import Tip
from Application.Request.GetTipsByRequest import GetTipsByRequest

app = FastAPI(title="Tips API")
# TODO docs
# TODO ApplicationLayer
# TODO HTTPExceptions

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

@app.post("/fetch") # TODO get?
async def read_tip(getTipsBy: GetTipsByRequest, env: Env = Header()):
    repo = TipRepoMongo(env)
    return repo.fetchTips(getTipsBy)