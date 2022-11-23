from Application.Request.CreateTipRequest import CreateTipRequest
from Domain.Tip import Tip
from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Infrastructure.EnvEnum import Env

class CreateTipHandler():
    def __init__(self, request: CreateTipRequest, env=Env.TEST):
        self.request = request
        self.repo = TipRepoMongo(env)

    def exec(self):
        tip = Tip(
            tipster_id = self.request.tipster_id, 
            match_id = self.request.match_id, 
            analysis = self.request.analysis, 
            bookie_id = self.request.bookie_id, 
            rate = self.request.rate, 
            stake = self.request.stake, 
            pick_id = self.request.pick_id, 
            media = self.request.media
            )

        return self.repo.insertOne(tip)