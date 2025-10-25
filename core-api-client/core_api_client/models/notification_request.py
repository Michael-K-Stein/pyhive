from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationRequest")


@_attrs_define
class NotificationRequest:
    """
    Attributes:
        user (int):
        help_ (Union[None, Unset, int]):
        assignment (Union[None, Unset, int]):
        comment (Union[Unset, str]):
        was_read (Union[Unset, bool]):
    """

    user: int
    help_: Union[None, Unset, int] = UNSET
    assignment: Union[None, Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    was_read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        help_: Union[None, Unset, int]
        if isinstance(self.help_, Unset):
            help_ = UNSET
        else:
            help_ = self.help_

        assignment: Union[None, Unset, int]
        if isinstance(self.assignment, Unset):
            assignment = UNSET
        else:
            assignment = self.assignment

        comment = self.comment

        was_read = self.was_read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )
        if help_ is not UNSET:
            field_dict["help"] = help_
        if assignment is not UNSET:
            field_dict["assignment"] = assignment
        if comment is not UNSET:
            field_dict["comment"] = comment
        if was_read is not UNSET:
            field_dict["was_read"] = was_read

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("user", (None, str(self.user).encode(), "text/plain")))

        if not isinstance(self.help_, Unset):
            if isinstance(self.help_, int):
                files.append(("help", (None, str(self.help_).encode(), "text/plain")))
            else:
                files.append(("help", (None, str(self.help_).encode(), "text/plain")))

        if not isinstance(self.assignment, Unset):
            if isinstance(self.assignment, int):
                files.append(("assignment", (None, str(self.assignment).encode(), "text/plain")))
            else:
                files.append(("assignment", (None, str(self.assignment).encode(), "text/plain")))

        if not isinstance(self.comment, Unset):
            files.append(("comment", (None, str(self.comment).encode(), "text/plain")))

        if not isinstance(self.was_read, Unset):
            files.append(("was_read", (None, str(self.was_read).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user")

        def _parse_help_(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        help_ = _parse_help_(d.pop("help", UNSET))

        def _parse_assignment(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assignment = _parse_assignment(d.pop("assignment", UNSET))

        comment = d.pop("comment", UNSET)

        was_read = d.pop("was_read", UNSET)

        notification_request = cls(
            user=user,
            help_=help_,
            assignment=assignment,
            comment=comment,
            was_read=was_read,
        )

        notification_request.additional_properties = d
        return notification_request

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
