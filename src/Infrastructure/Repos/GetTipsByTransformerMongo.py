from Application.Request.GetTipsByRequest import GetTipsByRequest, Range

class GetTipsByTransformerMongo():
    def __init__(self, getTipsBy: GetTipsByRequest):
        self.__model = getTipsBy

    def exec(self):
        query = self.__model.dict(exclude_none=True)
        if self.__model.rate_range is not None:
            del query["rate_range"]
            query["rate"] = {"$gte": self.__model.rate_range.min, "$lte": self.__model.rate_range.max}
        if self.__model.stake_range is not None:
            del query["stake_range"]
            query["stake"] = {"$gte": self.__model.stake_range.min, "$lte": self.__model.stake_range.max}
        if self.__model.has_media is not None:
            del query["has_media"]
            if self.__model.has_media:
                query["media"] = {"$exists": True, "$type": 'array', "$ne": []}
            else:
                query["media"] = {"$exists": True, "$type": 'array', "$eq": []}

        return query