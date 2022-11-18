from fastapi.testclient import TestClient

from api import app
from repo_mock import *

client = TestClient(app)

ENDPOINT_ROOT = "/"
ENDPOINT_NEW = "/new/"
ENDPOINT_LIST = "/list/"

def test_read_root():
    response = client.get(ENDPOINT_ROOT)
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_new_tip():
    response = client.post(ENDPOINT_NEW, json=mock_tip1_ok)
    assert response.status_code == 201

def test_new_tip_400():
    response = client.post(ENDPOINT_NEW, json=mock_tip3_fail)
    assert response.status_code == 400
    assert response.error_message == "tipster_id cannot be null"

def test_list_tips_by_one_param():
    listParams = {
        "test": True,
        "tipster_id": "111"
    }

    response = client.get(ENDPOINT_LIST, params=listParams)
    assert response.status_code == 200
    assert response.json() == [
        mock_tip1_ok,
        mock_tip2_ok,
    ]

def test_list_tips_by_several_param():
    listParams = {
        "test": True,
        "tipster_id": "111",
        "bookie_id": "333"
    }

    response = client.get(ENDPOINT_LIST, params=listParams)
    assert response.status_code == 200
    assert response.json() == [mock_tip1_ok]