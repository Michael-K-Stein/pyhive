from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_colors_update_color_error_component_attr import ScheduleColorsUpdateColorErrorComponentAttr
from ..models.schedule_colors_update_color_error_component_code import ScheduleColorsUpdateColorErrorComponentCode

T = TypeVar("T", bound="ScheduleColorsUpdateColorErrorComponent")


@_attrs_define
class ScheduleColorsUpdateColorErrorComponent:
    """
    Attributes:
        attr (ScheduleColorsUpdateColorErrorComponentAttr): * `color` - color
        code (ScheduleColorsUpdateColorErrorComponentCode): * `blank` - blank
            * `invalid` - invalid
            * `max_length` - max_length
            * `null` - null
            * `null_characters_not_allowed` - null_characters_not_allowed
            * `required` - required
            * `surrogate_characters_not_allowed` - surrogate_characters_not_allowed
        detail (str):
    """

    attr: ScheduleColorsUpdateColorErrorComponentAttr
    code: ScheduleColorsUpdateColorErrorComponentCode
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attr = self.attr.value

        code = self.code.value

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attr": attr,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attr = ScheduleColorsUpdateColorErrorComponentAttr(d.pop("attr"))

        code = ScheduleColorsUpdateColorErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        schedule_colors_update_color_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        schedule_colors_update_color_error_component.additional_properties = d
        return schedule_colors_update_color_error_component

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
