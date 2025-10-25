import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.help_response_type_enum import HelpResponseTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="HelpResponseSegelNested")


@_attrs_define
class HelpResponseSegelNested:
    """
    Attributes:
        id (int):
        user (int):
        date (datetime.datetime):
        response_type (HelpResponseTypeEnum):
            * `Resolve` - Resolve
            * `Open` - Open
            * `Comment` - Comment
        contents (Union[None, Unset, str]):
        file_name (Union[Unset, str]):
        dear_student (Union[Unset, bool]):  Default: True.
        hide_checker_name (Union[Unset, bool]):
        segel_only (Union[Unset, bool]):
    """

    id: int
    user: int
    date: datetime.datetime
    response_type: HelpResponseTypeEnum
    contents: Union[None, Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    dear_student: Union[Unset, bool] = True
    hide_checker_name: Union[Unset, bool] = UNSET
    segel_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user

        date = self.date.isoformat()

        response_type = self.response_type.value

        contents: Union[None, Unset, str]
        if isinstance(self.contents, Unset):
            contents = UNSET
        else:
            contents = self.contents

        file_name = self.file_name

        dear_student = self.dear_student

        hide_checker_name = self.hide_checker_name

        segel_only = self.segel_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "date": date,
                "response_type": response_type,
            }
        )
        if contents is not UNSET:
            field_dict["contents"] = contents
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if dear_student is not UNSET:
            field_dict["dear_student"] = dear_student
        if hide_checker_name is not UNSET:
            field_dict["hide_checker_name"] = hide_checker_name
        if segel_only is not UNSET:
            field_dict["segel_only"] = segel_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user = d.pop("user")

        date = isoparse(d.pop("date"))

        response_type = HelpResponseTypeEnum(d.pop("response_type"))

        def _parse_contents(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contents = _parse_contents(d.pop("contents", UNSET))

        file_name = d.pop("file_name", UNSET)

        dear_student = d.pop("dear_student", UNSET)

        hide_checker_name = d.pop("hide_checker_name", UNSET)

        segel_only = d.pop("segel_only", UNSET)

        help_response_segel_nested = cls(
            id=id,
            user=user,
            date=date,
            response_type=response_type,
            contents=contents,
            file_name=file_name,
            dear_student=dear_student,
            hide_checker_name=hide_checker_name,
            segel_only=segel_only,
        )

        help_response_segel_nested.additional_properties = d
        return help_response_segel_nested

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
