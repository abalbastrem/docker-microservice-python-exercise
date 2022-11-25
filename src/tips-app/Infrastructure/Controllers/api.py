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
# TODO test, test, test, test
# TODO docs
# TODO go full hexagonal, with interfaces and instantiations

@app.get("/")
async def read_root(env: Env = Header()):
    if env == Env.TEST:
        return Response(status_code=200, content="Hello test")
    if env == Env.PROD:
        return Response(status_code=200, content="Hello world")

@app.post("/new")
async def new_tip(createTipRequest: CreateTipRequest, env: Env = Header()):
    handler = CreateTipHandler(request=createTipRequest, env=env)
    try:
        handler.exec()
    except:
        raise HTTPException(status_code=500)
    return Response(status_code=200)

@app.post("/fetch") # TODO get? # TODO broken when different builds # TODO model_response List[Tip]
async def read_tip(getTipsByRequest: GetTipsByRequest, env: Env = Header()):
    handler = GetTipsByHandler(request=getTipsByRequest, env=env)
    try:
        tips = handler.exec()
    except:
        raise HTTPException(status_code=500)
    return tips

@app.get("/reset")
async def reset_env_db(token: str = Header()):
    if token != "root":
        raise HTTPException(status_code=101, detail="permission denied")
    tipRepo = TipRepoMongo(Env.TEST)
    mediaRepo = MediaRepoHDD(Env.TEST)
    tipRepo.deleteAllTest()
    mediaRepo.deleteAllTest()

    return Response(status_code=200, content="All test DB items deleted")