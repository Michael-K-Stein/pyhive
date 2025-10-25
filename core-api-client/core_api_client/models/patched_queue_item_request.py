from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.queue_rule_enum import QueueRuleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedQueueItemRequest")


@_attrs_define
class PatchedQueueItemRequest:
    """
    Attributes:
        order (Union[Unset, int]):
        set_exercise_id (Union[None, Unset, int]):
        set_nested_queue_id (Union[None, Unset, int]):
        set_module_id (Union[None, Unset, int]):
        queue_rule (Union[Unset, QueueRuleEnum]): * `Choose` - Choose
            * `Wait For Submitted` - Wait For Submitted
            * `Wait For AutoChecks` - Wait For AutoChecks
            * `Wait For Done` - Wait For Done
        continue_on_redo (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        set_tags_id (Union[Unset, list[Union[None, int]]]):
    """

    order: Union[Unset, int] = UNSET
    set_exercise_id: Union[None, Unset, int] = UNSET
    set_nested_queue_id: Union[None, Unset, int] = UNSET
    set_module_id: Union[None, Unset, int] = UNSET
    queue_rule: Union[Unset, QueueRuleEnum] = UNSET
    continue_on_redo: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    set_tags_id: Union[Unset, list[Union[None, int]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        set_exercise_id: Union[None, Unset, int]
        if isinstance(self.set_exercise_id, Unset):
            set_exercise_id = UNSET
        else:
            set_exercise_id = self.set_exercise_id

        set_nested_queue_id: Union[None, Unset, int]
        if isinstance(self.set_nested_queue_id, Unset):
            set_nested_queue_id = UNSET
        else:
            set_nested_queue_id = self.set_nested_queue_id

        set_module_id: Union[None, Unset, int]
        if isinstance(self.set_module_id, Unset):
            set_module_id = UNSET
        else:
            set_module_id = self.set_module_id

        queue_rule: Union[Unset, str] = UNSET
        if not isinstance(self.queue_rule, Unset):
            queue_rule = self.queue_rule.value

        continue_on_redo = self.continue_on_redo

        enabled = self.enabled

        set_tags_id: Union[Unset, list[Union[None, int]]] = UNSET
        if not isinstance(self.set_tags_id, Unset):
            set_tags_id = []
            for set_tags_id_item_data in self.set_tags_id:
                set_tags_id_item: Union[None, int]
                set_tags_id_item = set_tags_id_item_data
                set_tags_id.append(set_tags_id_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if set_exercise_id is not UNSET:
            field_dict["set_exercise_id"] = set_exercise_id
        if set_nested_queue_id is not UNSET:
            field_dict["set_nested_queue_id"] = set_nested_queue_id
        if set_module_id is not UNSET:
            field_dict["set_module_id"] = set_module_id
        if queue_rule is not UNSET:
            field_dict["queue_rule"] = queue_rule
        if continue_on_redo is not UNSET:
            field_dict["continue_on_redo"] = continue_on_redo
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if set_tags_id is not UNSET:
            field_dict["set_tags_id"] = set_tags_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.order, Unset):
            files.append(("order", (None, str(self.order).encode(), "text/plain")))

        if not isinstance(self.set_exercise_id, Unset):
            if isinstance(self.set_exercise_id, int):
                files.append(("set_exercise_id", (None, str(self.set_exercise_id).encode(), "text/plain")))
            else:
                files.append(("set_exercise_id", (None, str(self.set_exercise_id).encode(), "text/plain")))

        if not isinstance(self.set_nested_queue_id, Unset):
            if isinstance(self.set_nested_queue_id, int):
                files.append(("set_nested_queue_id", (None, str(self.set_nested_queue_id).encode(), "text/plain")))
            else:
                files.append(("set_nested_queue_id", (None, str(self.set_nested_queue_id).encode(), "text/plain")))

        if not isinstance(self.set_module_id, Unset):
            if isinstance(self.set_module_id, int):
                files.append(("set_module_id", (None, str(self.set_module_id).encode(), "text/plain")))
            else:
                files.append(("set_module_id", (None, str(self.set_module_id).encode(), "text/plain")))

        if not isinstance(self.queue_rule, Unset):
            files.append(("queue_rule", (None, str(self.queue_rule.value).encode(), "text/plain")))

        if not isinstance(self.continue_on_redo, Unset):
            files.append(("continue_on_redo", (None, str(self.continue_on_redo).encode(), "text/plain")))

        if not isinstance(self.enabled, Unset):
            files.append(("enabled", (None, str(self.enabled).encode(), "text/plain")))

        if not isinstance(self.set_tags_id, Unset):
            for set_tags_id_item_element in self.set_tags_id:
                if isinstance(set_tags_id_item_element, int):
                    files.append(("set_tags_id", (None, str(set_tags_id_item_element).encode(), "text/plain")))
                else:
                    files.append(("set_tags_id", (None, str(set_tags_id_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order = d.pop("order", UNSET)

        def _parse_set_exercise_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        set_exercise_id = _parse_set_exercise_id(d.pop("set_exercise_id", UNSET))

        def _parse_set_nested_queue_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        set_nested_queue_id = _parse_set_nested_queue_id(d.pop("set_nested_queue_id", UNSET))

        def _parse_set_module_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        set_module_id = _parse_set_module_id(d.pop("set_module_id", UNSET))

        _queue_rule = d.pop("queue_rule", UNSET)
        queue_rule: Union[Unset, QueueRuleEnum]
        if isinstance(_queue_rule, Unset):
            queue_rule = UNSET
        else:
            queue_rule = QueueRuleEnum(_queue_rule)

        continue_on_redo = d.pop("continue_on_redo", UNSET)

        enabled = d.pop("enabled", UNSET)

        set_tags_id = []
        _set_tags_id = d.pop("set_tags_id", UNSET)
        for set_tags_id_item_data in _set_tags_id or []:

            def _parse_set_tags_id_item(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

            set_tags_id_item = _parse_set_tags_id_item(set_tags_id_item_data)

            set_tags_id.append(set_tags_id_item)

        patched_queue_item_request = cls(
            order=order,
            set_exercise_id=set_exercise_id,
            set_nested_queue_id=set_nested_queue_id,
            set_module_id=set_module_id,
            queue_rule=queue_rule,
            continue_on_redo=continue_on_redo,
            enabled=enabled,
            set_tags_id=set_tags_id,
        )

        patched_queue_item_request.additional_properties = d
        return patched_queue_item_request

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
