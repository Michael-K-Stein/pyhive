import functools
import time
from collections.abc import Callable
from types import TracebackType
from typing import Any, TypeVar, cast

import httpx

F = TypeVar("F", bound=Callable[..., httpx.Response])

MAX_RETRIES_ON_SERVER_ERRORS = 5
INITIAL_BACKOFF_SECONDS = 0.5


def _retry_on_bad_gateway(func: F) -> F:
    @functools.wraps(func)
    def wrapper(self: "_AuthenticatedHiveClient", *args: Any, **kwargs: Any):
        delay = INITIAL_BACKOFF_SECONDS
        if MAX_RETRIES_ON_SERVER_ERRORS <= 0:
            raise ValueError("MAX_RETRIES_ON_SERVER_ERRORS must be greater than 0")
        response = None
        for attempt in range(MAX_RETRIES_ON_SERVER_ERRORS):
            response = func(self, *args, **kwargs)
            if response.status_code != httpx.codes.BAD_GATEWAY.value:
                return response
            if attempt < MAX_RETRIES_ON_SERVER_ERRORS - 1:
                time.sleep(delay)
                delay *= 2
        assert response is not None
        response.raise_for_status()
        return response

    return cast("F", wrapper)


def _refresh_token_on_unauthorized(func: F) -> F:
    @functools.wraps(func)
    def wrapper(self: "_AuthenticatedHiveClient", *args: Any, **kwargs: Any):
        response = func(self, *args, **kwargs)
        if response.status_code == httpx.codes.UNAUTHORIZED.value:
            self._refresh_access_token()  # pyright: ignore[reportPrivateUsage]
            response = func(self, *args, **kwargs)
        response.raise_for_status()
        return response

    return cast("F", wrapper)


def _with_retries_and_token_refresh(func: F) -> F:
    return _refresh_token_on_unauthorized(_retry_on_bad_gateway(func))


class _AuthenticatedHiveClient:
    """Internal class used to handle authentication and re-authentication with Hive web endpoint."""

    _refresh_token: str
    _access_token: str
    _session: httpx.Client
    username: str

    def __init__(
        self,
        username: str,
        password: str,
        hive_url: str,
        **kwargs: Any,
    ) -> None:
        self.username = username
        self.hive_url = hive_url
        self._session = httpx.Client(
            base_url=hive_url,
            **kwargs,
        ).__enter__()
        self._login(username, password)

    def __enter__(self) -> "_AuthenticatedHiveClient":
        return self

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        self._session.__exit__(type_, value, traceback)

    def _login(self, username: str, password: str) -> None:
        response = self._session.post(
            "/api/core/token/",
            json={"username": username, "password": password},
        )
        response.raise_for_status()
        data = response.json()
        self._access_token = data["access"]
        self._refresh_token = data["refresh"]

        self._session.headers.update({"Authorization": f"Bearer {self._access_token}"})

    def _refresh_access_token(self) -> None:
        response = self._session.post(
            "/api/core/token/refresh/",
            json={"refresh": self._refresh_token},
        )
        response.raise_for_status()
        data = response.json()
        self._access_token = data["access"]
        self._refresh_token = data["refresh"]

        self._session.headers.update({"Authorization": f"Bearer {self._access_token}"})

    @_with_retries_and_token_refresh
    def _get(
        self, endpoint: str, params: httpx.QueryParams | None = None
    ) -> httpx.Response:
        return self._session.get(endpoint, params=params)

    @_with_retries_and_token_refresh
    def _post(self, endpoint: str, data: dict[Any, Any]) -> httpx.Response:
        return self._session.post(endpoint, json=data)

    @_with_retries_and_token_refresh
    def _patch(self, endpoint: str, data: dict[Any, Any]) -> httpx.Response:
        return self._session.patch(endpoint, json=data)

    @_with_retries_and_token_refresh
    def _delete(self, endpoint: str) -> httpx.Response:
        return self._session.delete(endpoint)

    @_with_retries_and_token_refresh
    def _put(self, endpoint: str, data: dict[Any, Any]) -> httpx.Response:
        return self._session.put(endpoint, json=data)

    def get(self, endpoint: str, params: httpx.QueryParams | None = None) -> Any:
        return self._get(endpoint, params).json()

    def post(self, endpoint: str, data: dict[Any, Any]) -> Any:
        return self._post(endpoint, data).json()

    def __repr__(self) -> str:
        return f"HiveClient({self.username!r}, input(), {self.hive_url!r})"
