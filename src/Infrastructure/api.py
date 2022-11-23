from fastapi import FastAPI, Header, HTTPException

from Infrastructure.EnvEnum import Env
from Application.Request.CreateTipRequest import CreateTipRequest
from Application.Request.GetTipsByRequest import GetTipsByRequest
from Application.Handler.CreateTipHandler import CreateTipHandler
from Application.Handler.GetTipsByHandler import GetTipsByHandler

app = FastAPI(title="Tips API")
# TODO test, test, test, test
# TODO docs
# TODO go full hexagonal, with interfaces and instantiations
# TODO HTTPExceptions

@app.get("/")
async def read_root(env: Env = Header()):
    if env == Env.TEST:
        return {"Hello": "Test"}
    if env == Env.PROD:
        return {"Hello": "World"}

@app.post("/new")
async def new_tip(createTipRequest: CreateTipRequest, env: Env = Header()):
    handler = CreateTipHandler(request=createTipRequest, env=env)
    inserted = handler.exec()
    return {"inserted": str(inserted.inserted_id)}

@app.post("/fetch") # TODO get? # TODO broken when different builds
async def read_tip(getTipsByRequest: GetTipsByRequest, env: Env = Header()):
    handler = GetTipsByHandler(request=getTipsByRequest, env=env)
    return handler.exec()