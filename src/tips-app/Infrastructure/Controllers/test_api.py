from fastapi.testclient import TestClient
import json
import os

from Infrastructure.Repos.TipRepoMongo import TipRepoMongo
from Infrastructure.Repos.MediaRepoHDD import MediaRepoHDD

from Infrastructure.Controllers.api import app
from Infrastructure.Fixtures.TipFixture import *
from Infrastructure.EnvEnum import Env
from Application.Requests.GetTipsByRequest import GetTipsByRequest

client = TestClient(app)

ENDPOINT_ROOT = "/"
ENDPOINT_NEW = "/new/"
ENDPOINT_LIST = "/fetch/"
ENDPOINT_RESET = "/reset/"

TEST_HEADER_GET = {"env":"test"}
TEST_HEADER_POST = {
    "env":"test",
    "Content-Type": "application/json; charset=utf-8"
    }
WRONG_HEADER = {"env": "wrong_env"}

def test_hello_world_ok():
    response = client.get(ENDPOINT_ROOT, headers=TEST_HEADER_GET)
    assert response.status_code == 200
    assert response.content == b"Hello test"

def test_delete_items():
    tipRepo = TipRepoMongo(Env.TEST)
    mediaRepo = MediaRepoHDD(Env.TEST)
    tipRepo.deleteAllTest()
    mediaRepo.deleteAllTest()

    assert True == True

def test_wrong_header_fail():
    response = client.get(ENDPOINT_ROOT, headers=WRONG_HEADER)
    assert response.status_code == 422

def test_new_tip_ok():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip1_no_media_ok.dict())
    assert response.status_code == 200

def test_new_tip_ok_2():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip2_media_ok.dict())
    assert response.status_code == 200

def test_new_tip_ok_3():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip3_other_tipster_ok.dict())
    assert response.status_code == 200

def test_fetch_by_one_param_return_many_ok():
    request = GetTipsByRequest(
        tipster_id=tip1_no_media_ok.tipster_id, 
        )
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER_POST, json=request.dict())
    assert response.status_code == 200
    assert json.loads(response.content) == [tip1_no_media_ok.dict(), tip2_media_ok.dict()]

def test_fetch_by_several_param_return_one_ok():
    request = GetTipsByRequest(
        tipster_id=tip1_no_media_ok.tipster_id, 
        match_id=tip1_no_media_ok.match_id
        )
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER_POST, json=request.dict())
    assert response.status_code == 200
    assert json.loads(response.content) == [tip1_no_media_ok.dict()]

def test_fetch_by_several_param_return_zero_ok():
    request = GetTipsByRequest(
        tipster_id=tip3_other_tipster_ok.tipster_id, 
        match_id=tip1_no_media_ok.match_id
        )
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER_POST, json=request.dict())
    assert response.status_code == 200
    assert json.loads(response.content) == []

def test_new_tip_empty_field_fail():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip5_no_tipster_fail)
    assert response.status_code == 422
    assert json.loads(response.content)['detail'][0]['loc'] == ["body", "tipster_id"]

def test_new_tip_too_many_media_items_fail():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip6_too_many_media_fail)
    assert response.status_code == 422
    assert json.loads(response.content)['detail'][0]['loc'] == ["body", "media", "items"]

def test_new_tip_field_too_large_fail():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip7_too_large_stake_fail)
    assert response.status_code == 422
    assert json.loads(response.content)['detail'][0]['loc'] == ["body", "stake"]

# def test_new_tip_same_tipster_same_match():
#     response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=tip4_same_tipster_and_match_fail.json())
#     assert response.status_code == 400
#     assert response.error_message == "cannot tip more than once on the same match"

def test_media_moved_ext2int():
    mediaFolder = "/media/test/"
    mediaItem1 = "banana1.txt"
    mediaItem2 = "banana2.txt"
    mediaItem3 = "banana3.txt"
    fileCount = 0
    dirCount = 0
    for filename in os.listdir(mediaFolder):
        file_path = os.path.join(mediaFolder, filename)
        if os.path.isfile(file_path):
            fileCount += 1
        elif os.path.isdir(file_path):
            dirCount += 1
            assert os.path.exists(os.path.join(file_path, mediaItem1))
            assert os.path.exists(os.path.join(file_path, mediaItem2))
            assert os.path.exists(os.path.join(file_path, mediaItem3))
    
    assert fileCount == 0
    assert dirCount == 1

def test_media_moved_int2ext():
    mediaFolder = "/external_media/"
    mediaItem1 = "banana1.txt"
    mediaItem2 = "banana2.txt"
    mediaItem3 = "banana3.txt"

    assert os.path.exists(os.path.join(mediaFolder, mediaItem1))
    assert os.path.exists(os.path.join(mediaFolder, mediaItem2))
    assert os.path.exists(os.path.join(mediaFolder, mediaItem3))

    fileCount = 0
    dirCount = 0
    for filename in os.listdir(mediaFolder):
        file_path = os.path.join(mediaFolder, filename)
        if os.path.isfile(file_path):
            fileCount += 1
        elif os.path.isdir(file_path):
            dirCount += 1
            assert os.path.exists(os.path.join(file_path, mediaItem1))
            assert os.path.exists(os.path.join(file_path, mediaItem2))
            assert os.path.exists(os.path.join(file_path, mediaItem3))
    
    assert fileCount == 3
    assert dirCount > 0

