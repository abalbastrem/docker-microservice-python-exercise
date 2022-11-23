from pymongo import MongoClient, errors
from pydantic import BaseModel

from Infrastructure.EnvEnum import Env
from Domain.Tip import Tip
from Application.Request.GetTipsByRequest import GetTipsByRequest, Range
from Infrastructure.Repos.GetTipsByTransformerMongo import *

# TODO init both DB and collections?
# TODO create unique compound index
# TODO use docker-compose env constants
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

    def insertOne(self, tip: Tip):
        return self.collection.insert_one(tip.dict())

    def fetchMany(self, getTipsBy):
        tipsCursor = self.collection.find(getTipsBy)
        items = []
        for tip in tipsCursor:
            items.append(tip)
        return items