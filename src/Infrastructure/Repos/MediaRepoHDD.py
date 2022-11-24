from Domain.Entities.Media import Media
from Infrastructure.EnvEnum import Env
import os
from bson.objectid import ObjectId

class MediaRepoHDD():
    def __init__(self, env: str = Env.TEST):
        self.__intPathDir = "/media/"+str(env) # TODO wtf is wrong with Env?
        self.__intPathDir = "/media/"+"test/"
        self.__extPathDir = "/external_media/"

    def insertMany(self, media: Media, tipId: ObjectId):
        tipDir = str(tipId)
        for item in media.items:
            filename = os.path.basename(item)
            extFileFullPath = os.path.join(self.__extPathDir, filename)
            r = open(extFileFullPath, "r")
            fileContents = r.read()
            r.close()

            intTipFolder = os.path.join(self.__intPathDir, tipDir)
            intFileFullPath = os.path.join(intTipFolder, filename)
            if not os.path.exists(intTipFolder):
                os.makedirs(intTipFolder)
            w = open(intFileFullPath, "w")
            w.write(fileContents)
            w.close()

    def fetchMany(self, tipId: ObjectId):
        tipDir = str(tipId)
        intTipFolder = os.path.join(self.__intPathDir, tipDir)
        extTipFolder = os.path.join(self.__extPathDir, tipDir)
        for filename in os.listdir(intTipFolder):
            r = open(os.path.join(intTipFolder, filename), "r")
            fileContents = r.read()
            r.close()

            if not os.path.exists(extTipFolder):
                os.makedirs(extTipFolder)
            w = open(os.path.join(extTipFolder, filename), "w")
            w.write(fileContents)
            w.close()
