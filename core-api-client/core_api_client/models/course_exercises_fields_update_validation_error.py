from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_fields_update_choices_error_component import (
        CourseExercisesFieldsUpdateChoicesErrorComponent,
    )
    from ..models.course_exercises_fields_update_choices_index_error_component import (
        CourseExercisesFieldsUpdateChoicesINDEXErrorComponent,
    )
    from ..models.course_exercises_fields_update_description_error_component import (
        CourseExercisesFieldsUpdateDescriptionErrorComponent,
    )
    from ..models.course_exercises_fields_update_groups_error_component import (
        CourseExercisesFieldsUpdateGroupsErrorComponent,
    )
    from ..models.course_exercises_fields_update_hanich_responses_error_component import (
        CourseExercisesFieldsUpdateHanichResponsesErrorComponent,
    )
    from ..models.course_exercises_fields_update_has_value_error_component import (
        CourseExercisesFieldsUpdateHasValueErrorComponent,
    )
    from ..models.course_exercises_fields_update_lower_limit_error_component import (
        CourseExercisesFieldsUpdateLowerLimitErrorComponent,
    )
    from ..models.course_exercises_fields_update_metadata_error_component import (
        CourseExercisesFieldsUpdateMetadataErrorComponent,
    )
    from ..models.course_exercises_fields_update_name_error_component import (
        CourseExercisesFieldsUpdateNameErrorComponent,
    )
    from ..models.course_exercises_fields_update_non_field_errors_error_component import (
        CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_fields_update_order_error_component import (
        CourseExercisesFieldsUpdateOrderErrorComponent,
    )
    from ..models.course_exercises_fields_update_required_error_component import (
        CourseExercisesFieldsUpdateRequiredErrorComponent,
    )
    from ..models.course_exercises_fields_update_segel_only_error_component import (
        CourseExercisesFieldsUpdateSegelOnlyErrorComponent,
    )
    from ..models.course_exercises_fields_update_staff_responses_error_component import (
        CourseExercisesFieldsUpdateStaffResponsesErrorComponent,
    )
    from ..models.course_exercises_fields_update_type_error_component import (
        CourseExercisesFieldsUpdateTypeErrorComponent,
    )
    from ..models.course_exercises_fields_update_upper_limit_error_component import (
        CourseExercisesFieldsUpdateUpperLimitErrorComponent,
    )


T = TypeVar("T", bound="CourseExercisesFieldsUpdateValidationError")


@_attrs_define
class CourseExercisesFieldsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesFieldsUpdateChoicesErrorComponent',
            'CourseExercisesFieldsUpdateChoicesINDEXErrorComponent', 'CourseExercisesFieldsUpdateDescriptionErrorComponent',
            'CourseExercisesFieldsUpdateGroupsErrorComponent', 'CourseExercisesFieldsUpdateHanichResponsesErrorComponent',
            'CourseExercisesFieldsUpdateHasValueErrorComponent', 'CourseExercisesFieldsUpdateLowerLimitErrorComponent',
            'CourseExercisesFieldsUpdateMetadataErrorComponent', 'CourseExercisesFieldsUpdateNameErrorComponent',
            'CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent', 'CourseExercisesFieldsUpdateOrderErrorComponent',
            'CourseExercisesFieldsUpdateRequiredErrorComponent', 'CourseExercisesFieldsUpdateSegelOnlyErrorComponent',
            'CourseExercisesFieldsUpdateStaffResponsesErrorComponent', 'CourseExercisesFieldsUpdateTypeErrorComponent',
            'CourseExercisesFieldsUpdateUpperLimitErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesFieldsUpdateChoicesErrorComponent",
            "CourseExercisesFieldsUpdateChoicesINDEXErrorComponent",
            "CourseExercisesFieldsUpdateDescriptionErrorComponent",
            "CourseExercisesFieldsUpdateGroupsErrorComponent",
            "CourseExercisesFieldsUpdateHanichResponsesErrorComponent",
            "CourseExercisesFieldsUpdateHasValueErrorComponent",
            "CourseExercisesFieldsUpdateLowerLimitErrorComponent",
            "CourseExercisesFieldsUpdateMetadataErrorComponent",
            "CourseExercisesFieldsUpdateNameErrorComponent",
            "CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent",
            "CourseExercisesFieldsUpdateOrderErrorComponent",
            "CourseExercisesFieldsUpdateRequiredErrorComponent",
            "CourseExercisesFieldsUpdateSegelOnlyErrorComponent",
            "CourseExercisesFieldsUpdateStaffResponsesErrorComponent",
            "CourseExercisesFieldsUpdateTypeErrorComponent",
            "CourseExercisesFieldsUpdateUpperLimitErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_fields_update_choices_error_component import (
            CourseExercisesFieldsUpdateChoicesErrorComponent,
        )
        from ..models.course_exercises_fields_update_choices_index_error_component import (
            CourseExercisesFieldsUpdateChoicesINDEXErrorComponent,
        )
        from ..models.course_exercises_fields_update_description_error_component import (
            CourseExercisesFieldsUpdateDescriptionErrorComponent,
        )
        from ..models.course_exercises_fields_update_hanich_responses_error_component import (
            CourseExercisesFieldsUpdateHanichResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_update_has_value_error_component import (
            CourseExercisesFieldsUpdateHasValueErrorComponent,
        )
        from ..models.course_exercises_fields_update_lower_limit_error_component import (
            CourseExercisesFieldsUpdateLowerLimitErrorComponent,
        )
        from ..models.course_exercises_fields_update_metadata_error_component import (
            CourseExercisesFieldsUpdateMetadataErrorComponent,
        )
        from ..models.course_exercises_fields_update_name_error_component import (
            CourseExercisesFieldsUpdateNameErrorComponent,
        )
        from ..models.course_exercises_fields_update_non_field_errors_error_component import (
            CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_fields_update_order_error_component import (
            CourseExercisesFieldsUpdateOrderErrorComponent,
        )
        from ..models.course_exercises_fields_update_required_error_component import (
            CourseExercisesFieldsUpdateRequiredErrorComponent,
        )
        from ..models.course_exercises_fields_update_segel_only_error_component import (
            CourseExercisesFieldsUpdateSegelOnlyErrorComponent,
        )
        from ..models.course_exercises_fields_update_staff_responses_error_component import (
            CourseExercisesFieldsUpdateStaffResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_update_type_error_component import (
            CourseExercisesFieldsUpdateTypeErrorComponent,
        )
        from ..models.course_exercises_fields_update_upper_limit_error_component import (
            CourseExercisesFieldsUpdateUpperLimitErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateStaffResponsesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateHanichResponsesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateHasValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateLowerLimitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateUpperLimitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateChoicesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateChoicesINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateSegelOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesFieldsUpdateMetadataErrorComponent):
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
        from ..models.course_exercises_fields_update_choices_error_component import (
            CourseExercisesFieldsUpdateChoicesErrorComponent,
        )
        from ..models.course_exercises_fields_update_choices_index_error_component import (
            CourseExercisesFieldsUpdateChoicesINDEXErrorComponent,
        )
        from ..models.course_exercises_fields_update_description_error_component import (
            CourseExercisesFieldsUpdateDescriptionErrorComponent,
        )
        from ..models.course_exercises_fields_update_groups_error_component import (
            CourseExercisesFieldsUpdateGroupsErrorComponent,
        )
        from ..models.course_exercises_fields_update_hanich_responses_error_component import (
            CourseExercisesFieldsUpdateHanichResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_update_has_value_error_component import (
            CourseExercisesFieldsUpdateHasValueErrorComponent,
        )
        from ..models.course_exercises_fields_update_lower_limit_error_component import (
            CourseExercisesFieldsUpdateLowerLimitErrorComponent,
        )
        from ..models.course_exercises_fields_update_metadata_error_component import (
            CourseExercisesFieldsUpdateMetadataErrorComponent,
        )
        from ..models.course_exercises_fields_update_name_error_component import (
            CourseExercisesFieldsUpdateNameErrorComponent,
        )
        from ..models.course_exercises_fields_update_non_field_errors_error_component import (
            CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_fields_update_order_error_component import (
            CourseExercisesFieldsUpdateOrderErrorComponent,
        )
        from ..models.course_exercises_fields_update_required_error_component import (
            CourseExercisesFieldsUpdateRequiredErrorComponent,
        )
        from ..models.course_exercises_fields_update_segel_only_error_component import (
            CourseExercisesFieldsUpdateSegelOnlyErrorComponent,
        )
        from ..models.course_exercises_fields_update_staff_responses_error_component import (
            CourseExercisesFieldsUpdateStaffResponsesErrorComponent,
        )
        from ..models.course_exercises_fields_update_type_error_component import (
            CourseExercisesFieldsUpdateTypeErrorComponent,
        )
        from ..models.course_exercises_fields_update_upper_limit_error_component import (
            CourseExercisesFieldsUpdateUpperLimitErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesFieldsUpdateChoicesErrorComponent",
                "CourseExercisesFieldsUpdateChoicesINDEXErrorComponent",
                "CourseExercisesFieldsUpdateDescriptionErrorComponent",
                "CourseExercisesFieldsUpdateGroupsErrorComponent",
                "CourseExercisesFieldsUpdateHanichResponsesErrorComponent",
                "CourseExercisesFieldsUpdateHasValueErrorComponent",
                "CourseExercisesFieldsUpdateLowerLimitErrorComponent",
                "CourseExercisesFieldsUpdateMetadataErrorComponent",
                "CourseExercisesFieldsUpdateNameErrorComponent",
                "CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent",
                "CourseExercisesFieldsUpdateOrderErrorComponent",
                "CourseExercisesFieldsUpdateRequiredErrorComponent",
                "CourseExercisesFieldsUpdateSegelOnlyErrorComponent",
                "CourseExercisesFieldsUpdateStaffResponsesErrorComponent",
                "CourseExercisesFieldsUpdateTypeErrorComponent",
                "CourseExercisesFieldsUpdateUpperLimitErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_0 = (
                        CourseExercisesFieldsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_1 = (
                        CourseExercisesFieldsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_2 = (
                        CourseExercisesFieldsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_3 = (
                        CourseExercisesFieldsUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_4 = (
                        CourseExercisesFieldsUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_5 = (
                        CourseExercisesFieldsUpdateRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_6 = (
                        CourseExercisesFieldsUpdateStaffResponsesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_7 = (
                        CourseExercisesFieldsUpdateHanichResponsesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_8 = (
                        CourseExercisesFieldsUpdateHasValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_9 = (
                        CourseExercisesFieldsUpdateLowerLimitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_10 = (
                        CourseExercisesFieldsUpdateUpperLimitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_11 = (
                        CourseExercisesFieldsUpdateChoicesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_12 = (
                        CourseExercisesFieldsUpdateChoicesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_13 = (
                        CourseExercisesFieldsUpdateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_fields_update_error_type_14 = (
                        CourseExercisesFieldsUpdateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_fields_update_error_type_14
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_fields_update_error_type_15 = (
                    CourseExercisesFieldsUpdateGroupsErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_fields_update_error_type_15

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_fields_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_fields_update_validation_error.additional_properties = d
        return course_exercises_fields_update_validation_error

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
