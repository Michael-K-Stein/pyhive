from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_list_id_error_component import CourseExercisesListIdErrorComponent
    from ..models.course_exercises_list_parent_module_id_error_component import (
        CourseExercisesListParentModuleIdErrorComponent,
    )
    from ..models.course_exercises_list_parent_module_parent_subject_id_error_component import (
        CourseExercisesListParentModuleParentSubjectIdErrorComponent,
    )
    from ..models.course_exercises_list_parent_module_parent_subject_parent_program_id_in_error_component import (
        CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent,
    )
    from ..models.course_exercises_list_queue_id_error_component import CourseExercisesListQueueIdErrorComponent
    from ..models.course_exercises_list_tags_id_in_error_component import CourseExercisesListTagsIdInErrorComponent


T = TypeVar("T", bound="CourseExercisesListValidationError")


@_attrs_define
class CourseExercisesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesListIdErrorComponent', 'CourseExercisesListParentModuleIdErrorComponent',
            'CourseExercisesListParentModuleParentSubjectIdErrorComponent',
            'CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent',
            'CourseExercisesListQueueIdErrorComponent', 'CourseExercisesListTagsIdInErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesListIdErrorComponent",
            "CourseExercisesListParentModuleIdErrorComponent",
            "CourseExercisesListParentModuleParentSubjectIdErrorComponent",
            "CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent",
            "CourseExercisesListQueueIdErrorComponent",
            "CourseExercisesListTagsIdInErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_list_id_error_component import CourseExercisesListIdErrorComponent
        from ..models.course_exercises_list_parent_module_id_error_component import (
            CourseExercisesListParentModuleIdErrorComponent,
        )
        from ..models.course_exercises_list_parent_module_parent_subject_id_error_component import (
            CourseExercisesListParentModuleParentSubjectIdErrorComponent,
        )
        from ..models.course_exercises_list_parent_module_parent_subject_parent_program_id_in_error_component import (
            CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent,
        )
        from ..models.course_exercises_list_queue_id_error_component import CourseExercisesListQueueIdErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesListParentModuleIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesListParentModuleParentSubjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesListIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesListQueueIdErrorComponent):
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
        from ..models.course_exercises_list_id_error_component import CourseExercisesListIdErrorComponent
        from ..models.course_exercises_list_parent_module_id_error_component import (
            CourseExercisesListParentModuleIdErrorComponent,
        )
        from ..models.course_exercises_list_parent_module_parent_subject_id_error_component import (
            CourseExercisesListParentModuleParentSubjectIdErrorComponent,
        )
        from ..models.course_exercises_list_parent_module_parent_subject_parent_program_id_in_error_component import (
            CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent,
        )
        from ..models.course_exercises_list_queue_id_error_component import CourseExercisesListQueueIdErrorComponent
        from ..models.course_exercises_list_tags_id_in_error_component import CourseExercisesListTagsIdInErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesListIdErrorComponent",
                "CourseExercisesListParentModuleIdErrorComponent",
                "CourseExercisesListParentModuleParentSubjectIdErrorComponent",
                "CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent",
                "CourseExercisesListQueueIdErrorComponent",
                "CourseExercisesListTagsIdInErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_list_error_type_0 = (
                        CourseExercisesListParentModuleIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_list_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_list_error_type_1 = (
                        CourseExercisesListParentModuleParentSubjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_list_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_list_error_type_2 = (
                        CourseExercisesListParentModuleParentSubjectParentProgramIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_list_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_list_error_type_3 = (
                        CourseExercisesListIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_list_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_list_error_type_4 = (
                        CourseExercisesListQueueIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_list_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_list_error_type_5 = (
                    CourseExercisesListTagsIdInErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_list_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_list_validation_error.additional_properties = d
        return course_exercises_list_validation_error

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
