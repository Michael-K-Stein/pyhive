from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_create_autocheck_tag_error_component import (
        CourseExercisesCreateAutocheckTagErrorComponent,
    )
    from ..models.course_exercises_create_autodone_error_component import CourseExercisesCreateAutodoneErrorComponent
    from ..models.course_exercises_create_download_error_component import CourseExercisesCreateDownloadErrorComponent
    from ..models.course_exercises_create_expected_duration_error_component import (
        CourseExercisesCreateExpectedDurationErrorComponent,
    )
    from ..models.course_exercises_create_is_lecture_error_component import CourseExercisesCreateIsLectureErrorComponent
    from ..models.course_exercises_create_name_error_component import CourseExercisesCreateNameErrorComponent
    from ..models.course_exercises_create_non_field_errors_error_component import (
        CourseExercisesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_create_on_creation_data_error_component import (
        CourseExercisesCreateOnCreationDataErrorComponent,
    )
    from ..models.course_exercises_create_order_error_component import CourseExercisesCreateOrderErrorComponent
    from ..models.course_exercises_create_parent_module_error_component import (
        CourseExercisesCreateParentModuleErrorComponent,
    )
    from ..models.course_exercises_create_patbas_download_error_component import (
        CourseExercisesCreatePatbasDownloadErrorComponent,
    )
    from ..models.course_exercises_create_patbas_error_component import CourseExercisesCreatePatbasErrorComponent
    from ..models.course_exercises_create_patbas_preview_error_component import (
        CourseExercisesCreatePatbasPreviewErrorComponent,
    )
    from ..models.course_exercises_create_preview_error_component import CourseExercisesCreatePreviewErrorComponent
    from ..models.course_exercises_create_segel_brief_error_component import (
        CourseExercisesCreateSegelBriefErrorComponent,
    )
    from ..models.course_exercises_create_style_error_component import CourseExercisesCreateStyleErrorComponent
    from ..models.course_exercises_create_tags_error_component import CourseExercisesCreateTagsErrorComponent


T = TypeVar("T", bound="CourseExercisesCreateValidationError")


@_attrs_define
class CourseExercisesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesCreateAutocheckTagErrorComponent',
            'CourseExercisesCreateAutodoneErrorComponent', 'CourseExercisesCreateDownloadErrorComponent',
            'CourseExercisesCreateExpectedDurationErrorComponent', 'CourseExercisesCreateIsLectureErrorComponent',
            'CourseExercisesCreateNameErrorComponent', 'CourseExercisesCreateNonFieldErrorsErrorComponent',
            'CourseExercisesCreateOnCreationDataErrorComponent', 'CourseExercisesCreateOrderErrorComponent',
            'CourseExercisesCreateParentModuleErrorComponent', 'CourseExercisesCreatePatbasDownloadErrorComponent',
            'CourseExercisesCreatePatbasErrorComponent', 'CourseExercisesCreatePatbasPreviewErrorComponent',
            'CourseExercisesCreatePreviewErrorComponent', 'CourseExercisesCreateSegelBriefErrorComponent',
            'CourseExercisesCreateStyleErrorComponent', 'CourseExercisesCreateTagsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesCreateAutocheckTagErrorComponent",
            "CourseExercisesCreateAutodoneErrorComponent",
            "CourseExercisesCreateDownloadErrorComponent",
            "CourseExercisesCreateExpectedDurationErrorComponent",
            "CourseExercisesCreateIsLectureErrorComponent",
            "CourseExercisesCreateNameErrorComponent",
            "CourseExercisesCreateNonFieldErrorsErrorComponent",
            "CourseExercisesCreateOnCreationDataErrorComponent",
            "CourseExercisesCreateOrderErrorComponent",
            "CourseExercisesCreateParentModuleErrorComponent",
            "CourseExercisesCreatePatbasDownloadErrorComponent",
            "CourseExercisesCreatePatbasErrorComponent",
            "CourseExercisesCreatePatbasPreviewErrorComponent",
            "CourseExercisesCreatePreviewErrorComponent",
            "CourseExercisesCreateSegelBriefErrorComponent",
            "CourseExercisesCreateStyleErrorComponent",
            "CourseExercisesCreateTagsErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_create_autocheck_tag_error_component import (
            CourseExercisesCreateAutocheckTagErrorComponent,
        )
        from ..models.course_exercises_create_autodone_error_component import (
            CourseExercisesCreateAutodoneErrorComponent,
        )
        from ..models.course_exercises_create_download_error_component import (
            CourseExercisesCreateDownloadErrorComponent,
        )
        from ..models.course_exercises_create_expected_duration_error_component import (
            CourseExercisesCreateExpectedDurationErrorComponent,
        )
        from ..models.course_exercises_create_is_lecture_error_component import (
            CourseExercisesCreateIsLectureErrorComponent,
        )
        from ..models.course_exercises_create_name_error_component import CourseExercisesCreateNameErrorComponent
        from ..models.course_exercises_create_non_field_errors_error_component import (
            CourseExercisesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_create_on_creation_data_error_component import (
            CourseExercisesCreateOnCreationDataErrorComponent,
        )
        from ..models.course_exercises_create_order_error_component import CourseExercisesCreateOrderErrorComponent
        from ..models.course_exercises_create_parent_module_error_component import (
            CourseExercisesCreateParentModuleErrorComponent,
        )
        from ..models.course_exercises_create_patbas_download_error_component import (
            CourseExercisesCreatePatbasDownloadErrorComponent,
        )
        from ..models.course_exercises_create_patbas_error_component import CourseExercisesCreatePatbasErrorComponent
        from ..models.course_exercises_create_patbas_preview_error_component import (
            CourseExercisesCreatePatbasPreviewErrorComponent,
        )
        from ..models.course_exercises_create_preview_error_component import CourseExercisesCreatePreviewErrorComponent
        from ..models.course_exercises_create_style_error_component import CourseExercisesCreateStyleErrorComponent
        from ..models.course_exercises_create_tags_error_component import CourseExercisesCreateTagsErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateParentModuleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateDownloadErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreatePreviewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreatePatbasPreviewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreatePatbasDownloadErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateIsLectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateStyleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateTagsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreatePatbasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateOnCreationDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateAutocheckTagErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateAutodoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesCreateExpectedDurationErrorComponent):
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
        from ..models.course_exercises_create_autocheck_tag_error_component import (
            CourseExercisesCreateAutocheckTagErrorComponent,
        )
        from ..models.course_exercises_create_autodone_error_component import (
            CourseExercisesCreateAutodoneErrorComponent,
        )
        from ..models.course_exercises_create_download_error_component import (
            CourseExercisesCreateDownloadErrorComponent,
        )
        from ..models.course_exercises_create_expected_duration_error_component import (
            CourseExercisesCreateExpectedDurationErrorComponent,
        )
        from ..models.course_exercises_create_is_lecture_error_component import (
            CourseExercisesCreateIsLectureErrorComponent,
        )
        from ..models.course_exercises_create_name_error_component import CourseExercisesCreateNameErrorComponent
        from ..models.course_exercises_create_non_field_errors_error_component import (
            CourseExercisesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_create_on_creation_data_error_component import (
            CourseExercisesCreateOnCreationDataErrorComponent,
        )
        from ..models.course_exercises_create_order_error_component import CourseExercisesCreateOrderErrorComponent
        from ..models.course_exercises_create_parent_module_error_component import (
            CourseExercisesCreateParentModuleErrorComponent,
        )
        from ..models.course_exercises_create_patbas_download_error_component import (
            CourseExercisesCreatePatbasDownloadErrorComponent,
        )
        from ..models.course_exercises_create_patbas_error_component import CourseExercisesCreatePatbasErrorComponent
        from ..models.course_exercises_create_patbas_preview_error_component import (
            CourseExercisesCreatePatbasPreviewErrorComponent,
        )
        from ..models.course_exercises_create_preview_error_component import CourseExercisesCreatePreviewErrorComponent
        from ..models.course_exercises_create_segel_brief_error_component import (
            CourseExercisesCreateSegelBriefErrorComponent,
        )
        from ..models.course_exercises_create_style_error_component import CourseExercisesCreateStyleErrorComponent
        from ..models.course_exercises_create_tags_error_component import CourseExercisesCreateTagsErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesCreateAutocheckTagErrorComponent",
                "CourseExercisesCreateAutodoneErrorComponent",
                "CourseExercisesCreateDownloadErrorComponent",
                "CourseExercisesCreateExpectedDurationErrorComponent",
                "CourseExercisesCreateIsLectureErrorComponent",
                "CourseExercisesCreateNameErrorComponent",
                "CourseExercisesCreateNonFieldErrorsErrorComponent",
                "CourseExercisesCreateOnCreationDataErrorComponent",
                "CourseExercisesCreateOrderErrorComponent",
                "CourseExercisesCreateParentModuleErrorComponent",
                "CourseExercisesCreatePatbasDownloadErrorComponent",
                "CourseExercisesCreatePatbasErrorComponent",
                "CourseExercisesCreatePatbasPreviewErrorComponent",
                "CourseExercisesCreatePreviewErrorComponent",
                "CourseExercisesCreateSegelBriefErrorComponent",
                "CourseExercisesCreateStyleErrorComponent",
                "CourseExercisesCreateTagsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_0 = (
                        CourseExercisesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_1 = (
                        CourseExercisesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_2 = (
                        CourseExercisesCreateParentModuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_3 = (
                        CourseExercisesCreateDownloadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_4 = (
                        CourseExercisesCreatePreviewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_5 = (
                        CourseExercisesCreatePatbasPreviewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_6 = (
                        CourseExercisesCreatePatbasDownloadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_7 = (
                        CourseExercisesCreateIsLectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_8 = (
                        CourseExercisesCreateStyleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_9 = (
                        CourseExercisesCreateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_10 = (
                        CourseExercisesCreateTagsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_11 = (
                        CourseExercisesCreatePatbasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_12 = (
                        CourseExercisesCreateOnCreationDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_13 = (
                        CourseExercisesCreateAutocheckTagErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_14 = (
                        CourseExercisesCreateAutodoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_create_error_type_15 = (
                        CourseExercisesCreateExpectedDurationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_create_error_type_15
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_create_error_type_16 = (
                    CourseExercisesCreateSegelBriefErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_create_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_create_validation_error.additional_properties = d
        return course_exercises_create_validation_error

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
