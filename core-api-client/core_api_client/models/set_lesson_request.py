from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="SetLessonRequest")


@_attrs_define
class SetLessonRequest:
    """
    Attributes:
        lesson (Union[None, int]):
    """

    lesson: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lesson: Union[None, int]
        lesson = self.lesson

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lesson": lesson,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if isinstance(self.lesson, int):
            files.append(("lesson", (None, str(self.lesson).encode(), "text/plain")))
        else:
            files.append(("lesson", (None, str(self.lesson).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lesson(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        lesson = _parse_lesson(d.pop("lesson"))

        set_lesson_request = cls(
            lesson=lesson,
        )

        set_lesson_request.additional_properties = d
        return set_lesson_request

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
