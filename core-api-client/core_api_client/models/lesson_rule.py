from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.class_ import Class
    from ..models.queue import Queue


T = TypeVar("T", bound="LessonRule")


@_attrs_define
class LessonRule:
    """
    Attributes:
        id (int):
        queue_data (Union['Queue', None]):
        student_groups_data (Union[None, list['Class']]):
        parent_rule (Union[None, Unset, int]):
        student_groups (Union[Unset, list[int]]):
        queue (Union[None, Unset, int]):
    """

    id: int
    queue_data: Union["Queue", None]
    student_groups_data: Union[None, list["Class"]]
    parent_rule: Union[None, Unset, int] = UNSET
    student_groups: Union[Unset, list[int]] = UNSET
    queue: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.queue import Queue

        id = self.id

        queue_data: Union[None, dict[str, Any]]
        if isinstance(self.queue_data, Queue):
            queue_data = self.queue_data.to_dict()
        else:
            queue_data = self.queue_data

        student_groups_data: Union[None, list[dict[str, Any]]]
        if isinstance(self.student_groups_data, list):
            student_groups_data = []
            for student_groups_data_type_0_item_data in self.student_groups_data:
                student_groups_data_type_0_item = student_groups_data_type_0_item_data.to_dict()
                student_groups_data.append(student_groups_data_type_0_item)

        else:
            student_groups_data = self.student_groups_data

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
        field_dict.update(
            {
                "id": id,
                "queue_data": queue_data,
                "student_groups_data": student_groups_data,
            }
        )
        if parent_rule is not UNSET:
            field_dict["parent_rule"] = parent_rule
        if student_groups is not UNSET:
            field_dict["student_groups"] = student_groups
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.class_ import Class
        from ..models.queue import Queue

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_queue_data(data: object) -> Union["Queue", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                queue_data_type_1 = Queue.from_dict(data)

                return queue_data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Queue", None], data)

        queue_data = _parse_queue_data(d.pop("queue_data"))

        def _parse_student_groups_data(data: object) -> Union[None, list["Class"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                student_groups_data_type_0 = []
                _student_groups_data_type_0 = data
                for student_groups_data_type_0_item_data in _student_groups_data_type_0:
                    student_groups_data_type_0_item = Class.from_dict(student_groups_data_type_0_item_data)

                    student_groups_data_type_0.append(student_groups_data_type_0_item)

                return student_groups_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["Class"]], data)

        student_groups_data = _parse_student_groups_data(d.pop("student_groups_data"))

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

        lesson_rule = cls(
            id=id,
            queue_data=queue_data,
            student_groups_data=student_groups_data,
            parent_rule=parent_rule,
            student_groups=student_groups,
            queue=queue,
        )

        lesson_rule.additional_properties = d
        return lesson_rule

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
