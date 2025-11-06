"""Shared client utilities and common mixin base for Hive API access.

- ``resolve_item_or_id``: helper that extracts an integer id from a model instance or int, preserving None.
- ``ClientCoreMixin``: base class that provides ``_get_core_items`` used by resource mixins.
"""

from typing import Any, Generator, Optional, TypeVar, overload, Union, cast

import httpx

from ..src.authenticated_hive_client import AuthenticatedHiveClient
from ..src.types.core_item import HiveCoreItem

CoreItemTypeT = TypeVar("CoreItemTypeT", bound="HiveCoreItem")


@overload
def resolve_item_or_id(item_or_id: None) -> None: ...


@overload
def resolve_item_or_id(item_or_id: HiveCoreItem | int) -> int: ...


def resolve_item_or_id(
    item_or_id: Union[HiveCoreItem, int, None],
) -> Optional[int]:
    """Return the integer id represented by ``item_or_id``.

    If ``item_or_id`` is ``None``, returns ``None``. If a ``HiveCoreItem`` is provided, its ``id`` is returned.
    If an ``int`` is provided, it is returned as-is.
    """
    if item_or_id is None:
        return None
    if not isinstance(item_or_id, (HiveCoreItem, int)):
        raise TypeError(
            f"Expected HiveCoreItem or int, got {type(item_or_id).__name__}"
        )
    return (
        cast(int, item_or_id.id) if hasattr(item_or_id, "id") else cast(int, item_or_id)
    )


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
