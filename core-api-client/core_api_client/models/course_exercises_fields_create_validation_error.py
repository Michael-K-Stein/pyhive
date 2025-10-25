from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_fields_create_choices_error_component import (
        CourseExercisesFieldsCreateChoicesErrorComponent,
    )
    from ..models.course_exercises_fields_create_choices_index_error_component import (
        CourseExercisesFieldsCreateChoicesINDEXErrorComponent,
    )
    from ..models.course_exercises_fields_create_description_error_component import (
        CourseExercisesFieldsCreateDescriptionErrorComponent,
    )
    from ..models.course_exercises_fields_create_groups_error_component import (
        CourseExercisesFieldsCreateGroupsErrorComponent,
    )
    from ..models.course_exercises_fields_create_hanich_responses_error_component import (
        CourseExercisesFieldsCreateHanichResponsesErrorComponent,
    )
    from ..models.course_exercises_fields_create_has_value_error_component import (
        CourseExercisesFieldsCreateHasValueErrorComponent,
    )
    from ..models.course_exercises_fields_create_lower_limit_error_component import (
        CourseExercisesFieldsCreateLowerLimitErrorComponent,
    )
    from ..models.course_exercises_fields_create_metadata_error_component import (
        CourseExercisesFieldsCreateMetadataErrorComponent,
    )
    from ..models.course_exercises_fields_create_name_error_component import (
        CourseExercisesFieldsCreateNameErrorComponent,
    )
    from ..models.course_exercises_fields_create_non_field_errors_error_component import (
        CourseExercisesFieldsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_fields_create_order_error_component import (
        CourseExercisesFieldsCreateOrderErrorComponent,
    )
    from ..models.course_exercises_fields_create_required_error_component import (
        CourseExercisesFieldsCreateRequiredErrorComponent,
    )
    from ..models.course_exercises_fields_create_segel_only_error_component import (
        CourseExercisesFieldsCreateSegelOnlyErrorComponent,
    )
    from ..models.course_exercises_fields_create_staff_responses_error_component import (
        CourseExercisesFieldsCreateStaffResponsesErrorComponent,
    )
    from ..models.course_exercises_fields_create_type_error_component import (
        CourseExercisesFieldsCreateTypeErrorComponent,
    )
    from ..models.course_exercises_fields_create_upper_limit_error_component import (
        CourseExercisesFieldsCreateUpperLimitErrorComponent,
    )


T = TypeVar("T", bound="CourseExercisesFieldsCreateValidationError")


@_attrs_define
class CourseExercisesFieldsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesFieldsCreateChoicesErrorComponent',
            'CourseExercisesFieldsCreateChoicesINDEXErrorComponent', 'CourseExercisesFieldsCreateDescriptionErrorComponent',
            'CourseExercisesFieldsCreateGroupsErrorComponent', 'CourseExercisesFieldsCreateHanichResponsesErrorComponent',
            'CourseExercisesFieldsCreateHasValueErrorComponent', 'CourseExercisesFieldsCreateLowerLimitErrorComponent',
            'CourseExercisesFieldsCreateMetadataErrorComponent', 'CourseExercisesFieldsCreateNameErrorComponent',
            'CourseExercisesFieldsCreateNonFieldErrorsErrorComponent', 'CourseExercisesFieldsCreateOrderErrorComponent',
            'CourseExercisesFieldsCreateRequiredErrorComponent', 'CourseExercisesFieldsCreateSegelOnlyErrorComponent',
            'CourseExercisesFieldsCreateStaffResponsesErrorComponent', 'CourseExercisesFieldsCreateTypeErrorComponent',
            'CourseExercisesFieldsCreateUpperLimitErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesFieldsCreateChoicesErrorComponent",
            "CourseExercisesFieldsCreateChoicesINDEXErrorComponent",
            "CourseExercisesFieldsCreateDescriptionErrorComponent",
            "CourseExercisesFieldsCreateGroupsErrorComponent",
            "CourseExercisesFieldsCreateHanichResponsesErrorComponent",
            "CourseExercisesFieldsCreateHasValueErrorComponent",
            "CourseExercisesFieldsCreateLowerLimitErrorComponent",
            "CourseExercisesFieldsCreateMetadataErrorComponent",
            "CourseExercisesFieldsCreateNameErrorComponent",
            "CourseExercisesFieldsCreateNonFieldErrorsErrorComponent",
            "CourseExercisesFieldsCreateOrderErrorComponent",
            "CourseExercisesFieldsCreateRequiredErrorComponent",
            "CourseExercisesFieldsCreateSegelOnlyErrorComponent",
            "CourseExercisesFieldsCreateStaffResponsesErrorComponent",
            "CourseExercisesFieldsCreateTypeErrorComponent",
            "CourseExercisesFieldsCreateUpperLimitErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_fields_create_choices_error_component import (
            CourseExercisesFieldsCreateChoicesErrorComponent,
        )
        from ..models.course_exercises_fields_create_choices_index_error_component import (
            CourseExercisesFieldsCreateChoicesINDEXErrorComponent,
        )
        from ..models.course_exercises_fields_create_description_error_component import (
            CourseExercisesFieldsCreateDescriptionErrorComponent,
        )
        from ..models.course_exercises_fields_create_hanich_responses_error_component import (
            CourseExercisesFieldsCreateHanichResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_create_has_value_error_component import (
            CourseExercisesFieldsCreateHasValueErrorComponent,
        )
        from ..models.course_exercises_fields_create_lower_limit_error_component import (
            CourseExercisesFieldsCreateLowerLimitErrorComponent,
        )
        from ..models.course_exercises_fields_create_metadata_error_component import (
            CourseExercisesFieldsCreateMetadataErrorComponent,
        )
        from ..models.course_exercises_fields_create_name_error_component import (
            CourseExercisesFieldsCreateNameErrorComponent,
        )
        from ..models.course_exercises_fields_create_non_field_errors_error_component import (
            CourseExercisesFieldsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_fields_create_order_error_component import (
            CourseExercisesFieldsCreateOrderErrorComponent,
        )
        from ..models.course_exercises_fields_create_required_error_component import (
            CourseExercisesFieldsCreateRequiredErrorComponent,
        )
        from ..models.course_exercises_fields_create_segel_only_error_component import (
            CourseExercisesFieldsCreateSegelOnlyErrorComponent,
        )
        from ..models.course_exercises_fields_create_staff_responses_error_component import (
            CourseExercisesFieldsCreateStaffResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_create_type_error_component import (
            CourseExercisesFieldsCreateTypeErrorComponent,
        )
        from ..models.course_exercises_fields_create_upper_limit_error_component import (
            CourseExercisesFieldsCreateUpperLimitErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesFieldsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateStaffResponsesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateHanichResponsesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateHasValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateLowerLimitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateUpperLimitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateChoicesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateChoicesINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateSegelOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsCreateMetadataErrorComponent):
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
        from ..models.course_exercises_fields_create_choices_error_component import (
            CourseExercisesFieldsCreateChoicesErrorComponent,
        )
        from ..models.course_exercises_fields_create_choices_index_error_component import (
            CourseExercisesFieldsCreateChoicesINDEXErrorComponent,
        )
        from ..models.course_exercises_fields_create_description_error_component import (
            CourseExercisesFieldsCreateDescriptionErrorComponent,
        )
        from ..models.course_exercises_fields_create_groups_error_component import (
            CourseExercisesFieldsCreateGroupsErrorComponent,
        )
        from ..models.course_exercises_fields_create_hanich_responses_error_component import (
            CourseExercisesFieldsCreateHanichResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_create_has_value_error_component import (
            CourseExercisesFieldsCreateHasValueErrorComponent,
        )
        from ..models.course_exercises_fields_create_lower_limit_error_component import (
            CourseExercisesFieldsCreateLowerLimitErrorComponent,
        )
        from ..models.course_exercises_fields_create_metadata_error_component import (
            CourseExercisesFieldsCreateMetadataErrorComponent,
        )
        from ..models.course_exercises_fields_create_name_error_component import (
            CourseExercisesFieldsCreateNameErrorComponent,
        )
        from ..models.course_exercises_fields_create_non_field_errors_error_component import (
            CourseExercisesFieldsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_fields_create_order_error_component import (
            CourseExercisesFieldsCreateOrderErrorComponent,
        )
        from ..models.course_exercises_fields_create_required_error_component import (
            CourseExercisesFieldsCreateRequiredErrorComponent,
        )
        from ..models.course_exercises_fields_create_segel_only_error_component import (
            CourseExercisesFieldsCreateSegelOnlyErrorComponent,
        )
        from ..models.course_exercises_fields_create_staff_responses_error_component import (
            CourseExercisesFieldsCreateStaffResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_create_type_error_component import (
            CourseExercisesFieldsCreateTypeErrorComponent,
        )
        from ..models.course_exercises_fields_create_upper_limit_error_component import (
            CourseExercisesFieldsCreateUpperLimitErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesFieldsCreateChoicesErrorComponent",
                "CourseExercisesFieldsCreateChoicesINDEXErrorComponent",
                "CourseExercisesFieldsCreateDescriptionErrorComponent",
                "CourseExercisesFieldsCreateGroupsErrorComponent",
                "CourseExercisesFieldsCreateHanichResponsesErrorComponent",
                "CourseExercisesFieldsCreateHasValueErrorComponent",
                "CourseExercisesFieldsCreateLowerLimitErrorComponent",
                "CourseExercisesFieldsCreateMetadataErrorComponent",
                "CourseExercisesFieldsCreateNameErrorComponent",
                "CourseExercisesFieldsCreateNonFieldErrorsErrorComponent",
                "CourseExercisesFieldsCreateOrderErrorComponent",
                "CourseExercisesFieldsCreateRequiredErrorComponent",
                "CourseExercisesFieldsCreateSegelOnlyErrorComponent",
                "CourseExercisesFieldsCreateStaffResponsesErrorComponent",
                "CourseExercisesFieldsCreateTypeErrorComponent",
                "CourseExercisesFieldsCreateUpperLimitErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_0 = (
                        CourseExercisesFieldsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_1 = (
                        CourseExercisesFieldsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_2 = (
                        CourseExercisesFieldsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_3 = (
                        CourseExercisesFieldsCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_4 = (
                        CourseExercisesFieldsCreateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_5 = (
                        CourseExercisesFieldsCreateRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_6 = (
                        CourseExercisesFieldsCreateStaffResponsesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_7 = (
                        CourseExercisesFieldsCreateHanichResponsesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_8 = (
                        CourseExercisesFieldsCreateHasValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_9 = (
                        CourseExercisesFieldsCreateLowerLimitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_10 = (
                        CourseExercisesFieldsCreateUpperLimitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_11 = (
                        CourseExercisesFieldsCreateChoicesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_12 = (
                        CourseExercisesFieldsCreateChoicesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_13 = (
                        CourseExercisesFieldsCreateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_create_error_type_14 = (
                        CourseExercisesFieldsCreateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_create_error_type_14
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_fields_create_error_type_15 = (
                    CourseExercisesFieldsCreateGroupsErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_fields_create_error_type_15

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_fields_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_fields_create_validation_error.additional_properties = d
        return course_exercises_fields_create_validation_error

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
