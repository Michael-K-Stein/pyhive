from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLessonRuleRequest")


@_attrs_define
class PatchedLessonRuleRequest:
    """
    Attributes:
        parent_rule (Union[None, Unset, int]):
        student_groups (Union[Unset, list[int]]):
        queue (Union[None, Unset, int]):
    """

    parent_rule: Union[None, Unset, int] = UNSET
    student_groups: Union[Unset, list[int]] = UNSET
    queue: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_rule: Union[None, Unset, int]
        if isinstance(self.parent_rule, Unset):
            parent_rule = UNSET
        else:
            parent_rule = self.parent_rule

        student_groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.student_groups, Unset):
            student_groups = self.student_groups

        queue: Union[None, Unset, int]
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_rule is not UNSET:
            field_dict["parent_rule"] = parent_rule
        if student_groups is not UNSET:
            field_dict["student_groups"] = student_groups
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.parent_rule, Unset):
            if isinstance(self.parent_rule, int):
                files.append(("parent_rule", (None, str(self.parent_rule).encode(), "text/plain")))
            else:
                files.append(("parent_rule", (None, str(self.parent_rule).encode(), "text/plain")))

        if not isinstance(self.student_groups, Unset):
            for student_groups_item_element in self.student_groups:
                files.append(("student_groups", (None, str(student_groups_item_element).encode(), "text/plain")))

        if not isinstance(self.queue, Unset):
            if isinstance(self.queue, int):
                files.append(("queue", (None, str(self.queue).encode(), "text/plain")))
            else:
                files.append(("queue", (None, str(self.queue).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_parent_rule(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_rule = _parse_parent_rule(d.pop("parent_rule", UNSET))

        student_groups = cast(list[int], d.pop("student_groups", UNSET))

        def _parse_queue(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        queue = _parse_queue(d.pop("queue", UNSET))

        patched_lesson_rule_request = cls(
            parent_rule=parent_rule,
            student_groups=student_groups,
            queue=queue,
        )

        patched_lesson_rule_request.additional_properties = d
        return patched_lesson_rule_request

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
