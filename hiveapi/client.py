import httpx


class HiveClient:
    def __init__(self, username: str, password: str, hive_url: str) -> None:
        self.hive_url = hive_url
        self._session = httpx.Client(base_url=hive_url)

        self._login(username, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def _login(self, username: str, password: str) -> None:
        self._session.get("/core/auth")

    def get(self, endpoint: str):
        self._session.get(endpoint)
