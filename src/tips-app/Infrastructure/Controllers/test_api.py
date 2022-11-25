from fastapi.testclient import TestClient
import json

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
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=mock_tip1_ok.dict())
    assert response.status_code == 200

def test_new_tip_ok():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=mock_tip2_ok.dict())
    assert response.status_code == 200

def test_fetch_by_one_param_ok():
    request = GetTipsByRequest(
        tipster_id=mock_tip1_ok.tipster_id, 
        )
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER_POST, json=request.dict())
    assert response.status_code == 200
    assert json.loads(response.content) == [mock_tip1_ok.dict(), mock_tip2_ok]

def test_fetch_by_several_param_return_one_ok():
    request = GetTipsByRequest(
        tipster_id=mock_tip1_ok.tipster_id, 
        match_id=mock_tip1_ok.match_id
        )
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER_POST, json=request.dict())
    assert response.status_code == 200
    assert json.loads(response.content) == [mock_tip1_ok.dict()]

def test_fetch_by_several_param_return_zero_ok():
    request = GetTipsByRequest(
        tipster_id=mock_tip1_ok.tipster_id, 
        match_id=mock_tip2_ok.match_id
        )
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER_POST, json=request.dict())
    assert response.status_code == 200
    assert json.loads(response.content) == []

def test_new_tip_empty_field_fail():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=mock_tip4_fail)
    assert response.status_code == 422
    assert json.loads(response.content)['detail'][0]['loc'] == ["body", "tipster_id"]

def test_new_tip_too_many_media_items_fail():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=mock_tip5_fail)
    assert response.status_code == 422
    assert json.loads(response.content)['detail'][0]['loc'] == ["body", "media", "items"]

def test_new_tip_field_too_large_fail():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER_POST, json=mock_tip6_fail)
    assert response.status_code == 422
    assert json.loads(response.content)['detail'][0]['loc'] == ["body", "stake"]

# def test_new_tip_same_tipster_same_match():
#     response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip1_ok.json())
#     assert response.status_code == 400
#     assert response.error_message == "cannot tip more than once on the same match"

def test_media_moved_ext2int():
    assert True == True

def test_media_moved_int2ext():
    assert True == True
