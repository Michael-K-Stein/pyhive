from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="SetQueueRequest")


@_attrs_define
class SetQueueRequest:
    """
    Attributes:
        queue (Union[None, int]):
    """

    queue: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue: Union[None, int]
        queue = self.queue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue": queue,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

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

        def _parse_queue(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        queue = _parse_queue(d.pop("queue"))

        set_queue_request = cls(
            queue=queue,
        )

        set_queue_request.additional_properties = d
        return set_queue_request

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
