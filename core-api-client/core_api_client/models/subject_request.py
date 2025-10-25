from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="SubjectRequest")


@_attrs_define
class SubjectRequest:
    """
    Attributes:
        symbol (str):
        parent_program (int):
        color (str):
        name (str):
    """

    symbol: str
    parent_program: int
    color: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        parent_program = self.parent_program

        color = self.color

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "parent_program": parent_program,
                "color": color,
                "name": name,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("symbol", (None, str(self.symbol).encode(), "text/plain")))

        files.append(("parent_program", (None, str(self.parent_program).encode(), "text/plain")))

        files.append(("color", (None, str(self.color).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        parent_program = d.pop("parent_program")

        color = d.pop("color")

        name = d.pop("name")

        subject_request = cls(
            symbol=symbol,
            parent_program=parent_program,
            color=color,
            name=name,
        )

        subject_request.additional_properties = d
        return subject_request

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
