from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateQueueRequest")


@_attrs_define
class DuplicateQueueRequest:
    """
    Attributes:
        name (str):
        module (Union[None, Unset, int]):
        user (Union[None, Unset, int]):
    """

    name: str
    module: Union[None, Unset, int] = UNSET
    user: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        module: Union[None, Unset, int]
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module

        user: Union[None, Unset, int]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if module is not UNSET:
            field_dict["module"] = module
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.module, Unset):
            if isinstance(self.module, int):
                files.append(("module", (None, str(self.module).encode(), "text/plain")))
            else:
                files.append(("module", (None, str(self.module).encode(), "text/plain")))

        if not isinstance(self.user, Unset):
            if isinstance(self.user, int):
                files.append(("user", (None, str(self.user).encode(), "text/plain")))
            else:
                files.append(("user", (None, str(self.user).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_module(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        module = _parse_module(d.pop("module", UNSET))

        def _parse_user(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user = _parse_user(d.pop("user", UNSET))

        duplicate_queue_request = cls(
            name=name,
            module=module,
            user=user,
        )

        duplicate_queue_request.additional_properties = d
        return duplicate_queue_request

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
