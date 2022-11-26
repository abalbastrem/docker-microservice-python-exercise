from fastapi import FastAPI, Header, HTTPException, Response

from Infrastructure.EnvEnum import Env
from Application.Requests.CreateTipRequest import CreateTipRequest
from Application.Requests.GetTipsByRequest import GetTipsByRequest
from Application.Handlers.CreateTipHandler import CreateTipHandler
from Application.Handlers.GetTipsByHandler import GetTipsByHandler

from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Infrastructure.Repos.MediaRepoHDD import MediaRepoHDD

from Infrastructure.Fixtures.TipFixture import *

app = FastAPI(title="Tips API")

@app.get("/")
async def read_root():
    return Response(status_code=200, content="Hello world")

@app.post("/new")
async def new_tip(createTipRequest: CreateTipRequest, env: Env = Header()):
    handler = CreateTipHandler(request=createTipRequest, env=env)
    try:
        inserted = handler.exec()
    except:
        raise HTTPException(status_code=500)
    return Response(status_code=200, content=str(inserted.inserted_id))

@app.post("/fetch")
async def read_tip(getTipsByRequest: GetTipsByRequest, env: Env = Header()):
    handler = GetTipsByHandler(request=getTipsByRequest, env=env)
    try:
        tips = handler.exec()
    except:
        raise HTTPException(status_code=500)
    return tips