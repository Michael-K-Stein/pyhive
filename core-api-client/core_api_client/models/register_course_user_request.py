from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.gender_enum import GenderEnum

T = TypeVar("T", bound="RegisterCourseUserRequest")


@_attrs_define
class RegisterCourseUserRequest:
    """
    Attributes:
        first_name (str):
        last_name (str):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        gender (GenderEnum):
            * `Male` - Male
            * `Female` - Female
            * `NonBinary` - Nonbinary
        password (str):
        secret (str):
    """

    first_name: str
    last_name: str
    username: str
    gender: GenderEnum
    password: str
    secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        username = self.username

        gender = self.gender.value

        password = self.password

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "gender": gender,
                "password": password,
                "secret": secret,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        files.append(("username", (None, str(self.username).encode(), "text/plain")))

        files.append(("gender", (None, str(self.gender.value).encode(), "text/plain")))

        files.append(("password", (None, str(self.password).encode(), "text/plain")))

        files.append(("secret", (None, str(self.secret).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        username = d.pop("username")

        gender = GenderEnum(d.pop("gender"))

        password = d.pop("password")

        secret = d.pop("secret")

        register_course_user_request = cls(
            first_name=first_name,
            last_name=last_name,
            username=username,
            gender=gender,
            password=password,
            secret=secret,
        )

        register_course_user_request.additional_properties = d
        return register_course_user_request

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
