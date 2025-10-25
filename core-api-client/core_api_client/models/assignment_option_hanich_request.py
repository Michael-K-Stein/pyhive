from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignment_status_enum import AssignmentStatusEnum

T = TypeVar("T", bound="AssignmentOptionHanichRequest")


@_attrs_define
class AssignmentOptionHanichRequest:
    """
    Attributes:
        exercise (int):
        assignment_status (AssignmentStatusEnum):
            * `New` - New
            * `Work In Progress` - Work In Progress
            * `Redo` - Redo
            * `Submitted` - Submitted
            * `AutoChecked` - AutoChecked
            * `Done` - Done
    """

    exercise: int
    assignment_status: AssignmentStatusEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise = self.exercise

        assignment_status = self.assignment_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exercise": exercise,
                "assignment_status": assignment_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exercise = d.pop("exercise")

        assignment_status = AssignmentStatusEnum(d.pop("assignment_status"))

        assignment_option_hanich_request = cls(
            exercise=exercise,
            assignment_status=assignment_status,
        )

        assignment_option_hanich_request.additional_properties = d
        return assignment_option_hanich_request

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
