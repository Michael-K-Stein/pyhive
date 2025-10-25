from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_notify_students_create_contents_index_content_error_component import (
        CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_contents_index_field_error_component import (
        CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_contents_index_non_field_errors_error_component import (
        CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_contents_non_field_errors_error_component import (
        CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_dear_student_error_component import (
        CourseExercisesNotifyStudentsCreateDearStudentErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_file_error_component import (
        CourseExercisesNotifyStudentsCreateFileErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_file_name_error_component import (
        CourseExercisesNotifyStudentsCreateFileNameErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_hide_checker_name_error_component import (
        CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_non_field_errors_error_component import (
        CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_response_type_error_component import (
        CourseExercisesNotifyStudentsCreateResponseTypeErrorComponent,
    )
    from ..models.course_exercises_notify_students_create_segel_only_error_component import (
        CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent,
    )


T = TypeVar("T", bound="CourseExercisesNotifyStudentsCreateValidationError")


@_attrs_define
class CourseExercisesNotifyStudentsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent',
            'CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent',
            'CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent',
            'CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent',
            'CourseExercisesNotifyStudentsCreateDearStudentErrorComponent',
            'CourseExercisesNotifyStudentsCreateFileErrorComponent',
            'CourseExercisesNotifyStudentsCreateFileNameErrorComponent',
            'CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent',
            'CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent',
            'CourseExercisesNotifyStudentsCreateResponseTypeErrorComponent',
            'CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent",
            "CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent",
            "CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent",
            "CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent",
            "CourseExercisesNotifyStudentsCreateDearStudentErrorComponent",
            "CourseExercisesNotifyStudentsCreateFileErrorComponent",
            "CourseExercisesNotifyStudentsCreateFileNameErrorComponent",
            "CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent",
            "CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent",
            "CourseExercisesNotifyStudentsCreateResponseTypeErrorComponent",
            "CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_notify_students_create_contents_index_content_error_component import (
            CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_contents_index_field_error_component import (
            CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_contents_index_non_field_errors_error_component import (
            CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_contents_non_field_errors_error_component import (
            CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_dear_student_error_component import (
            CourseExercisesNotifyStudentsCreateDearStudentErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_file_error_component import (
            CourseExercisesNotifyStudentsCreateFileErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_file_name_error_component import (
            CourseExercisesNotifyStudentsCreateFileNameErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_hide_checker_name_error_component import (
            CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_non_field_errors_error_component import (
            CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_segel_only_error_component import (
            CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent):
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
        from ..models.course_exercises_notify_students_create_contents_index_content_error_component import (
            CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_contents_index_field_error_component import (
            CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_contents_index_non_field_errors_error_component import (
            CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_contents_non_field_errors_error_component import (
            CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_dear_student_error_component import (
            CourseExercisesNotifyStudentsCreateDearStudentErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_file_error_component import (
            CourseExercisesNotifyStudentsCreateFileErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_file_name_error_component import (
            CourseExercisesNotifyStudentsCreateFileNameErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_hide_checker_name_error_component import (
            CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_non_field_errors_error_component import (
            CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_response_type_error_component import (
            CourseExercisesNotifyStudentsCreateResponseTypeErrorComponent,
        )
        from ..models.course_exercises_notify_students_create_segel_only_error_component import (
            CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent",
                "CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent",
                "CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent",
                "CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent",
                "CourseExercisesNotifyStudentsCreateDearStudentErrorComponent",
                "CourseExercisesNotifyStudentsCreateFileErrorComponent",
                "CourseExercisesNotifyStudentsCreateFileNameErrorComponent",
                "CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent",
                "CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent",
                "CourseExercisesNotifyStudentsCreateResponseTypeErrorComponent",
                "CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_0 = (
                        CourseExercisesNotifyStudentsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_1 = (
                        CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_2 = (
                        CourseExercisesNotifyStudentsCreateContentsINDEXNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_3 = (
                        CourseExercisesNotifyStudentsCreateContentsINDEXContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_4 = (
                        CourseExercisesNotifyStudentsCreateContentsINDEXFieldErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_5 = (
                        CourseExercisesNotifyStudentsCreateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_6 = (
                        CourseExercisesNotifyStudentsCreateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_7 = (
                        CourseExercisesNotifyStudentsCreateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_8 = (
                        CourseExercisesNotifyStudentsCreateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_notify_students_create_error_type_9 = (
                        CourseExercisesNotifyStudentsCreateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_notify_students_create_error_type_9
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_notify_students_create_error_type_10 = (
                    CourseExercisesNotifyStudentsCreateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_notify_students_create_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_notify_students_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_notify_students_create_validation_error.additional_properties = d
        return course_exercises_notify_students_create_validation_error

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
