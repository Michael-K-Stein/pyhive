from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.help_type_enum import HelpTypeEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedHelpRequest")


@_attrs_define
class PatchedHelpRequest:
    """
    Attributes:
        user (Union[Unset, int]):
        title (Union[Unset, str]):
        help_type (Union[Unset, HelpTypeEnum]): * `Exercise` - Exercise
            * `Medical` - Medical
            * `Error` - Error
            * `Music` - Music
            * `Request` - Request
            * `Other` - Other
            * `Chat` - Chat
        exercise_id (Union[None, Unset, int]):
        visibility (Union[Unset, VisibilityEnum]): * `All Staff` - Allstaff
            * `All Staff And Checkers` - Allstaffandcheckers
            * `Author Only` - Authoronly
    """

    user: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    help_type: Union[Unset, HelpTypeEnum] = UNSET
    exercise_id: Union[None, Unset, int] = UNSET
    visibility: Union[Unset, VisibilityEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        title = self.title

        help_type: Union[Unset, str] = UNSET
        if not isinstance(self.help_type, Unset):
            help_type = self.help_type.value

        exercise_id: Union[None, Unset, int]
        if isinstance(self.exercise_id, Unset):
            exercise_id = UNSET
        else:
            exercise_id = self.exercise_id

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if title is not UNSET:
            field_dict["title"] = title
        if help_type is not UNSET:
            field_dict["help_type"] = help_type
        if exercise_id is not UNSET:
            field_dict["exercise_id"] = exercise_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.user, Unset):
            files.append(("user", (None, str(self.user).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.help_type, Unset):
            files.append(("help_type", (None, str(self.help_type.value).encode(), "text/plain")))

        if not isinstance(self.exercise_id, Unset):
            if isinstance(self.exercise_id, int):
                files.append(("exercise_id", (None, str(self.exercise_id).encode(), "text/plain")))
            else:
                files.append(("exercise_id", (None, str(self.exercise_id).encode(), "text/plain")))

        if not isinstance(self.visibility, Unset):
            files.append(("visibility", (None, str(self.visibility.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user", UNSET)

        title = d.pop("title", UNSET)

        _help_type = d.pop("help_type", UNSET)
        help_type: Union[Unset, HelpTypeEnum]
        if isinstance(_help_type, Unset):
            help_type = UNSET
        else:
            help_type = HelpTypeEnum(_help_type)

        def _parse_exercise_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        exercise_id = _parse_exercise_id(d.pop("exercise_id", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, VisibilityEnum]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = VisibilityEnum(_visibility)

        patched_help_request = cls(
            user=user,
            title=title,
            help_type=help_type,
            exercise_id=exercise_id,
            visibility=visibility,
        )

        patched_help_request.additional_properties = d
        return patched_help_request

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
