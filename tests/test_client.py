import httpx
from client import HiveClient
from src.types.class_ import Class
from tests.common import get_client_params


def test_client():
    hive_url = "https://hive.org"
    with HiveClient("michaelks", "Password1", hive_url, verify=False) as client:
        assert client.hive_url == hive_url


def test_get():
    with HiveClient(**get_client_params()) as client:
        response = client._get("/")
        response.raise_for_status()
        assert response.status_code == httpx.codes.OK


def test_get_classes_returns_generator_and_calls_get():
    with (
        HiveClient(**get_client_params()) as client,
    ):
        # Act
        result = list(client.get_classes())

        # Assert
        assert len(result) == 7
        assert all(isinstance(item, Class) for item in result)
