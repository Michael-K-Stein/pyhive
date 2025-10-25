from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self

if TYPE_CHECKING:
    from client import HiveClient


class HiveCoreItem:
    def to_dict(self) -> dict[str, Any]:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any], hive_client: "HiveClient") -> Self:  # noqa: D102
        raise NotImplementedError
