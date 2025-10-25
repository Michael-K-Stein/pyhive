from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.class_type_enum import ClassTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedClassRequest")


@_attrs_define
class PatchedClassRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        program (Union[Unset, int]):
        users (Union[Unset, list[int]]):
        email (Union[Unset, str]):
        type_ (Union[Unset, ClassTypeEnum]): * `Room` - Room
            * `Student Group` - Studentgroup
        classes (Union[Unset, list[int]]):
        description (Union[None, Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    program: Union[Unset, int] = UNSET
    users: Union[Unset, list[int]] = UNSET
    email: Union[Unset, str] = UNSET
    type_: Union[Unset, ClassTypeEnum] = UNSET
    classes: Union[Unset, list[int]] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        program = self.program

        users: Union[Unset, list[int]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        email = self.email

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        classes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if program is not UNSET:
            field_dict["program"] = program
        if users is not UNSET:
            field_dict["users"] = users
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if classes is not UNSET:
            field_dict["classes"] = classes
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.program, Unset):
            files.append(("program", (None, str(self.program).encode(), "text/plain")))

        if not isinstance(self.users, Unset):
            for users_item_element in self.users:
                files.append(("users", (None, str(users_item_element).encode(), "text/plain")))

        if not isinstance(self.email, Unset):
            files.append(("email", (None, str(self.email).encode(), "text/plain")))

        if not isinstance(self.type_, Unset):
            files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        if not isinstance(self.classes, Unset):
            for classes_item_element in self.classes:
                files.append(("classes", (None, str(classes_item_element).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        program = d.pop("program", UNSET)

        users = cast(list[int], d.pop("users", UNSET))

        email = d.pop("email", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ClassTypeEnum]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClassTypeEnum(_type_)

        classes = cast(list[int], d.pop("classes", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        patched_class_request = cls(
            name=name,
            program=program,
            users=users,
            email=email,
            type_=type_,
            classes=classes,
            description=description,
        )

        patched_class_request.additional_properties = d
        return patched_class_request

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
