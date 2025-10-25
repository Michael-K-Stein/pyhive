from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_subjects_list_parent_program_id_in_error_component import (
        CourseSubjectsListParentProgramIdInErrorComponent,
    )


T = TypeVar("T", bound="CourseSubjectsListValidationError")


@_attrs_define
class CourseSubjectsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list['CourseSubjectsListParentProgramIdInErrorComponent']):
    """

    type_: ValidationErrorEnum
    errors: list["CourseSubjectsListParentProgramIdInErrorComponent"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_subjects_list_parent_program_id_in_error_component import (
            CourseSubjectsListParentProgramIdInErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = CourseSubjectsListParentProgramIdInErrorComponent.from_dict(errors_item_data)

            errors.append(errors_item)

        course_subjects_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_subjects_list_validation_error.additional_properties = d
        return course_subjects_list_validation_error

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
