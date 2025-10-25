from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_programs_partial_update_auto_room_error_component import (
        CourseProgramsPartialUpdateAutoRoomErrorComponent,
    )
    from ..models.course_programs_partial_update_auto_schedule_error_component import (
        CourseProgramsPartialUpdateAutoScheduleErrorComponent,
    )
    from ..models.course_programs_partial_update_auto_toilet_count_error_component import (
        CourseProgramsPartialUpdateAutoToiletCountErrorComponent,
    )
    from ..models.course_programs_partial_update_auto_toilet_error_component import (
        CourseProgramsPartialUpdateAutoToiletErrorComponent,
    )
    from ..models.course_programs_partial_update_checker_error_component import (
        CourseProgramsPartialUpdateCheckerErrorComponent,
    )
    from ..models.course_programs_partial_update_default_class_error_component import (
        CourseProgramsPartialUpdateDefaultClassErrorComponent,
    )
    from ..models.course_programs_partial_update_hanich_classes_only_error_component import (
        CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent,
    )
    from ..models.course_programs_partial_update_hanich_day_only_error_component import (
        CourseProgramsPartialUpdateHanichDayOnlyErrorComponent,
    )
    from ..models.course_programs_partial_update_hanich_raise_hand_error_component import (
        CourseProgramsPartialUpdateHanichRaiseHandErrorComponent,
    )
    from ..models.course_programs_partial_update_hanich_schedule_error_component import (
        CourseProgramsPartialUpdateHanichScheduleErrorComponent,
    )
    from ..models.course_programs_partial_update_hanich_work_name_error_component import (
        CourseProgramsPartialUpdateHanichWorkNameErrorComponent,
    )
    from ..models.course_programs_partial_update_name_error_component import (
        CourseProgramsPartialUpdateNameErrorComponent,
    )
    from ..models.course_programs_partial_update_non_field_errors_error_component import (
        CourseProgramsPartialUpdateNonFieldErrorsErrorComponent,
    )


T = TypeVar("T", bound="CourseProgramsPartialUpdateValidationError")


@_attrs_define
class CourseProgramsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseProgramsPartialUpdateAutoRoomErrorComponent',
            'CourseProgramsPartialUpdateAutoScheduleErrorComponent',
            'CourseProgramsPartialUpdateAutoToiletCountErrorComponent',
            'CourseProgramsPartialUpdateAutoToiletErrorComponent', 'CourseProgramsPartialUpdateCheckerErrorComponent',
            'CourseProgramsPartialUpdateDefaultClassErrorComponent',
            'CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent',
            'CourseProgramsPartialUpdateHanichDayOnlyErrorComponent',
            'CourseProgramsPartialUpdateHanichRaiseHandErrorComponent',
            'CourseProgramsPartialUpdateHanichScheduleErrorComponent',
            'CourseProgramsPartialUpdateHanichWorkNameErrorComponent', 'CourseProgramsPartialUpdateNameErrorComponent',
            'CourseProgramsPartialUpdateNonFieldErrorsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseProgramsPartialUpdateAutoRoomErrorComponent",
            "CourseProgramsPartialUpdateAutoScheduleErrorComponent",
            "CourseProgramsPartialUpdateAutoToiletCountErrorComponent",
            "CourseProgramsPartialUpdateAutoToiletErrorComponent",
            "CourseProgramsPartialUpdateCheckerErrorComponent",
            "CourseProgramsPartialUpdateDefaultClassErrorComponent",
            "CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent",
            "CourseProgramsPartialUpdateHanichDayOnlyErrorComponent",
            "CourseProgramsPartialUpdateHanichRaiseHandErrorComponent",
            "CourseProgramsPartialUpdateHanichScheduleErrorComponent",
            "CourseProgramsPartialUpdateHanichWorkNameErrorComponent",
            "CourseProgramsPartialUpdateNameErrorComponent",
            "CourseProgramsPartialUpdateNonFieldErrorsErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_programs_partial_update_auto_room_error_component import (
            CourseProgramsPartialUpdateAutoRoomErrorComponent,
        )
        from ..models.course_programs_partial_update_auto_schedule_error_component import (
            CourseProgramsPartialUpdateAutoScheduleErrorComponent,
        )
        from ..models.course_programs_partial_update_auto_toilet_count_error_component import (
            CourseProgramsPartialUpdateAutoToiletCountErrorComponent,
        )
        from ..models.course_programs_partial_update_auto_toilet_error_component import (
            CourseProgramsPartialUpdateAutoToiletErrorComponent,
        )
        from ..models.course_programs_partial_update_checker_error_component import (
            CourseProgramsPartialUpdateCheckerErrorComponent,
        )
        from ..models.course_programs_partial_update_default_class_error_component import (
            CourseProgramsPartialUpdateDefaultClassErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_classes_only_error_component import (
            CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_day_only_error_component import (
            CourseProgramsPartialUpdateHanichDayOnlyErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_raise_hand_error_component import (
            CourseProgramsPartialUpdateHanichRaiseHandErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_work_name_error_component import (
            CourseProgramsPartialUpdateHanichWorkNameErrorComponent,
        )
        from ..models.course_programs_partial_update_name_error_component import (
            CourseProgramsPartialUpdateNameErrorComponent,
        )
        from ..models.course_programs_partial_update_non_field_errors_error_component import (
            CourseProgramsPartialUpdateNonFieldErrorsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseProgramsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateCheckerErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateDefaultClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateAutoToiletErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateHanichRaiseHandErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateAutoScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateAutoRoomErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateHanichDayOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateHanichWorkNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateAutoToiletCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent):
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
        from ..models.course_programs_partial_update_auto_room_error_component import (
            CourseProgramsPartialUpdateAutoRoomErrorComponent,
        )
        from ..models.course_programs_partial_update_auto_schedule_error_component import (
            CourseProgramsPartialUpdateAutoScheduleErrorComponent,
        )
        from ..models.course_programs_partial_update_auto_toilet_count_error_component import (
            CourseProgramsPartialUpdateAutoToiletCountErrorComponent,
        )
        from ..models.course_programs_partial_update_auto_toilet_error_component import (
            CourseProgramsPartialUpdateAutoToiletErrorComponent,
        )
        from ..models.course_programs_partial_update_checker_error_component import (
            CourseProgramsPartialUpdateCheckerErrorComponent,
        )
        from ..models.course_programs_partial_update_default_class_error_component import (
            CourseProgramsPartialUpdateDefaultClassErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_classes_only_error_component import (
            CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_day_only_error_component import (
            CourseProgramsPartialUpdateHanichDayOnlyErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_raise_hand_error_component import (
            CourseProgramsPartialUpdateHanichRaiseHandErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_schedule_error_component import (
            CourseProgramsPartialUpdateHanichScheduleErrorComponent,
        )
        from ..models.course_programs_partial_update_hanich_work_name_error_component import (
            CourseProgramsPartialUpdateHanichWorkNameErrorComponent,
        )
        from ..models.course_programs_partial_update_name_error_component import (
            CourseProgramsPartialUpdateNameErrorComponent,
        )
        from ..models.course_programs_partial_update_non_field_errors_error_component import (
            CourseProgramsPartialUpdateNonFieldErrorsErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseProgramsPartialUpdateAutoRoomErrorComponent",
                "CourseProgramsPartialUpdateAutoScheduleErrorComponent",
                "CourseProgramsPartialUpdateAutoToiletCountErrorComponent",
                "CourseProgramsPartialUpdateAutoToiletErrorComponent",
                "CourseProgramsPartialUpdateCheckerErrorComponent",
                "CourseProgramsPartialUpdateDefaultClassErrorComponent",
                "CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent",
                "CourseProgramsPartialUpdateHanichDayOnlyErrorComponent",
                "CourseProgramsPartialUpdateHanichRaiseHandErrorComponent",
                "CourseProgramsPartialUpdateHanichScheduleErrorComponent",
                "CourseProgramsPartialUpdateHanichWorkNameErrorComponent",
                "CourseProgramsPartialUpdateNameErrorComponent",
                "CourseProgramsPartialUpdateNonFieldErrorsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_0 = (
                        CourseProgramsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_1 = (
                        CourseProgramsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_2 = (
                        CourseProgramsPartialUpdateCheckerErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_3 = (
                        CourseProgramsPartialUpdateDefaultClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_4 = (
                        CourseProgramsPartialUpdateAutoToiletErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_5 = (
                        CourseProgramsPartialUpdateHanichRaiseHandErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_6 = (
                        CourseProgramsPartialUpdateAutoScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_7 = (
                        CourseProgramsPartialUpdateAutoRoomErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_8 = (
                        CourseProgramsPartialUpdateHanichDayOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_9 = (
                        CourseProgramsPartialUpdateHanichWorkNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_10 = (
                        CourseProgramsPartialUpdateAutoToiletCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_partial_update_error_type_11 = (
                        CourseProgramsPartialUpdateHanichClassesOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_partial_update_error_type_11
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_programs_partial_update_error_type_12 = (
                    CourseProgramsPartialUpdateHanichScheduleErrorComponent.from_dict(data)
                )

                return componentsschemas_course_programs_partial_update_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_programs_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_programs_partial_update_validation_error.additional_properties = d
        return course_programs_partial_update_validation_error

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
