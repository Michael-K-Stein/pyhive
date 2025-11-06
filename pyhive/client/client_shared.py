"""Shared client utilities and common mixin base for Hive API access.

- ``ClientCoreMixin``: base class that provides ``_get_core_items`` used by resource mixins.
"""

from typing import Any, Generator, Optional

import httpx

from ..src.authenticated_hive_client import AuthenticatedHiveClient
from .utils import CoreItemTypeT


class ClientCoreMixin(AuthenticatedHiveClient):
    """Common mixin base that exposes ``_get_core_items`` for list endpoints.

    This relies on the authenticated transport provided by the base client and is designed to be used only on
    the composed ``HiveClient``.
    """

    def _get_core_items(
        self,
        endpoint: str,
        item_type: type[CoreItemTypeT],
        /,
        extra_ctor_params: Optional[dict[str, Any]] = None,
        **kwargs,
    ) -> Generator[CoreItemTypeT, None, None]:
        """Yield typed items from a list endpoint with optional query parameters."""
        from ..client import HiveClient

        assert isinstance(self, HiveClient), "self must be an instance of HiveClient"

        if extra_ctor_params is None:
            extra_ctor_params = {}
        query_params = httpx.QueryParams()
        for name, value in kwargs.items():
            if value is not None:
                if isinstance(value, list):
                    query_params = query_params.set(
                        name, ",".join(str(x) for x in value)
                    )
                else:
                    query_params = query_params.set(name, value)
        return (
            item_type.from_dict(x, **extra_ctor_params, hive_client=self)
            for x in self.get(endpoint, params=query_params)
        )
