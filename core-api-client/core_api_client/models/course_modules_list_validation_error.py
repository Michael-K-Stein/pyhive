from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_modules_list_parent_subject_id_error_component import (
        CourseModulesListParentSubjectIdErrorComponent,
    )
    from ..models.course_modules_list_parent_subject_parent_program_id_in_error_component import (
        CourseModulesListParentSubjectParentProgramIdInErrorComponent,
    )


T = TypeVar("T", bound="CourseModulesListValidationError")


@_attrs_define
class CourseModulesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseModulesListParentSubjectIdErrorComponent',
            'CourseModulesListParentSubjectParentProgramIdInErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseModulesListParentSubjectIdErrorComponent",
            "CourseModulesListParentSubjectParentProgramIdInErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_modules_list_parent_subject_id_error_component import (
            CourseModulesListParentSubjectIdErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseModulesListParentSubjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
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
        from ..models.course_modules_list_parent_subject_id_error_component import (
            CourseModulesListParentSubjectIdErrorComponent,
        )
        from ..models.course_modules_list_parent_subject_parent_program_id_in_error_component import (
            CourseModulesListParentSubjectParentProgramIdInErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseModulesListParentSubjectIdErrorComponent",
                "CourseModulesListParentSubjectParentProgramIdInErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_modules_list_error_type_0 = (
                        CourseModulesListParentSubjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_modules_list_error_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_modules_list_error_type_1 = (
                    CourseModulesListParentSubjectParentProgramIdInErrorComponent.from_dict(data)
                )

                return componentsschemas_course_modules_list_error_type_1

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_modules_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_modules_list_validation_error.additional_properties = d
        return course_modules_list_validation_error

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
