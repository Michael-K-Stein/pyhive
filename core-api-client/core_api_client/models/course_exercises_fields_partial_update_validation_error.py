from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_fields_partial_update_choices_error_component import (
        CourseExercisesFieldsPartialUpdateChoicesErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_choices_index_error_component import (
        CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_description_error_component import (
        CourseExercisesFieldsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_groups_error_component import (
        CourseExercisesFieldsPartialUpdateGroupsErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_hanich_responses_error_component import (
        CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_has_value_error_component import (
        CourseExercisesFieldsPartialUpdateHasValueErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_lower_limit_error_component import (
        CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_metadata_error_component import (
        CourseExercisesFieldsPartialUpdateMetadataErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_name_error_component import (
        CourseExercisesFieldsPartialUpdateNameErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_non_field_errors_error_component import (
        CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_order_error_component import (
        CourseExercisesFieldsPartialUpdateOrderErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_required_error_component import (
        CourseExercisesFieldsPartialUpdateRequiredErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_segel_only_error_component import (
        CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_staff_responses_error_component import (
        CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_type_error_component import (
        CourseExercisesFieldsPartialUpdateTypeErrorComponent,
    )
    from ..models.course_exercises_fields_partial_update_upper_limit_error_component import (
        CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent,
    )


T = TypeVar("T", bound="CourseExercisesFieldsPartialUpdateValidationError")


@_attrs_define
class CourseExercisesFieldsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesFieldsPartialUpdateChoicesErrorComponent',
            'CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent',
            'CourseExercisesFieldsPartialUpdateDescriptionErrorComponent',
            'CourseExercisesFieldsPartialUpdateGroupsErrorComponent',
            'CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent',
            'CourseExercisesFieldsPartialUpdateHasValueErrorComponent',
            'CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent',
            'CourseExercisesFieldsPartialUpdateMetadataErrorComponent',
            'CourseExercisesFieldsPartialUpdateNameErrorComponent',
            'CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent',
            'CourseExercisesFieldsPartialUpdateOrderErrorComponent',
            'CourseExercisesFieldsPartialUpdateRequiredErrorComponent',
            'CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent',
            'CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent',
            'CourseExercisesFieldsPartialUpdateTypeErrorComponent',
            'CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesFieldsPartialUpdateChoicesErrorComponent",
            "CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent",
            "CourseExercisesFieldsPartialUpdateDescriptionErrorComponent",
            "CourseExercisesFieldsPartialUpdateGroupsErrorComponent",
            "CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent",
            "CourseExercisesFieldsPartialUpdateHasValueErrorComponent",
            "CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent",
            "CourseExercisesFieldsPartialUpdateMetadataErrorComponent",
            "CourseExercisesFieldsPartialUpdateNameErrorComponent",
            "CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent",
            "CourseExercisesFieldsPartialUpdateOrderErrorComponent",
            "CourseExercisesFieldsPartialUpdateRequiredErrorComponent",
            "CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent",
            "CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent",
            "CourseExercisesFieldsPartialUpdateTypeErrorComponent",
            "CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_fields_partial_update_choices_error_component import (
            CourseExercisesFieldsPartialUpdateChoicesErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_choices_index_error_component import (
            CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_description_error_component import (
            CourseExercisesFieldsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_hanich_responses_error_component import (
            CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_has_value_error_component import (
            CourseExercisesFieldsPartialUpdateHasValueErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_lower_limit_error_component import (
            CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_metadata_error_component import (
            CourseExercisesFieldsPartialUpdateMetadataErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_name_error_component import (
            CourseExercisesFieldsPartialUpdateNameErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_non_field_errors_error_component import (
            CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_order_error_component import (
            CourseExercisesFieldsPartialUpdateOrderErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_required_error_component import (
            CourseExercisesFieldsPartialUpdateRequiredErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_segel_only_error_component import (
            CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_staff_responses_error_component import (
            CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_type_error_component import (
            CourseExercisesFieldsPartialUpdateTypeErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_upper_limit_error_component import (
            CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateHasValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateChoicesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsPartialUpdateMetadataErrorComponent):
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
        from ..models.course_exercises_fields_partial_update_choices_error_component import (
            CourseExercisesFieldsPartialUpdateChoicesErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_choices_index_error_component import (
            CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_description_error_component import (
            CourseExercisesFieldsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_groups_error_component import (
            CourseExercisesFieldsPartialUpdateGroupsErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_hanich_responses_error_component import (
            CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_has_value_error_component import (
            CourseExercisesFieldsPartialUpdateHasValueErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_lower_limit_error_component import (
            CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_metadata_error_component import (
            CourseExercisesFieldsPartialUpdateMetadataErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_name_error_component import (
            CourseExercisesFieldsPartialUpdateNameErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_non_field_errors_error_component import (
            CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_order_error_component import (
            CourseExercisesFieldsPartialUpdateOrderErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_required_error_component import (
            CourseExercisesFieldsPartialUpdateRequiredErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_segel_only_error_component import (
            CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_staff_responses_error_component import (
            CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_type_error_component import (
            CourseExercisesFieldsPartialUpdateTypeErrorComponent,
        )
        from ..models.course_exercises_fields_partial_update_upper_limit_error_component import (
            CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesFieldsPartialUpdateChoicesErrorComponent",
                "CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent",
                "CourseExercisesFieldsPartialUpdateDescriptionErrorComponent",
                "CourseExercisesFieldsPartialUpdateGroupsErrorComponent",
                "CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent",
                "CourseExercisesFieldsPartialUpdateHasValueErrorComponent",
                "CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent",
                "CourseExercisesFieldsPartialUpdateMetadataErrorComponent",
                "CourseExercisesFieldsPartialUpdateNameErrorComponent",
                "CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent",
                "CourseExercisesFieldsPartialUpdateOrderErrorComponent",
                "CourseExercisesFieldsPartialUpdateRequiredErrorComponent",
                "CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent",
                "CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent",
                "CourseExercisesFieldsPartialUpdateTypeErrorComponent",
                "CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_0 = (
                        CourseExercisesFieldsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_1 = (
                        CourseExercisesFieldsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_2 = (
                        CourseExercisesFieldsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_3 = (
                        CourseExercisesFieldsPartialUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_4 = (
                        CourseExercisesFieldsPartialUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_5 = (
                        CourseExercisesFieldsPartialUpdateRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_6 = (
                        CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_7 = (
                        CourseExercisesFieldsPartialUpdateHanichResponsesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_8 = (
                        CourseExercisesFieldsPartialUpdateHasValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_9 = (
                        CourseExercisesFieldsPartialUpdateLowerLimitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_10 = (
                        CourseExercisesFieldsPartialUpdateUpperLimitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_11 = (
                        CourseExercisesFieldsPartialUpdateChoicesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_12 = (
                        CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_13 = (
                        CourseExercisesFieldsPartialUpdateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_partial_update_error_type_14 = (
                        CourseExercisesFieldsPartialUpdateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_partial_update_error_type_14
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_fields_partial_update_error_type_15 = (
                    CourseExercisesFieldsPartialUpdateGroupsErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_fields_partial_update_error_type_15

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_fields_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_fields_partial_update_validation_error.additional_properties = d
        return course_exercises_fields_partial_update_validation_error

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
