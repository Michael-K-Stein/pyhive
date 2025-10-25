from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_programs_update_auto_room_error_component import CourseProgramsUpdateAutoRoomErrorComponent
    from ..models.course_programs_update_auto_schedule_error_component import (
        CourseProgramsUpdateAutoScheduleErrorComponent,
    )
    from ..models.course_programs_update_auto_toilet_count_error_component import (
        CourseProgramsUpdateAutoToiletCountErrorComponent,
    )
    from ..models.course_programs_update_auto_toilet_error_component import CourseProgramsUpdateAutoToiletErrorComponent
    from ..models.course_programs_update_checker_error_component import CourseProgramsUpdateCheckerErrorComponent
    from ..models.course_programs_update_default_class_error_component import (
        CourseProgramsUpdateDefaultClassErrorComponent,
    )
    from ..models.course_programs_update_hanich_classes_only_error_component import (
        CourseProgramsUpdateHanichClassesOnlyErrorComponent,
    )
    from ..models.course_programs_update_hanich_day_only_error_component import (
        CourseProgramsUpdateHanichDayOnlyErrorComponent,
    )
    from ..models.course_programs_update_hanich_raise_hand_error_component import (
        CourseProgramsUpdateHanichRaiseHandErrorComponent,
    )
    from ..models.course_programs_update_hanich_schedule_error_component import (
        CourseProgramsUpdateHanichScheduleErrorComponent,
    )
    from ..models.course_programs_update_hanich_work_name_error_component import (
        CourseProgramsUpdateHanichWorkNameErrorComponent,
    )
    from ..models.course_programs_update_name_error_component import CourseProgramsUpdateNameErrorComponent
    from ..models.course_programs_update_non_field_errors_error_component import (
        CourseProgramsUpdateNonFieldErrorsErrorComponent,
    )


T = TypeVar("T", bound="CourseProgramsUpdateValidationError")


@_attrs_define
class CourseProgramsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseProgramsUpdateAutoRoomErrorComponent',
            'CourseProgramsUpdateAutoScheduleErrorComponent', 'CourseProgramsUpdateAutoToiletCountErrorComponent',
            'CourseProgramsUpdateAutoToiletErrorComponent', 'CourseProgramsUpdateCheckerErrorComponent',
            'CourseProgramsUpdateDefaultClassErrorComponent', 'CourseProgramsUpdateHanichClassesOnlyErrorComponent',
            'CourseProgramsUpdateHanichDayOnlyErrorComponent', 'CourseProgramsUpdateHanichRaiseHandErrorComponent',
            'CourseProgramsUpdateHanichScheduleErrorComponent', 'CourseProgramsUpdateHanichWorkNameErrorComponent',
            'CourseProgramsUpdateNameErrorComponent', 'CourseProgramsUpdateNonFieldErrorsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseProgramsUpdateAutoRoomErrorComponent",
            "CourseProgramsUpdateAutoScheduleErrorComponent",
            "CourseProgramsUpdateAutoToiletCountErrorComponent",
            "CourseProgramsUpdateAutoToiletErrorComponent",
            "CourseProgramsUpdateCheckerErrorComponent",
            "CourseProgramsUpdateDefaultClassErrorComponent",
            "CourseProgramsUpdateHanichClassesOnlyErrorComponent",
            "CourseProgramsUpdateHanichDayOnlyErrorComponent",
            "CourseProgramsUpdateHanichRaiseHandErrorComponent",
            "CourseProgramsUpdateHanichScheduleErrorComponent",
            "CourseProgramsUpdateHanichWorkNameErrorComponent",
            "CourseProgramsUpdateNameErrorComponent",
            "CourseProgramsUpdateNonFieldErrorsErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_programs_update_auto_room_error_component import CourseProgramsUpdateAutoRoomErrorComponent
        from ..models.course_programs_update_auto_schedule_error_component import (
            CourseProgramsUpdateAutoScheduleErrorComponent,
        )
        from ..models.course_programs_update_auto_toilet_count_error_component import (
            CourseProgramsUpdateAutoToiletCountErrorComponent,
        )
        from ..models.course_programs_update_auto_toilet_error_component import (
            CourseProgramsUpdateAutoToiletErrorComponent,
        )
        from ..models.course_programs_update_checker_error_component import CourseProgramsUpdateCheckerErrorComponent
        from ..models.course_programs_update_default_class_error_component import (
            CourseProgramsUpdateDefaultClassErrorComponent,
        )
        from ..models.course_programs_update_hanich_classes_only_error_component import (
            CourseProgramsUpdateHanichClassesOnlyErrorComponent,
        )
        from ..models.course_programs_update_hanich_day_only_error_component import (
            CourseProgramsUpdateHanichDayOnlyErrorComponent,
        )
        from ..models.course_programs_update_hanich_raise_hand_error_component import (
            CourseProgramsUpdateHanichRaiseHandErrorComponent,
        )
        from ..models.course_programs_update_hanich_work_name_error_component import (
            CourseProgramsUpdateHanichWorkNameErrorComponent,
        )
        from ..models.course_programs_update_name_error_component import CourseProgramsUpdateNameErrorComponent
        from ..models.course_programs_update_non_field_errors_error_component import (
            CourseProgramsUpdateNonFieldErrorsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseProgramsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateCheckerErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateDefaultClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateAutoToiletErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateHanichRaiseHandErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateAutoScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateAutoRoomErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateHanichDayOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateHanichWorkNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateAutoToiletCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsUpdateHanichClassesOnlyErrorComponent):
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
        from ..models.course_programs_update_auto_room_error_component import CourseProgramsUpdateAutoRoomErrorComponent
        from ..models.course_programs_update_auto_schedule_error_component import (
            CourseProgramsUpdateAutoScheduleErrorComponent,
        )
        from ..models.course_programs_update_auto_toilet_count_error_component import (
            CourseProgramsUpdateAutoToiletCountErrorComponent,
        )
        from ..models.course_programs_update_auto_toilet_error_component import (
            CourseProgramsUpdateAutoToiletErrorComponent,
        )
        from ..models.course_programs_update_checker_error_component import CourseProgramsUpdateCheckerErrorComponent
        from ..models.course_programs_update_default_class_error_component import (
            CourseProgramsUpdateDefaultClassErrorComponent,
        )
        from ..models.course_programs_update_hanich_classes_only_error_component import (
            CourseProgramsUpdateHanichClassesOnlyErrorComponent,
        )
        from ..models.course_programs_update_hanich_day_only_error_component import (
            CourseProgramsUpdateHanichDayOnlyErrorComponent,
        )
        from ..models.course_programs_update_hanich_raise_hand_error_component import (
            CourseProgramsUpdateHanichRaiseHandErrorComponent,
        )
        from ..models.course_programs_update_hanich_schedule_error_component import (
            CourseProgramsUpdateHanichScheduleErrorComponent,
        )
        from ..models.course_programs_update_hanich_work_name_error_component import (
            CourseProgramsUpdateHanichWorkNameErrorComponent,
        )
        from ..models.course_programs_update_name_error_component import CourseProgramsUpdateNameErrorComponent
        from ..models.course_programs_update_non_field_errors_error_component import (
            CourseProgramsUpdateNonFieldErrorsErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseProgramsUpdateAutoRoomErrorComponent",
                "CourseProgramsUpdateAutoScheduleErrorComponent",
                "CourseProgramsUpdateAutoToiletCountErrorComponent",
                "CourseProgramsUpdateAutoToiletErrorComponent",
                "CourseProgramsUpdateCheckerErrorComponent",
                "CourseProgramsUpdateDefaultClassErrorComponent",
                "CourseProgramsUpdateHanichClassesOnlyErrorComponent",
                "CourseProgramsUpdateHanichDayOnlyErrorComponent",
                "CourseProgramsUpdateHanichRaiseHandErrorComponent",
                "CourseProgramsUpdateHanichScheduleErrorComponent",
                "CourseProgramsUpdateHanichWorkNameErrorComponent",
                "CourseProgramsUpdateNameErrorComponent",
                "CourseProgramsUpdateNonFieldErrorsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_0 = (
                        CourseProgramsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_1 = (
                        CourseProgramsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_2 = (
                        CourseProgramsUpdateCheckerErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_3 = (
                        CourseProgramsUpdateDefaultClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_4 = (
                        CourseProgramsUpdateAutoToiletErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_5 = (
                        CourseProgramsUpdateHanichRaiseHandErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_6 = (
                        CourseProgramsUpdateAutoScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_7 = (
                        CourseProgramsUpdateAutoRoomErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_8 = (
                        CourseProgramsUpdateHanichDayOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_9 = (
                        CourseProgramsUpdateHanichWorkNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_10 = (
                        CourseProgramsUpdateAutoToiletCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_update_error_type_11 = (
                        CourseProgramsUpdateHanichClassesOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_update_error_type_11
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_programs_update_error_type_12 = (
                    CourseProgramsUpdateHanichScheduleErrorComponent.from_dict(data)
                )

                return componentsschemas_course_programs_update_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_programs_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_programs_update_validation_error.additional_properties = d
        return course_programs_update_validation_error

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
