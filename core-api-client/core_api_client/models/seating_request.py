from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeatingRequest")


@_attrs_define
class SeatingRequest:
    """
    Attributes:
        classroom (int):
        x (int):
        y (int):
        hostname (Union[None, Unset, str]):
        hanich (Union[None, Unset, int]):
    """

    classroom: int
    x: int
    y: int
    hostname: Union[None, Unset, str] = UNSET
    hanich: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("classroom", (None, str(self.classroom).encode(), "text/plain")))

        files.append(("x", (None, str(self.x).encode(), "text/plain")))

        files.append(("y", (None, str(self.y).encode(), "text/plain")))

        if not isinstance(self.hostname, Unset):
            if isinstance(self.hostname, str):
                files.append(("hostname", (None, str(self.hostname).encode(), "text/plain")))
            else:
                files.append(("hostname", (None, str(self.hostname).encode(), "text/plain")))

        if not isinstance(self.hanich, Unset):
            if isinstance(self.hanich, int):
                files.append(("hanich", (None, str(self.hanich).encode(), "text/plain")))
            else:
                files.append(("hanich", (None, str(self.hanich).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        seating_request = cls(
            classroom=classroom,
            x=x,
            y=y,
            hostname=hostname,
            hanich=hanich,
        )

        seating_request.additional_properties = d
        return seating_request

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
