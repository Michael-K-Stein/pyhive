from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Queue")


@_attrs_define
class Queue:
    """
    Attributes:
        id (int):
        name (str):
        user_id (Union[None, int]):
        user_name (Union[None, str]):
        subject_id (Union[None, int]):
        subject_name (Union[None, str]):
        subject_color (Union[None, str]):
        subject_symbol (Union[None, str]):
        module_id (Union[None, int]):
        module_name (Union[None, str]):
        module_order (Union[None, str]):
        program_id (int):
        program_name (str):
        description (Union[None, Unset, str]):
        module (Union[None, Unset, int]):
        user (Union[None, Unset, int]):
    """

    id: int
    name: str
    user_id: Union[None, int]
    user_name: Union[None, str]
    subject_id: Union[None, int]
    subject_name: Union[None, str]
    subject_color: Union[None, str]
    subject_symbol: Union[None, str]
    module_id: Union[None, int]
    module_name: Union[None, str]
    module_order: Union[None, str]
    program_id: int
    program_name: str
    description: Union[None, Unset, str] = UNSET
    module: Union[None, Unset, int] = UNSET
    user: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id: Union[None, int]
        user_id = self.user_id

        user_name: Union[None, str]
        user_name = self.user_name

        subject_id: Union[None, int]
        subject_id = self.subject_id

        subject_name: Union[None, str]
        subject_name = self.subject_name

        subject_color: Union[None, str]
        subject_color = self.subject_color

        subject_symbol: Union[None, str]
        subject_symbol = self.subject_symbol

        module_id: Union[None, int]
        module_id = self.module_id

        module_name: Union[None, str]
        module_name = self.module_name

        module_order: Union[None, str]
        module_order = self.module_order

        program_id = self.program_id

        program_name = self.program_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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
                "id": id,
                "name": name,
                "user_id": user_id,
                "user_name": user_name,
                "subject_id": subject_id,
                "subject_name": subject_name,
                "subject_color": subject_color,
                "subject_symbol": subject_symbol,
                "module_id": module_id,
                "module_name": module_name,
                "module_order": module_order,
                "program_id": program_id,
                "program_name": program_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if module is not UNSET:
            field_dict["module"] = module
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_user_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        user_id = _parse_user_id(d.pop("user_id"))

        def _parse_user_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_name = _parse_user_name(d.pop("user_name"))

        def _parse_subject_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        subject_id = _parse_subject_id(d.pop("subject_id"))

        def _parse_subject_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_name = _parse_subject_name(d.pop("subject_name"))

        def _parse_subject_color(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_color = _parse_subject_color(d.pop("subject_color"))

        def _parse_subject_symbol(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_symbol = _parse_subject_symbol(d.pop("subject_symbol"))

        def _parse_module_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        module_id = _parse_module_id(d.pop("module_id"))

        def _parse_module_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        module_name = _parse_module_name(d.pop("module_name"))

        def _parse_module_order(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        module_order = _parse_module_order(d.pop("module_order"))

        program_id = d.pop("program_id")

        program_name = d.pop("program_name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        queue = cls(
            id=id,
            name=name,
            user_id=user_id,
            user_name=user_name,
            subject_id=subject_id,
            subject_name=subject_name,
            subject_color=subject_color,
            subject_symbol=subject_symbol,
            module_id=module_id,
            module_name=module_name,
            module_order=module_order,
            program_id=program_id,
            program_name=program_name,
            description=description,
            module=module,
            user=user,
        )

        queue.additional_properties = d
        return queue

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
