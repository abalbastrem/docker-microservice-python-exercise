from Application.Requests.GetTipsByRequest import GetTipsByRequest
from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Infrastructure.Repos.MediaRepoHDD import MediaRepoHDD
from Infrastructure.Transformers.GetTipsByMongoTransformer import GetTipsByMongoTransformer
from Infrastructure.EnvEnum import Env

class GetTipsByHandler():
    def __init__(self, request: GetTipsByRequest, env: Env.TEST):
        self.__request = (GetTipsByMongoTransformer(request)).exec()
        self.__tipRepo = TipRepoMongo(env)
        self.__mediaRepo = MediaRepoHDD(env)

    def exec(self):
        tips = self.__tipRepo.fetchMany(self.__request)

        for tip in tips:
            self.__mediaRepo.fetchMany(tip['_id'])
            del tip['_id']

        return tips