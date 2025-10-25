from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from client import HiveClient

T = TypeVar("T", bound="EventColor")


@_attrs_define
class EventColor:
    """Attributes:
    id (int):
    name (str):
    color (str):

    """

    id: int
    name: str
    color: str
    hive_client: "HiveClient"

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "color": color,
            },
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any], hive_client: "HiveClient") -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        color = d.pop("color")

        return cls(
            id=id,
            name=name,
            color=color,
            hive_client=hive_client,
        )
