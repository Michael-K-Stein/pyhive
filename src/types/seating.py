from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from src.common import UNSET, Unset

T = TypeVar("T", bound="Seating")


@_attrs_define
class Seating:
    """
    Attributes:
        id (int):
        classroom (int):
        x (int):
        y (int):
        hostname (Union[None, Unset, str]):
        hanich (Union[None, Unset, int]):
    """

    hive_client: "HiveClient"
    id: int
    classroom: int
    x: int
    y: int
    hostname: Union[None, Unset, str] = UNSET
    hanich: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        classroom = self.classroom

        x = self.x

        y = self.y

        hostname: Union[None, Unset, str]
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        hanich: Union[None, Unset, int]
        if isinstance(self.hanich, Unset):
            hanich = UNSET
        else:
            hanich = self.hanich

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "classroom": classroom,
                "x": x,
                "y": y,
            }
        )
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if hanich is not UNSET:
            field_dict["hanich"] = hanich

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        classroom = d.pop("classroom")

        x = d.pop("x")

        y = d.pop("y")

        def _parse_hostname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_hanich(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        hanich = _parse_hanich(d.pop("hanich", UNSET))

        seating = cls(
            hive_client=hive_client,
            id=id,
            classroom=classroom,
            x=x,
            y=y,
            hostname=hostname,
            hanich=hanich,
        )

        seating.additional_properties = d
        return seating

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
