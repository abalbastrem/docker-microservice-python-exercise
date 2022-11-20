from pymongo import MongoClient, errors

from Infrastructure.EnvEnum import Env
from Domain.Tip import Tip

MONGODB_CONNSTRING = "mongodb://root:tipsterchat@172.18.0.2:27017"
DATABASE_PROD = "tips_prod"
DATABASE_TEST = "tips_test"
COLLECTION = "tips"

class TipRepoMongo:
    def __init__(self, env=Env.TEST, autoConnect=True):
        self.env = env
        if autoConnect:
            self.__conn__()

    def __conn__(self):
        self.client = MongoClient(MONGODB_CONNSTRING)
        if self.env == Env.TEST:
            self.database = self.client[DATABASE_TEST]
        if self.env == Env.PROD:
            self.database = self.client[DATABASE_PROD]
        try:
            self.collection = self.database[COLLECTION]
        except errors.CollectionInvalid:
            return errors.CollectionInvalid

    def insertTip(self, tip: Tip):
        return self.collection.insert_one(tip.dict())

    def fetchTips(self, params):
        items = []
        for tip in self.collection.find(params):
            items.append(tip)