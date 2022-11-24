from fastapi import FastAPI, Header, HTTPException, Response

from Infrastructure.EnvEnum import Env
from Application.Requests.CreateTipRequest import CreateTipRequest
from Application.Requests.GetTipsByRequest import GetTipsByRequest
from Application.Handlers.CreateTipHandler import CreateTipHandler
from Application.Handlers.GetTipsByHandler import GetTipsByHandler

app = FastAPI(title="Tips API")
# TODO test, test, test, test
# TODO HTTPExceptions, Responses
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
    inserted = handler.exec()
    return Response(status_code=200, content=str(inserted.inserted_id))

@app.post("/fetch") # TODO get? # TODO broken when different builds # TODO model_response List[Tip]
async def read_tip(getTipsByRequest: GetTipsByRequest, env: Env = Header()):
    handler = GetTipsByHandler(request=getTipsByRequest, env=env)
    return handler.exec()