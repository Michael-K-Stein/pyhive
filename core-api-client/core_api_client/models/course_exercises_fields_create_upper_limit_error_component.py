from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.course_exercises_fields_create_upper_limit_error_component_attr import (
    CourseExercisesFieldsCreateUpperLimitErrorComponentAttr,
)
from ..models.course_exercises_fields_create_upper_limit_error_component_code import (
    CourseExercisesFieldsCreateUpperLimitErrorComponentCode,
)

T = TypeVar("T", bound="CourseExercisesFieldsCreateUpperLimitErrorComponent")


@_attrs_define
class CourseExercisesFieldsCreateUpperLimitErrorComponent:
    """
    Attributes:
        attr (CourseExercisesFieldsCreateUpperLimitErrorComponentAttr): * `upper_limit` - upper_limit
        code (CourseExercisesFieldsCreateUpperLimitErrorComponentCode): * `invalid` - invalid
            * `max_string_length` - max_string_length
            * `max_value` - max_value
            * `min_value` - min_value
        detail (str):
    """

    attr: CourseExercisesFieldsCreateUpperLimitErrorComponentAttr
    code: CourseExercisesFieldsCreateUpperLimitErrorComponentCode
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
        attr = CourseExercisesFieldsCreateUpperLimitErrorComponentAttr(d.pop("attr"))

        code = CourseExercisesFieldsCreateUpperLimitErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        course_exercises_fields_create_upper_limit_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        course_exercises_fields_create_upper_limit_error_component.additional_properties = d
        return course_exercises_fields_create_upper_limit_error_component

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
