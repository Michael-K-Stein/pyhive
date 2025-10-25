from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.course_exercises_list_tags_id_in_error_component_attr import CourseExercisesListTagsIdInErrorComponentAttr
from ..models.course_exercises_list_tags_id_in_error_component_code import CourseExercisesListTagsIdInErrorComponentCode

T = TypeVar("T", bound="CourseExercisesListTagsIdInErrorComponent")


@_attrs_define
class CourseExercisesListTagsIdInErrorComponent:
    """
    Attributes:
        attr (CourseExercisesListTagsIdInErrorComponentAttr): * `tags__id__in` - tags__id__in
        code (CourseExercisesListTagsIdInErrorComponentCode): * `invalid_choice` - invalid_choice
            * `invalid_list` - invalid_list
            * `invalid_pk_value` - invalid_pk_value
        detail (str):
    """

    attr: CourseExercisesListTagsIdInErrorComponentAttr
    code: CourseExercisesListTagsIdInErrorComponentCode
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
        attr = CourseExercisesListTagsIdInErrorComponentAttr(d.pop("attr"))

        code = CourseExercisesListTagsIdInErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        course_exercises_list_tags_id_in_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        course_exercises_list_tags_id_in_error_component.additional_properties = d
        return course_exercises_list_tags_id_in_error_component

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
