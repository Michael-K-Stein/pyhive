from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.assignment_status_enum import AssignmentStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAssignmentRequest")


@_attrs_define
class PatchedAssignmentRequest:
    """
    Attributes:
        assignment_status (Union[Unset, AssignmentStatusEnum]): * `New` - New
            * `Work In Progress` - Work In Progress
            * `Redo` - Redo
            * `Submitted` - Submitted
            * `AutoChecked` - AutoChecked
            * `Done` - Done
        student_assignment_status (Union[Unset, AssignmentStatusEnum]): * `New` - New
            * `Work In Progress` - Work In Progress
            * `Redo` - Redo
            * `Submitted` - Submitted
            * `AutoChecked` - AutoChecked
            * `Done` - Done
        description (Union[None, Unset, str]):
        submission_count (Union[Unset, int]):
        total_check_count (Union[Unset, int]):
        manual_check_count (Union[Unset, int]):
        flagged (Union[Unset, bool]):
        timer (Union[None, Unset, str]):
    """

    assignment_status: Union[Unset, AssignmentStatusEnum] = UNSET
    student_assignment_status: Union[Unset, AssignmentStatusEnum] = UNSET
    description: Union[None, Unset, str] = UNSET
    submission_count: Union[Unset, int] = UNSET
    total_check_count: Union[Unset, int] = UNSET
    manual_check_count: Union[Unset, int] = UNSET
    flagged: Union[Unset, bool] = UNSET
    timer: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_status: Union[Unset, str] = UNSET
        if not isinstance(self.assignment_status, Unset):
            assignment_status = self.assignment_status.value

        student_assignment_status: Union[Unset, str] = UNSET
        if not isinstance(self.student_assignment_status, Unset):
            student_assignment_status = self.student_assignment_status.value

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        submission_count = self.submission_count

        total_check_count = self.total_check_count

        manual_check_count = self.manual_check_count

        flagged = self.flagged

        timer: Union[None, Unset, str]
        if isinstance(self.timer, Unset):
            timer = UNSET
        else:
            timer = self.timer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignment_status is not UNSET:
            field_dict["assignment_status"] = assignment_status
        if student_assignment_status is not UNSET:
            field_dict["student_assignment_status"] = student_assignment_status
        if description is not UNSET:
            field_dict["description"] = description
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count
        if total_check_count is not UNSET:
            field_dict["total_check_count"] = total_check_count
        if manual_check_count is not UNSET:
            field_dict["manual_check_count"] = manual_check_count
        if flagged is not UNSET:
            field_dict["flagged"] = flagged
        if timer is not UNSET:
            field_dict["timer"] = timer

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.assignment_status, Unset):
            files.append(("assignment_status", (None, str(self.assignment_status.value).encode(), "text/plain")))

        if not isinstance(self.student_assignment_status, Unset):
            files.append(
                ("student_assignment_status", (None, str(self.student_assignment_status.value).encode(), "text/plain"))
            )

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.submission_count, Unset):
            files.append(("submission_count", (None, str(self.submission_count).encode(), "text/plain")))

        if not isinstance(self.total_check_count, Unset):
            files.append(("total_check_count", (None, str(self.total_check_count).encode(), "text/plain")))

        if not isinstance(self.manual_check_count, Unset):
            files.append(("manual_check_count", (None, str(self.manual_check_count).encode(), "text/plain")))

        if not isinstance(self.flagged, Unset):
            files.append(("flagged", (None, str(self.flagged).encode(), "text/plain")))

        if not isinstance(self.timer, Unset):
            if isinstance(self.timer, str):
                files.append(("timer", (None, str(self.timer).encode(), "text/plain")))
            else:
                files.append(("timer", (None, str(self.timer).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _assignment_status = d.pop("assignment_status", UNSET)
        assignment_status: Union[Unset, AssignmentStatusEnum]
        if isinstance(_assignment_status, Unset):
            assignment_status = UNSET
        else:
            assignment_status = AssignmentStatusEnum(_assignment_status)

        _student_assignment_status = d.pop("student_assignment_status", UNSET)
        student_assignment_status: Union[Unset, AssignmentStatusEnum]
        if isinstance(_student_assignment_status, Unset):
            student_assignment_status = UNSET
        else:
            student_assignment_status = AssignmentStatusEnum(_student_assignment_status)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        submission_count = d.pop("submission_count", UNSET)

        total_check_count = d.pop("total_check_count", UNSET)

        manual_check_count = d.pop("manual_check_count", UNSET)

        flagged = d.pop("flagged", UNSET)

        def _parse_timer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timer = _parse_timer(d.pop("timer", UNSET))

        patched_assignment_request = cls(
            assignment_status=assignment_status,
            student_assignment_status=student_assignment_status,
            description=description,
            submission_count=submission_count,
            total_check_count=total_check_count,
            manual_check_count=manual_check_count,
            flagged=flagged,
            timer=timer,
        )

        patched_assignment_request.additional_properties = d
        return patched_assignment_request

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
