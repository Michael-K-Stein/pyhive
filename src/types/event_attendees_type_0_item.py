from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from src.common import UNSET, Unset

T = TypeVar("T", bound="EventAttendeesType0Item")


@_attrs_define
class EventAttendeesType0Item:
    """
    Attributes:
        name (str):
        id (int):
        description (Union[Unset, str]):
    """

    hive_client: "HiveClient"
    name: str
    id: int
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id")

        description = d.pop("description", UNSET)

        event_attendees_type_0_item = cls(
            name=name,
            id=id,
            description=description,
        )

        event_attendees_type_0_item.additional_properties = d
        return event_attendees_type_0_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
