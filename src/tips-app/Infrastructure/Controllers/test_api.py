from fastapi.testclient import TestClient
from fastapi import Response

from Infrastructure.Controllers.api import app
from Infrastructure.Fixtures.TipFixture import *
from Infrastructure.EnvEnum import Env
from Application.Requests.GetTipsByRequest import GetTipsByRequest

client = TestClient(app)

ENDPOINT_ROOT = "/"
ENDPOINT_NEW = "/new/"
ENDPOINT_LIST = "/list/"

TEST_HEADER = {"env":str(Env.TEST)}
TEST_HEADER = {"env":"test"}

def test_read_root():
    response = client.get(ENDPOINT_ROOT, headers=TEST_HEADER)
    print(response)
    assert response.status_code == 200
    assert response.content == b"Hello test"

def test_new_tip():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip1_ok.json())
    assert response.status_code == 200
    assert response.content is not None
    assert response.content is str

def test_fetch_just_created_tip():
    getTips = GetTipsByRequest(tipster_id=mock_tip1_ok.tipster_id, match_id=mock_tip1_ok.match_id)
    response = client.post(ENDPOINT_LIST, headers=TEST_HEADER, params=getTips)
    assert response.status_code == 200
    assert response.content == mock_tip1_ok

# def test_new_tip_400():
#     response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip4_fail.json())
#     assert response.status_code == 400
#     assert response.error_message == "tipster_id cannot be null"

# def test_new_tip_same_tipster_same_match():
#     response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip1_ok.json())
#     assert response.status_code == 400
#     assert response.error_message == "cannot tip more than once on the same match"


# def test_list_tips_by_one_param():
#     listParams = {
#         "tipster_id": "111"
#     }

#     response = client.get(ENDPOINT_LIST, headers=TEST_HEADER, params=listParams)
#     assert response.status_code == 200
#     assert response.json() == [
#         mock_tip1_ok,
#         mock_tip2_ok,
#     ]

# def test_list_tips_by_several_param():
#     listParams = {
#         "tipster_id": "111",
#         "bookie_id": "333"
#     }

#     response = client.get(ENDPOINT_LIST, headers=TEST_HEADER, params=listParams)
#     assert response.status_code == 200
#     assert response.json() == [mock_tip1_ok]

# TODO drop test database colls after done?