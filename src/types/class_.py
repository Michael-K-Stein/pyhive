from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.class_type_enum import ClassTypeEnum
from src.common import UNSET, Unset

T = TypeVar("T", bound="Class")


@_attrs_define
class Class:
    """
    Attributes:
        id (int):
        name (str):
        display_name (str):
        program (int):
        users (list[int]):
        program_name (str):
        email (Union[Unset, str]):
        type_ (Union[Unset, ClassTypeEnum]): * `Room` - Room
            * `Student Group` - Studentgroup
        description (Union[None, Unset, str]):
    """

    hive_client: "HiveClient"
    id: int
    name: str
    display_name: str
    program: int
    users: list[int]
    program_name: str
    email: Union[Unset, str] = UNSET
    type_: Union[Unset, ClassTypeEnum] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        program = self.program

        users = self.users

        program_name = self.program_name

        email = self.email

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "program": program,
                "users": users,
                "program__name": program_name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("display_name")

        program = d.pop("program")

        users = cast(list[int], d.pop("users"))

        program_name = d.pop("program__name")

        email = d.pop("email", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ClassTypeEnum]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClassTypeEnum(_type_)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        class_ = cls(
            hive_client=hive_client,
            id=id,
            name=name,
            display_name=display_name,
            program=program,
            users=users,
            program_name=program_name,
            email=email,
            type_=type_,
            description=description,
        )

        class_.additional_properties = d
        return class_

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
