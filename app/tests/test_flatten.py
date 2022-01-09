from typing import Any, Dict, List
from json import dumps
from fastapi.testclient import TestClient

from app.core.constants import FLATTEN_ARRAY_URL, API_PREFIX

from app.main import app

client = TestClient(app)


def test_flatten_array_service() -> None:
    data: Dict[str, List[Any]] = {"input": [1, [2, 3, [4]], [5], 6, [7, [8]]]}
    response = client.post(f"{API_PREFIX}{FLATTEN_ARRAY_URL}", dumps(data))
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"output": [1, 2, 3, 4, 5, 6, 7, 8]}


def test_flatten_array_service_without_param() -> None:
    data: Dict[str, List[Any]] = {}
    response = client.post(f"{API_PREFIX}{FLATTEN_ARRAY_URL}", dumps(data))
    print(response.json())
    assert response.status_code == 400
    assert response.json() == {"detail": "Please check the data you sent."}
