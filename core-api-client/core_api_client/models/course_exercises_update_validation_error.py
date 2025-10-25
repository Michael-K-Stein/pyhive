from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_update_autocheck_tag_error_component import (
        CourseExercisesUpdateAutocheckTagErrorComponent,
    )
    from ..models.course_exercises_update_autodone_error_component import CourseExercisesUpdateAutodoneErrorComponent
    from ..models.course_exercises_update_download_error_component import CourseExercisesUpdateDownloadErrorComponent
    from ..models.course_exercises_update_expected_duration_error_component import (
        CourseExercisesUpdateExpectedDurationErrorComponent,
    )
    from ..models.course_exercises_update_is_lecture_error_component import CourseExercisesUpdateIsLectureErrorComponent
    from ..models.course_exercises_update_name_error_component import CourseExercisesUpdateNameErrorComponent
    from ..models.course_exercises_update_non_field_errors_error_component import (
        CourseExercisesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_update_on_creation_data_error_component import (
        CourseExercisesUpdateOnCreationDataErrorComponent,
    )
    from ..models.course_exercises_update_order_error_component import CourseExercisesUpdateOrderErrorComponent
    from ..models.course_exercises_update_parent_module_error_component import (
        CourseExercisesUpdateParentModuleErrorComponent,
    )
    from ..models.course_exercises_update_patbas_download_error_component import (
        CourseExercisesUpdatePatbasDownloadErrorComponent,
    )
    from ..models.course_exercises_update_patbas_error_component import CourseExercisesUpdatePatbasErrorComponent
    from ..models.course_exercises_update_patbas_preview_error_component import (
        CourseExercisesUpdatePatbasPreviewErrorComponent,
    )
    from ..models.course_exercises_update_preview_error_component import CourseExercisesUpdatePreviewErrorComponent
    from ..models.course_exercises_update_segel_brief_error_component import (
        CourseExercisesUpdateSegelBriefErrorComponent,
    )
    from ..models.course_exercises_update_style_error_component import CourseExercisesUpdateStyleErrorComponent
    from ..models.course_exercises_update_tags_error_component import CourseExercisesUpdateTagsErrorComponent


T = TypeVar("T", bound="CourseExercisesUpdateValidationError")


@_attrs_define
class CourseExercisesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesUpdateAutocheckTagErrorComponent',
            'CourseExercisesUpdateAutodoneErrorComponent', 'CourseExercisesUpdateDownloadErrorComponent',
            'CourseExercisesUpdateExpectedDurationErrorComponent', 'CourseExercisesUpdateIsLectureErrorComponent',
            'CourseExercisesUpdateNameErrorComponent', 'CourseExercisesUpdateNonFieldErrorsErrorComponent',
            'CourseExercisesUpdateOnCreationDataErrorComponent', 'CourseExercisesUpdateOrderErrorComponent',
            'CourseExercisesUpdateParentModuleErrorComponent', 'CourseExercisesUpdatePatbasDownloadErrorComponent',
            'CourseExercisesUpdatePatbasErrorComponent', 'CourseExercisesUpdatePatbasPreviewErrorComponent',
            'CourseExercisesUpdatePreviewErrorComponent', 'CourseExercisesUpdateSegelBriefErrorComponent',
            'CourseExercisesUpdateStyleErrorComponent', 'CourseExercisesUpdateTagsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesUpdateAutocheckTagErrorComponent",
            "CourseExercisesUpdateAutodoneErrorComponent",
            "CourseExercisesUpdateDownloadErrorComponent",
            "CourseExercisesUpdateExpectedDurationErrorComponent",
            "CourseExercisesUpdateIsLectureErrorComponent",
            "CourseExercisesUpdateNameErrorComponent",
            "CourseExercisesUpdateNonFieldErrorsErrorComponent",
            "CourseExercisesUpdateOnCreationDataErrorComponent",
            "CourseExercisesUpdateOrderErrorComponent",
            "CourseExercisesUpdateParentModuleErrorComponent",
            "CourseExercisesUpdatePatbasDownloadErrorComponent",
            "CourseExercisesUpdatePatbasErrorComponent",
            "CourseExercisesUpdatePatbasPreviewErrorComponent",
            "CourseExercisesUpdatePreviewErrorComponent",
            "CourseExercisesUpdateSegelBriefErrorComponent",
            "CourseExercisesUpdateStyleErrorComponent",
            "CourseExercisesUpdateTagsErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_update_autocheck_tag_error_component import (
            CourseExercisesUpdateAutocheckTagErrorComponent,
        )
        from ..models.course_exercises_update_autodone_error_component import (
            CourseExercisesUpdateAutodoneErrorComponent,
        )
        from ..models.course_exercises_update_download_error_component import (
            CourseExercisesUpdateDownloadErrorComponent,
        )
        from ..models.course_exercises_update_expected_duration_error_component import (
            CourseExercisesUpdateExpectedDurationErrorComponent,
        )
        from ..models.course_exercises_update_is_lecture_error_component import (
            CourseExercisesUpdateIsLectureErrorComponent,
        )
        from ..models.course_exercises_update_name_error_component import CourseExercisesUpdateNameErrorComponent
        from ..models.course_exercises_update_non_field_errors_error_component import (
            CourseExercisesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_update_on_creation_data_error_component import (
            CourseExercisesUpdateOnCreationDataErrorComponent,
        )
        from ..models.course_exercises_update_order_error_component import CourseExercisesUpdateOrderErrorComponent
        from ..models.course_exercises_update_parent_module_error_component import (
            CourseExercisesUpdateParentModuleErrorComponent,
        )
        from ..models.course_exercises_update_patbas_download_error_component import (
            CourseExercisesUpdatePatbasDownloadErrorComponent,
        )
        from ..models.course_exercises_update_patbas_error_component import CourseExercisesUpdatePatbasErrorComponent
        from ..models.course_exercises_update_patbas_preview_error_component import (
            CourseExercisesUpdatePatbasPreviewErrorComponent,
        )
        from ..models.course_exercises_update_preview_error_component import CourseExercisesUpdatePreviewErrorComponent
        from ..models.course_exercises_update_style_error_component import CourseExercisesUpdateStyleErrorComponent
        from ..models.course_exercises_update_tags_error_component import CourseExercisesUpdateTagsErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateParentModuleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateDownloadErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdatePreviewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdatePatbasPreviewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdatePatbasDownloadErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateIsLectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateStyleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateTagsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdatePatbasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateOnCreationDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateAutocheckTagErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateAutodoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesUpdateExpectedDurationErrorComponent):
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
        from ..models.course_exercises_update_autocheck_tag_error_component import (
            CourseExercisesUpdateAutocheckTagErrorComponent,
        )
        from ..models.course_exercises_update_autodone_error_component import (
            CourseExercisesUpdateAutodoneErrorComponent,
        )
        from ..models.course_exercises_update_download_error_component import (
            CourseExercisesUpdateDownloadErrorComponent,
        )
        from ..models.course_exercises_update_expected_duration_error_component import (
            CourseExercisesUpdateExpectedDurationErrorComponent,
        )
        from ..models.course_exercises_update_is_lecture_error_component import (
            CourseExercisesUpdateIsLectureErrorComponent,
        )
        from ..models.course_exercises_update_name_error_component import CourseExercisesUpdateNameErrorComponent
        from ..models.course_exercises_update_non_field_errors_error_component import (
            CourseExercisesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_update_on_creation_data_error_component import (
            CourseExercisesUpdateOnCreationDataErrorComponent,
        )
        from ..models.course_exercises_update_order_error_component import CourseExercisesUpdateOrderErrorComponent
        from ..models.course_exercises_update_parent_module_error_component import (
            CourseExercisesUpdateParentModuleErrorComponent,
        )
        from ..models.course_exercises_update_patbas_download_error_component import (
            CourseExercisesUpdatePatbasDownloadErrorComponent,
        )
        from ..models.course_exercises_update_patbas_error_component import CourseExercisesUpdatePatbasErrorComponent
        from ..models.course_exercises_update_patbas_preview_error_component import (
            CourseExercisesUpdatePatbasPreviewErrorComponent,
        )
        from ..models.course_exercises_update_preview_error_component import CourseExercisesUpdatePreviewErrorComponent
        from ..models.course_exercises_update_segel_brief_error_component import (
            CourseExercisesUpdateSegelBriefErrorComponent,
        )
        from ..models.course_exercises_update_style_error_component import CourseExercisesUpdateStyleErrorComponent
        from ..models.course_exercises_update_tags_error_component import CourseExercisesUpdateTagsErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesUpdateAutocheckTagErrorComponent",
                "CourseExercisesUpdateAutodoneErrorComponent",
                "CourseExercisesUpdateDownloadErrorComponent",
                "CourseExercisesUpdateExpectedDurationErrorComponent",
                "CourseExercisesUpdateIsLectureErrorComponent",
                "CourseExercisesUpdateNameErrorComponent",
                "CourseExercisesUpdateNonFieldErrorsErrorComponent",
                "CourseExercisesUpdateOnCreationDataErrorComponent",
                "CourseExercisesUpdateOrderErrorComponent",
                "CourseExercisesUpdateParentModuleErrorComponent",
                "CourseExercisesUpdatePatbasDownloadErrorComponent",
                "CourseExercisesUpdatePatbasErrorComponent",
                "CourseExercisesUpdatePatbasPreviewErrorComponent",
                "CourseExercisesUpdatePreviewErrorComponent",
                "CourseExercisesUpdateSegelBriefErrorComponent",
                "CourseExercisesUpdateStyleErrorComponent",
                "CourseExercisesUpdateTagsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_0 = (
                        CourseExercisesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_1 = (
                        CourseExercisesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_2 = (
                        CourseExercisesUpdateParentModuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_3 = (
                        CourseExercisesUpdateDownloadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_4 = (
                        CourseExercisesUpdatePreviewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_5 = (
                        CourseExercisesUpdatePatbasPreviewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_6 = (
                        CourseExercisesUpdatePatbasDownloadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_7 = (
                        CourseExercisesUpdateIsLectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_8 = (
                        CourseExercisesUpdateStyleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_9 = (
                        CourseExercisesUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_10 = (
                        CourseExercisesUpdateTagsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_11 = (
                        CourseExercisesUpdatePatbasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_12 = (
                        CourseExercisesUpdateOnCreationDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_13 = (
                        CourseExercisesUpdateAutocheckTagErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_14 = (
                        CourseExercisesUpdateAutodoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_update_error_type_15 = (
                        CourseExercisesUpdateExpectedDurationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_update_error_type_15
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_update_error_type_16 = (
                    CourseExercisesUpdateSegelBriefErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_update_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_update_validation_error.additional_properties = d
        return course_exercises_update_validation_error

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
