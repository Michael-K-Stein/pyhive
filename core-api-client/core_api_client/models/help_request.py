from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.help_type_enum import HelpTypeEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="HelpRequest")


@_attrs_define
class HelpRequest:
    """
    Attributes:
        user (int):
        help_type (HelpTypeEnum):
            * `Exercise` - Exercise
            * `Medical` - Medical
            * `Error` - Error
            * `Music` - Music
            * `Request` - Request
            * `Other` - Other
            * `Chat` - Chat
        exercise_id (Union[None, int]):
        title (Union[Unset, str]):
        visibility (Union[Unset, VisibilityEnum]): * `All Staff` - Allstaff
            * `All Staff And Checkers` - Allstaffandcheckers
            * `Author Only` - Authoronly
    """

    user: int
    help_type: HelpTypeEnum
    exercise_id: Union[None, int]
    title: Union[Unset, str] = UNSET
    visibility: Union[Unset, VisibilityEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        help_type = self.help_type.value

        exercise_id: Union[None, int]
        exercise_id = self.exercise_id

        title = self.title

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "help_type": help_type,
                "exercise_id": exercise_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("user", (None, str(self.user).encode(), "text/plain")))

        files.append(("help_type", (None, str(self.help_type.value).encode(), "text/plain")))

        if isinstance(self.exercise_id, int):
            files.append(("exercise_id", (None, str(self.exercise_id).encode(), "text/plain")))
        else:
            files.append(("exercise_id", (None, str(self.exercise_id).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.visibility, Unset):
            files.append(("visibility", (None, str(self.visibility.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user")

        help_type = HelpTypeEnum(d.pop("help_type"))

        def _parse_exercise_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        exercise_id = _parse_exercise_id(d.pop("exercise_id"))

        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, VisibilityEnum]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = VisibilityEnum(_visibility)

        help_request = cls(
            user=user,
            help_type=help_type,
            exercise_id=exercise_id,
            title=title,
            visibility=visibility,
        )

        help_request.additional_properties = d
        return help_request

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
