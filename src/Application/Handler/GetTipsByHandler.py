from Application.Request.GetTipsByRequest import GetTipsByRequest
from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Infrastructure.EnvEnum import Env

class GetTipsByHandler():
    def __init__(self, request: GetTipsByRequest, env: Env.TEST):
        self.request = request
        self.repo = TipRepoMongo(env)

    def exec(self):
        return self.repo.fetchMany(self.request)