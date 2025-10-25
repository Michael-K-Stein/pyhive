from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSubjectRequest")


@_attrs_define
class PatchedSubjectRequest:
    """
    Attributes:
        symbol (Union[Unset, str]):
        parent_program (Union[Unset, int]):
        color (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    symbol: Union[Unset, str] = UNSET
    parent_program: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        parent_program = self.parent_program

        color = self.color

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if parent_program is not UNSET:
            field_dict["parent_program"] = parent_program
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.symbol, Unset):
            files.append(("symbol", (None, str(self.symbol).encode(), "text/plain")))

        if not isinstance(self.parent_program, Unset):
            files.append(("parent_program", (None, str(self.parent_program).encode(), "text/plain")))

        if not isinstance(self.color, Unset):
            files.append(("color", (None, str(self.color).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol", UNSET)

        parent_program = d.pop("parent_program", UNSET)

        color = d.pop("color", UNSET)

        name = d.pop("name", UNSET)

        patched_subject_request = cls(
            symbol=symbol,
            parent_program=parent_program,
            color=color,
            name=name,
        )

        patched_subject_request.additional_properties = d
        return patched_subject_request

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
