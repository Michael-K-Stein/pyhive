from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queue_rule_enum import QueueRuleEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise import Exercise
    from ..models.queue import Queue


T = TypeVar("T", bound="QueueItem")


@_attrs_define
class QueueItem:
    """
    Attributes:
        id (int):
        order (int):
        exercise (Union['Exercise', None]):
        nested_queue (Union['Queue', None]):
        queue_rule (QueueRuleEnum):
            * `Choose` - Choose
            * `Wait For Submitted` - Wait For Submitted
            * `Wait For AutoChecks` - Wait For AutoChecks
            * `Wait For Done` - Wait For Done
        enabled (bool):
        continue_on_redo (Union[Unset, bool]):
    """

    id: int
    order: int
    exercise: Union["Exercise", None]
    nested_queue: Union["Queue", None]
    queue_rule: QueueRuleEnum
    enabled: bool
    continue_on_redo: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exercise import Exercise
        from ..models.queue import Queue

        id = self.id

        order = self.order

        exercise: Union[None, dict[str, Any]]
        if isinstance(self.exercise, Exercise):
            exercise = self.exercise.to_dict()
        else:
            exercise = self.exercise

        nested_queue: Union[None, dict[str, Any]]
        if isinstance(self.nested_queue, Queue):
            nested_queue = self.nested_queue.to_dict()
        else:
            nested_queue = self.nested_queue

        queue_rule = self.queue_rule.value

        enabled = self.enabled

        continue_on_redo = self.continue_on_redo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order": order,
                "exercise": exercise,
                "nested_queue": nested_queue,
                "queue_rule": queue_rule,
                "enabled": enabled,
            }
        )
        if continue_on_redo is not UNSET:
            field_dict["continue_on_redo"] = continue_on_redo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise import Exercise
        from ..models.queue import Queue

        d = dict(src_dict)
        id = d.pop("id")

        order = d.pop("order")

        def _parse_exercise(data: object) -> Union["Exercise", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exercise_type_1 = Exercise.from_dict(data)

                return exercise_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Exercise", None], data)

        exercise = _parse_exercise(d.pop("exercise"))

        def _parse_nested_queue(data: object) -> Union["Queue", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nested_queue_type_1 = Queue.from_dict(data)

                return nested_queue_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Queue", None], data)

        nested_queue = _parse_nested_queue(d.pop("nested_queue"))

        queue_rule = QueueRuleEnum(d.pop("queue_rule"))

        enabled = d.pop("enabled")

        continue_on_redo = d.pop("continue_on_redo", UNSET)

        queue_item = cls(
            id=id,
            order=order,
            exercise=exercise,
            nested_queue=nested_queue,
            queue_rule=queue_rule,
            enabled=enabled,
            continue_on_redo=continue_on_redo,
        )

        queue_item.additional_properties = d
        return queue_item

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
