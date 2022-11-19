from typing import Union

from pymongo import MongoClient, errors

DOMAIN = '172.18.0.3'
PORT = 27107

try:
    # client = MongoClient(
    #     host = [str(DOMAIN) + ":" + str(PORT)]
    #     serverSelectionTimeoutMS = 3000,
    #     username = 'root',
    #     password = 'tipsterchat',
    # )

    client = MongoClient(DOMAIN, 27107)

    print ("server version:", client.server_info()["version"])

    database_names = MongoClient().list_database_names()

except errors.ServerSelectionTimeoutError as err:
    print("ERROR")