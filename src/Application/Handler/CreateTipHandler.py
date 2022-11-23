from Application.Request.CreateTipRequest import CreateTipRequest
from Domain.Tip import Tip
from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Infrastructure.Repos.MediaRepoHDD import MediaRepoHDD
from Infrastructure.EnvEnum import Env

class CreateTipHandler():
    def __init__(self, request: CreateTipRequest, env=Env.TEST):
        self.__request = request
        self.__tipRepo = TipRepoMongo(env)
        self.__mediaRepo = MediaRepoHDD(env)

    def exec(self):
        tip = Tip(
            tipster_id = self.__request.tipster_id, 
            match_id = self.__request.match_id, 
            analysis = self.__request.analysis, 
            bookie_id = self.__request.bookie_id, 
            rate = self.__request.rate, 
            stake = self.__request.stake, 
            pick_id = self.__request.pick_id, 
            media = self.__request.media
            )

        insertedTip = self.__tipRepo.insertOne(tip)
        self.__mediaRepo.insertMany(self.__request.media, insertedTip.inserted_id)

        return insertedTip