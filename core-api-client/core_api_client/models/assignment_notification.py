from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignmentNotification")


@_attrs_define
class AssignmentNotification:
    """
    Attributes:
        id (int):
        user (int):
        user_name (str):
        exercise (int):
        module (int):
        subject (int):
    """

    id: int
    user: int
    user_name: str
    exercise: int
    module: int
    subject: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user

        user_name = self.user_name

        exercise = self.exercise

        module = self.module

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "user_name": user_name,
                "exercise": exercise,
                "module": module,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user = d.pop("user")

        user_name = d.pop("user_name")

        exercise = d.pop("exercise")

        module = d.pop("module")

        subject = d.pop("subject")

        assignment_notification = cls(
            id=id,
            user=user,
            user_name=user_name,
            exercise=exercise,
            module=module,
            subject=subject,
        )

        assignment_notification.additional_properties = d
        return assignment_notification

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
