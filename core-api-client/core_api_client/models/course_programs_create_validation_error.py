from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_programs_create_auto_room_error_component import CourseProgramsCreateAutoRoomErrorComponent
    from ..models.course_programs_create_auto_schedule_error_component import (
        CourseProgramsCreateAutoScheduleErrorComponent,
    )
    from ..models.course_programs_create_auto_toilet_count_error_component import (
        CourseProgramsCreateAutoToiletCountErrorComponent,
    )
    from ..models.course_programs_create_auto_toilet_error_component import CourseProgramsCreateAutoToiletErrorComponent
    from ..models.course_programs_create_checker_error_component import CourseProgramsCreateCheckerErrorComponent
    from ..models.course_programs_create_default_class_error_component import (
        CourseProgramsCreateDefaultClassErrorComponent,
    )
    from ..models.course_programs_create_hanich_classes_only_error_component import (
        CourseProgramsCreateHanichClassesOnlyErrorComponent,
    )
    from ..models.course_programs_create_hanich_day_only_error_component import (
        CourseProgramsCreateHanichDayOnlyErrorComponent,
    )
    from ..models.course_programs_create_hanich_raise_hand_error_component import (
        CourseProgramsCreateHanichRaiseHandErrorComponent,
    )
    from ..models.course_programs_create_hanich_schedule_error_component import (
        CourseProgramsCreateHanichScheduleErrorComponent,
    )
    from ..models.course_programs_create_hanich_work_name_error_component import (
        CourseProgramsCreateHanichWorkNameErrorComponent,
    )
    from ..models.course_programs_create_name_error_component import CourseProgramsCreateNameErrorComponent
    from ..models.course_programs_create_non_field_errors_error_component import (
        CourseProgramsCreateNonFieldErrorsErrorComponent,
    )


T = TypeVar("T", bound="CourseProgramsCreateValidationError")


@_attrs_define
class CourseProgramsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseProgramsCreateAutoRoomErrorComponent',
            'CourseProgramsCreateAutoScheduleErrorComponent', 'CourseProgramsCreateAutoToiletCountErrorComponent',
            'CourseProgramsCreateAutoToiletErrorComponent', 'CourseProgramsCreateCheckerErrorComponent',
            'CourseProgramsCreateDefaultClassErrorComponent', 'CourseProgramsCreateHanichClassesOnlyErrorComponent',
            'CourseProgramsCreateHanichDayOnlyErrorComponent', 'CourseProgramsCreateHanichRaiseHandErrorComponent',
            'CourseProgramsCreateHanichScheduleErrorComponent', 'CourseProgramsCreateHanichWorkNameErrorComponent',
            'CourseProgramsCreateNameErrorComponent', 'CourseProgramsCreateNonFieldErrorsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseProgramsCreateAutoRoomErrorComponent",
            "CourseProgramsCreateAutoScheduleErrorComponent",
            "CourseProgramsCreateAutoToiletCountErrorComponent",
            "CourseProgramsCreateAutoToiletErrorComponent",
            "CourseProgramsCreateCheckerErrorComponent",
            "CourseProgramsCreateDefaultClassErrorComponent",
            "CourseProgramsCreateHanichClassesOnlyErrorComponent",
            "CourseProgramsCreateHanichDayOnlyErrorComponent",
            "CourseProgramsCreateHanichRaiseHandErrorComponent",
            "CourseProgramsCreateHanichScheduleErrorComponent",
            "CourseProgramsCreateHanichWorkNameErrorComponent",
            "CourseProgramsCreateNameErrorComponent",
            "CourseProgramsCreateNonFieldErrorsErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_programs_create_auto_room_error_component import CourseProgramsCreateAutoRoomErrorComponent
        from ..models.course_programs_create_auto_schedule_error_component import (
            CourseProgramsCreateAutoScheduleErrorComponent,
        )
        from ..models.course_programs_create_auto_toilet_count_error_component import (
            CourseProgramsCreateAutoToiletCountErrorComponent,
        )
        from ..models.course_programs_create_auto_toilet_error_component import (
            CourseProgramsCreateAutoToiletErrorComponent,
        )
        from ..models.course_programs_create_checker_error_component import CourseProgramsCreateCheckerErrorComponent
        from ..models.course_programs_create_default_class_error_component import (
            CourseProgramsCreateDefaultClassErrorComponent,
        )
        from ..models.course_programs_create_hanich_classes_only_error_component import (
            CourseProgramsCreateHanichClassesOnlyErrorComponent,
        )
        from ..models.course_programs_create_hanich_day_only_error_component import (
            CourseProgramsCreateHanichDayOnlyErrorComponent,
        )
        from ..models.course_programs_create_hanich_raise_hand_error_component import (
            CourseProgramsCreateHanichRaiseHandErrorComponent,
        )
        from ..models.course_programs_create_hanich_work_name_error_component import (
            CourseProgramsCreateHanichWorkNameErrorComponent,
        )
        from ..models.course_programs_create_name_error_component import CourseProgramsCreateNameErrorComponent
        from ..models.course_programs_create_non_field_errors_error_component import (
            CourseProgramsCreateNonFieldErrorsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseProgramsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateCheckerErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateDefaultClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateAutoToiletErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateHanichRaiseHandErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateAutoScheduleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateAutoRoomErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateHanichDayOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateHanichWorkNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateAutoToiletCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseProgramsCreateHanichClassesOnlyErrorComponent):
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
        from ..models.course_programs_create_auto_room_error_component import CourseProgramsCreateAutoRoomErrorComponent
        from ..models.course_programs_create_auto_schedule_error_component import (
            CourseProgramsCreateAutoScheduleErrorComponent,
        )
        from ..models.course_programs_create_auto_toilet_count_error_component import (
            CourseProgramsCreateAutoToiletCountErrorComponent,
        )
        from ..models.course_programs_create_auto_toilet_error_component import (
            CourseProgramsCreateAutoToiletErrorComponent,
        )
        from ..models.course_programs_create_checker_error_component import CourseProgramsCreateCheckerErrorComponent
        from ..models.course_programs_create_default_class_error_component import (
            CourseProgramsCreateDefaultClassErrorComponent,
        )
        from ..models.course_programs_create_hanich_classes_only_error_component import (
            CourseProgramsCreateHanichClassesOnlyErrorComponent,
        )
        from ..models.course_programs_create_hanich_day_only_error_component import (
            CourseProgramsCreateHanichDayOnlyErrorComponent,
        )
        from ..models.course_programs_create_hanich_raise_hand_error_component import (
            CourseProgramsCreateHanichRaiseHandErrorComponent,
        )
        from ..models.course_programs_create_hanich_schedule_error_component import (
            CourseProgramsCreateHanichScheduleErrorComponent,
        )
        from ..models.course_programs_create_hanich_work_name_error_component import (
            CourseProgramsCreateHanichWorkNameErrorComponent,
        )
        from ..models.course_programs_create_name_error_component import CourseProgramsCreateNameErrorComponent
        from ..models.course_programs_create_non_field_errors_error_component import (
            CourseProgramsCreateNonFieldErrorsErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseProgramsCreateAutoRoomErrorComponent",
                "CourseProgramsCreateAutoScheduleErrorComponent",
                "CourseProgramsCreateAutoToiletCountErrorComponent",
                "CourseProgramsCreateAutoToiletErrorComponent",
                "CourseProgramsCreateCheckerErrorComponent",
                "CourseProgramsCreateDefaultClassErrorComponent",
                "CourseProgramsCreateHanichClassesOnlyErrorComponent",
                "CourseProgramsCreateHanichDayOnlyErrorComponent",
                "CourseProgramsCreateHanichRaiseHandErrorComponent",
                "CourseProgramsCreateHanichScheduleErrorComponent",
                "CourseProgramsCreateHanichWorkNameErrorComponent",
                "CourseProgramsCreateNameErrorComponent",
                "CourseProgramsCreateNonFieldErrorsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_0 = (
                        CourseProgramsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_1 = (
                        CourseProgramsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_2 = (
                        CourseProgramsCreateCheckerErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_3 = (
                        CourseProgramsCreateDefaultClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_4 = (
                        CourseProgramsCreateAutoToiletErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_5 = (
                        CourseProgramsCreateHanichRaiseHandErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_6 = (
                        CourseProgramsCreateAutoScheduleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_7 = (
                        CourseProgramsCreateAutoRoomErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_8 = (
                        CourseProgramsCreateHanichDayOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_9 = (
                        CourseProgramsCreateHanichWorkNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_10 = (
                        CourseProgramsCreateAutoToiletCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_programs_create_error_type_11 = (
                        CourseProgramsCreateHanichClassesOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_programs_create_error_type_11
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_programs_create_error_type_12 = (
                    CourseProgramsCreateHanichScheduleErrorComponent.from_dict(data)
                )

                return componentsschemas_course_programs_create_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_programs_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_programs_create_validation_error.additional_properties = d
        return course_programs_create_validation_error

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
