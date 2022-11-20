from fastapi.testclient import TestClient

from api import app
from repo_mock import *

client = TestClient(app)

ENDPOINT_ROOT = "/"
ENDPOINT_NEW = "/new/"
ENDPOINT_LIST = "/list/"

TEST_HEADER = {"test": str(True)}

def test_read_root():
    response = client.get(ENDPOINT_ROOT, headers=TEST_HEADER)
    assert response.status_code == 200
    assert response.json() == {"Hello": "Test"}

def test_new_tip():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip1_ok)
    assert response.status_code == 201

def test_new_tip_400():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip4_fail)
    assert response.status_code == 400
    assert response.error_message == "tipster_id cannot be null"

def test_new_tip_same_tipster_same_match():
    response = client.post(ENDPOINT_NEW, headers=TEST_HEADER, json=mock_tip1_ok)
    assert response.status_code == 400
    assert response.error_message == "cannot tip more than once on the same match"

def test_list_tips_by_one_param():
    listParams = {
        "tipster_id": "111"
    }

    response = client.get(ENDPOINT_LIST, headers=TEST_HEADER, params=listParams)
    assert response.status_code == 200
    assert response.json() == [
        mock_tip1_ok,
        mock_tip2_ok,
    ]

def test_list_tips_by_several_param():
    listParams = {
        "tipster_id": "111",
        "bookie_id": "333"
    }

    response = client.get(ENDPOINT_LIST, headers=TEST_HEADER, params=listParams)
    assert response.status_code == 200
    assert response.json() == [mock_tip1_ok]