import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.assignment_response_type_enum import AssignmentResponseTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignment_response_content import AssignmentResponseContent
    from ..models.status import Status


T = TypeVar("T", bound="AssignmentResponse")


@_attrs_define
class AssignmentResponse:
    """
    Attributes:
        id (int):
        user (int):
        contents (list['AssignmentResponseContent']):
        date (datetime.datetime):
        response_type (AssignmentResponseTypeEnum):
            * `Comment` - Comment
            * `Work In Progress` - Workinprogress
            * `Submission` - Submission
            * `AutoCheck` - Autocheck
            * `Redo` - Redo
            * `Done` - Done
        autocheck_statuses (Union[None, list['Status']]):
        file_name (Union[Unset, str]):
        dear_student (Union[Unset, bool]):  Default: True.
        hide_checker_name (Union[Unset, bool]):
        segel_only (Union[Unset, bool]):
    """

    id: int
    user: int
    contents: list["AssignmentResponseContent"]
    date: datetime.datetime
    response_type: AssignmentResponseTypeEnum
    autocheck_statuses: Union[None, list["Status"]]
    file_name: Union[Unset, str] = UNSET
    dear_student: Union[Unset, bool] = True
    hide_checker_name: Union[Unset, bool] = UNSET
    segel_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user

        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()
            contents.append(contents_item)

        date = self.date.isoformat()

        response_type = self.response_type.value

        autocheck_statuses: Union[None, list[dict[str, Any]]]
        if isinstance(self.autocheck_statuses, list):
            autocheck_statuses = []
            for autocheck_statuses_type_0_item_data in self.autocheck_statuses:
                autocheck_statuses_type_0_item = autocheck_statuses_type_0_item_data.to_dict()
                autocheck_statuses.append(autocheck_statuses_type_0_item)

        else:
            autocheck_statuses = self.autocheck_statuses

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
                "contents": contents,
                "date": date,
                "response_type": response_type,
                "autocheck_statuses": autocheck_statuses,
            }
        )
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
        from ..models.assignment_response_content import AssignmentResponseContent
        from ..models.status import Status

        d = dict(src_dict)
        id = d.pop("id")

        user = d.pop("user")

        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:
            contents_item = AssignmentResponseContent.from_dict(contents_item_data)

            contents.append(contents_item)

        date = isoparse(d.pop("date"))

        response_type = AssignmentResponseTypeEnum(d.pop("response_type"))

        def _parse_autocheck_statuses(data: object) -> Union[None, list["Status"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                autocheck_statuses_type_0 = []
                _autocheck_statuses_type_0 = data
                for autocheck_statuses_type_0_item_data in _autocheck_statuses_type_0:
                    autocheck_statuses_type_0_item = Status.from_dict(autocheck_statuses_type_0_item_data)

                    autocheck_statuses_type_0.append(autocheck_statuses_type_0_item)

                return autocheck_statuses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["Status"]], data)

        autocheck_statuses = _parse_autocheck_statuses(d.pop("autocheck_statuses"))

        file_name = d.pop("file_name", UNSET)

        dear_student = d.pop("dear_student", UNSET)

        hide_checker_name = d.pop("hide_checker_name", UNSET)

        segel_only = d.pop("segel_only", UNSET)

        assignment_response = cls(
            id=id,
            user=user,
            contents=contents,
            date=date,
            response_type=response_type,
            autocheck_statuses=autocheck_statuses,
            file_name=file_name,
            dear_student=dear_student,
            hide_checker_name=hide_checker_name,
            segel_only=segel_only,
        )

        assignment_response.additional_properties = d
        return assignment_response

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
