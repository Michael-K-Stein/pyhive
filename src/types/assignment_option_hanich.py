from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignment_status_enum import AssignmentStatusEnum

T = TypeVar("T", bound="AssignmentOptionHanich")


@_attrs_define
class AssignmentOptionHanich:
    """
    Attributes:
        id (int):
        exercise (int):
        exercise_name (str):
        parent_module (int):
        parent_subject (int):
        parent_module_name (str):
        parent_subject_symbol (str):
        parent_subject_color (str):
        assignment_status (AssignmentStatusEnum):
            * `New` - New
            * `Work In Progress` - Work In Progress
            * `Redo` - Redo
            * `Submitted` - Submitted
            * `AutoChecked` - AutoChecked
            * `Done` - Done
    """

    hive_client: "HiveClient"
    id: int
    exercise: int
    exercise_name: str
    parent_module: int
    parent_subject: int
    parent_module_name: str
    parent_subject_symbol: str
    parent_subject_color: str
    assignment_status: AssignmentStatusEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        exercise = self.exercise

        exercise_name = self.exercise_name

        parent_module = self.parent_module

        parent_subject = self.parent_subject

        parent_module_name = self.parent_module_name

        parent_subject_symbol = self.parent_subject_symbol

        parent_subject_color = self.parent_subject_color

        assignment_status = self.assignment_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "exercise": exercise,
                "exercise_name": exercise_name,
                "parent_module": parent_module,
                "parent_subject": parent_subject,
                "parent_module_name": parent_module_name,
                "parent_subject_symbol": parent_subject_symbol,
                "parent_subject_color": parent_subject_color,
                "assignment_status": assignment_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        exercise = d.pop("exercise")

        exercise_name = d.pop("exercise_name")

        parent_module = d.pop("parent_module")

        parent_subject = d.pop("parent_subject")

        parent_module_name = d.pop("parent_module_name")

        parent_subject_symbol = d.pop("parent_subject_symbol")

        parent_subject_color = d.pop("parent_subject_color")

        assignment_status = AssignmentStatusEnum(d.pop("assignment_status"))

        assignment_option_hanich = cls(
            hive_client=hive_client,
            id=id,
            exercise=exercise,
            exercise_name=exercise_name,
            parent_module=parent_module,
            parent_subject=parent_subject,
            parent_module_name=parent_module_name,
            parent_subject_symbol=parent_subject_symbol,
            parent_subject_color=parent_subject_color,
            assignment_status=assignment_status,
        )

        assignment_option_hanich.additional_properties = d
        return assignment_option_hanich

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
