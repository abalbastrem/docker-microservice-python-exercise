from pymongo import MongoClient, errors

from Infrastructure.EnvEnum import Env
from Domain.Entities.Tip import Tip
from Infrastructure.Transformers.GetTipsByMongoTransformer import *

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
        try:
            self.client = MongoClient(MONGODB_CONNSTRING)
        except:
            raise errors.ConnectionFailure(message="could not connect to database. Chase CONNSTRING and mongo container")
        if self.env == Env.TEST:
            self.database = self.client[DATABASE_TEST]
        elif self.env == Env.PROD:
            self.database = self.client[DATABASE_PROD]
        else:
            raise errors.PyMongoError(message="database not found")
        try:
            self.collection = self.database[COLLECTION]
        except errors.CollectionInvalid:
            raise errors.CollectionInvalid

    def insertOne(self, tip: Tip):
        return self.collection.insert_one(tip.dict())

    def fetchMany(self, getTipsBy):
        tipsCursor = self.collection.find(getTipsBy)
        items = []
        for tip in tipsCursor:
            items.append(tip)
        return items

    def deleteAllTest(self):
        try:
            testCollection = self.client[DATABASE_TEST][COLLECTION]
            testCollection.delete_many({})
        except:
            raise errors.OperationFailure(error="could not delete TEST tips collection")