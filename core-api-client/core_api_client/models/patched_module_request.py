from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedModuleRequest")


@_attrs_define
class PatchedModuleRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        parent_subject (Union[Unset, int]):
        order (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    parent_subject: Union[Unset, int] = UNSET
    order: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent_subject = self.parent_subject

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if parent_subject is not UNSET:
            field_dict["parent_subject"] = parent_subject
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.parent_subject, Unset):
            files.append(("parent_subject", (None, str(self.parent_subject).encode(), "text/plain")))

        if not isinstance(self.order, Unset):
            files.append(("order", (None, str(self.order).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        parent_subject = d.pop("parent_subject", UNSET)

        order = d.pop("order", UNSET)

        patched_module_request = cls(
            name=name,
            parent_subject=parent_subject,
            order=order,
        )

        patched_module_request.additional_properties = d
        return patched_module_request

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
