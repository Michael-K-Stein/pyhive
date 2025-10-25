from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMeRequest")


@_attrs_define
class PatchedMeRequest:
    """
    Attributes:
        status (Union[Unset, StatusEnum]): * `Present` - Present
            * `Raised Hand` - Raisedhand
            * `Toilet Request` - Toiletrequest
            * `Toilet` - Toilet
            * `Personal Talk` - Personaltalk
            * `Work Talk` - Worktalk
            * `Medical` - Medical
            * `Prayer` - Prayer
            * `Room` - Room
            * `Home` - Home
        current_assignment (Union[None, Unset, int]):
        confirmed (Union[Unset, bool]):
        password (Union[Unset, str]):
        current_password (Union[Unset, str]):
        hostname (Union[Unset, str]):
    """

    status: Union[Unset, StatusEnum] = UNSET
    current_assignment: Union[None, Unset, int] = UNSET
    confirmed: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    current_password: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        current_assignment: Union[None, Unset, int]
        if isinstance(self.current_assignment, Unset):
            current_assignment = UNSET
        else:
            current_assignment = self.current_assignment

        confirmed = self.confirmed

        password = self.password

        current_password = self.current_password

        hostname = self.hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if current_assignment is not UNSET:
            field_dict["current_assignment"] = current_assignment
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if password is not UNSET:
            field_dict["password"] = password
        if current_password is not UNSET:
            field_dict["current_password"] = current_password
        if hostname is not UNSET:
            field_dict["hostname"] = hostname

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.current_assignment, Unset):
            if isinstance(self.current_assignment, int):
                files.append(("current_assignment", (None, str(self.current_assignment).encode(), "text/plain")))
            else:
                files.append(("current_assignment", (None, str(self.current_assignment).encode(), "text/plain")))

        if not isinstance(self.confirmed, Unset):
            files.append(("confirmed", (None, str(self.confirmed).encode(), "text/plain")))

        if not isinstance(self.password, Unset):
            files.append(("password", (None, str(self.password).encode(), "text/plain")))

        if not isinstance(self.current_password, Unset):
            files.append(("current_password", (None, str(self.current_password).encode(), "text/plain")))

        if not isinstance(self.hostname, Unset):
            files.append(("hostname", (None, str(self.hostname).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)

        def _parse_current_assignment(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        current_assignment = _parse_current_assignment(d.pop("current_assignment", UNSET))

        confirmed = d.pop("confirmed", UNSET)

        password = d.pop("password", UNSET)

        current_password = d.pop("current_password", UNSET)

        hostname = d.pop("hostname", UNSET)

        patched_me_request = cls(
            status=status,
            current_assignment=current_assignment,
            confirmed=confirmed,
            password=password,
            current_password=current_password,
            hostname=hostname,
        )

        patched_me_request.additional_properties = d
        return patched_me_request

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
