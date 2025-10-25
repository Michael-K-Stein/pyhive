from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.course_exercises_partial_update_autocheck_tag_error_component import (
        CourseExercisesPartialUpdateAutocheckTagErrorComponent,
    )
    from ..models.course_exercises_partial_update_autodone_error_component import (
        CourseExercisesPartialUpdateAutodoneErrorComponent,
    )
    from ..models.course_exercises_partial_update_download_error_component import (
        CourseExercisesPartialUpdateDownloadErrorComponent,
    )
    from ..models.course_exercises_partial_update_expected_duration_error_component import (
        CourseExercisesPartialUpdateExpectedDurationErrorComponent,
    )
    from ..models.course_exercises_partial_update_is_lecture_error_component import (
        CourseExercisesPartialUpdateIsLectureErrorComponent,
    )
    from ..models.course_exercises_partial_update_name_error_component import (
        CourseExercisesPartialUpdateNameErrorComponent,
    )
    from ..models.course_exercises_partial_update_non_field_errors_error_component import (
        CourseExercisesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.course_exercises_partial_update_on_creation_data_error_component import (
        CourseExercisesPartialUpdateOnCreationDataErrorComponent,
    )
    from ..models.course_exercises_partial_update_order_error_component import (
        CourseExercisesPartialUpdateOrderErrorComponent,
    )
    from ..models.course_exercises_partial_update_parent_module_error_component import (
        CourseExercisesPartialUpdateParentModuleErrorComponent,
    )
    from ..models.course_exercises_partial_update_patbas_download_error_component import (
        CourseExercisesPartialUpdatePatbasDownloadErrorComponent,
    )
    from ..models.course_exercises_partial_update_patbas_error_component import (
        CourseExercisesPartialUpdatePatbasErrorComponent,
    )
    from ..models.course_exercises_partial_update_patbas_preview_error_component import (
        CourseExercisesPartialUpdatePatbasPreviewErrorComponent,
    )
    from ..models.course_exercises_partial_update_preview_error_component import (
        CourseExercisesPartialUpdatePreviewErrorComponent,
    )
    from ..models.course_exercises_partial_update_segel_brief_error_component import (
        CourseExercisesPartialUpdateSegelBriefErrorComponent,
    )
    from ..models.course_exercises_partial_update_style_error_component import (
        CourseExercisesPartialUpdateStyleErrorComponent,
    )
    from ..models.course_exercises_partial_update_tags_error_component import (
        CourseExercisesPartialUpdateTagsErrorComponent,
    )


T = TypeVar("T", bound="CourseExercisesPartialUpdateValidationError")


@_attrs_define
class CourseExercisesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['CourseExercisesPartialUpdateAutocheckTagErrorComponent',
            'CourseExercisesPartialUpdateAutodoneErrorComponent', 'CourseExercisesPartialUpdateDownloadErrorComponent',
            'CourseExercisesPartialUpdateExpectedDurationErrorComponent',
            'CourseExercisesPartialUpdateIsLectureErrorComponent', 'CourseExercisesPartialUpdateNameErrorComponent',
            'CourseExercisesPartialUpdateNonFieldErrorsErrorComponent',
            'CourseExercisesPartialUpdateOnCreationDataErrorComponent', 'CourseExercisesPartialUpdateOrderErrorComponent',
            'CourseExercisesPartialUpdateParentModuleErrorComponent',
            'CourseExercisesPartialUpdatePatbasDownloadErrorComponent', 'CourseExercisesPartialUpdatePatbasErrorComponent',
            'CourseExercisesPartialUpdatePatbasPreviewErrorComponent', 'CourseExercisesPartialUpdatePreviewErrorComponent',
            'CourseExercisesPartialUpdateSegelBriefErrorComponent', 'CourseExercisesPartialUpdateStyleErrorComponent',
            'CourseExercisesPartialUpdateTagsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "CourseExercisesPartialUpdateAutocheckTagErrorComponent",
            "CourseExercisesPartialUpdateAutodoneErrorComponent",
            "CourseExercisesPartialUpdateDownloadErrorComponent",
            "CourseExercisesPartialUpdateExpectedDurationErrorComponent",
            "CourseExercisesPartialUpdateIsLectureErrorComponent",
            "CourseExercisesPartialUpdateNameErrorComponent",
            "CourseExercisesPartialUpdateNonFieldErrorsErrorComponent",
            "CourseExercisesPartialUpdateOnCreationDataErrorComponent",
            "CourseExercisesPartialUpdateOrderErrorComponent",
            "CourseExercisesPartialUpdateParentModuleErrorComponent",
            "CourseExercisesPartialUpdatePatbasDownloadErrorComponent",
            "CourseExercisesPartialUpdatePatbasErrorComponent",
            "CourseExercisesPartialUpdatePatbasPreviewErrorComponent",
            "CourseExercisesPartialUpdatePreviewErrorComponent",
            "CourseExercisesPartialUpdateSegelBriefErrorComponent",
            "CourseExercisesPartialUpdateStyleErrorComponent",
            "CourseExercisesPartialUpdateTagsErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.course_exercises_partial_update_autocheck_tag_error_component import (
            CourseExercisesPartialUpdateAutocheckTagErrorComponent,
        )
        from ..models.course_exercises_partial_update_autodone_error_component import (
            CourseExercisesPartialUpdateAutodoneErrorComponent,
        )
        from ..models.course_exercises_partial_update_download_error_component import (
            CourseExercisesPartialUpdateDownloadErrorComponent,
        )
        from ..models.course_exercises_partial_update_expected_duration_error_component import (
            CourseExercisesPartialUpdateExpectedDurationErrorComponent,
        )
        from ..models.course_exercises_partial_update_is_lecture_error_component import (
            CourseExercisesPartialUpdateIsLectureErrorComponent,
        )
        from ..models.course_exercises_partial_update_name_error_component import (
            CourseExercisesPartialUpdateNameErrorComponent,
        )
        from ..models.course_exercises_partial_update_non_field_errors_error_component import (
            CourseExercisesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_partial_update_on_creation_data_error_component import (
            CourseExercisesPartialUpdateOnCreationDataErrorComponent,
        )
        from ..models.course_exercises_partial_update_order_error_component import (
            CourseExercisesPartialUpdateOrderErrorComponent,
        )
        from ..models.course_exercises_partial_update_parent_module_error_component import (
            CourseExercisesPartialUpdateParentModuleErrorComponent,
        )
        from ..models.course_exercises_partial_update_patbas_download_error_component import (
            CourseExercisesPartialUpdatePatbasDownloadErrorComponent,
        )
        from ..models.course_exercises_partial_update_patbas_error_component import (
            CourseExercisesPartialUpdatePatbasErrorComponent,
        )
        from ..models.course_exercises_partial_update_patbas_preview_error_component import (
            CourseExercisesPartialUpdatePatbasPreviewErrorComponent,
        )
        from ..models.course_exercises_partial_update_preview_error_component import (
            CourseExercisesPartialUpdatePreviewErrorComponent,
        )
        from ..models.course_exercises_partial_update_style_error_component import (
            CourseExercisesPartialUpdateStyleErrorComponent,
        )
        from ..models.course_exercises_partial_update_tags_error_component import (
            CourseExercisesPartialUpdateTagsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, CourseExercisesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateParentModuleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateDownloadErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdatePreviewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdatePatbasPreviewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdatePatbasDownloadErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateIsLectureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateStyleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateTagsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdatePatbasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateOnCreationDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateAutocheckTagErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateAutodoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, CourseExercisesPartialUpdateExpectedDurationErrorComponent):
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
        from ..models.course_exercises_partial_update_autocheck_tag_error_component import (
            CourseExercisesPartialUpdateAutocheckTagErrorComponent,
        )
        from ..models.course_exercises_partial_update_autodone_error_component import (
            CourseExercisesPartialUpdateAutodoneErrorComponent,
        )
        from ..models.course_exercises_partial_update_download_error_component import (
            CourseExercisesPartialUpdateDownloadErrorComponent,
        )
        from ..models.course_exercises_partial_update_expected_duration_error_component import (
            CourseExercisesPartialUpdateExpectedDurationErrorComponent,
        )
        from ..models.course_exercises_partial_update_is_lecture_error_component import (
            CourseExercisesPartialUpdateIsLectureErrorComponent,
        )
        from ..models.course_exercises_partial_update_name_error_component import (
            CourseExercisesPartialUpdateNameErrorComponent,
        )
        from ..models.course_exercises_partial_update_non_field_errors_error_component import (
            CourseExercisesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.course_exercises_partial_update_on_creation_data_error_component import (
            CourseExercisesPartialUpdateOnCreationDataErrorComponent,
        )
        from ..models.course_exercises_partial_update_order_error_component import (
            CourseExercisesPartialUpdateOrderErrorComponent,
        )
        from ..models.course_exercises_partial_update_parent_module_error_component import (
            CourseExercisesPartialUpdateParentModuleErrorComponent,
        )
        from ..models.course_exercises_partial_update_patbas_download_error_component import (
            CourseExercisesPartialUpdatePatbasDownloadErrorComponent,
        )
        from ..models.course_exercises_partial_update_patbas_error_component import (
            CourseExercisesPartialUpdatePatbasErrorComponent,
        )
        from ..models.course_exercises_partial_update_patbas_preview_error_component import (
            CourseExercisesPartialUpdatePatbasPreviewErrorComponent,
        )
        from ..models.course_exercises_partial_update_preview_error_component import (
            CourseExercisesPartialUpdatePreviewErrorComponent,
        )
        from ..models.course_exercises_partial_update_segel_brief_error_component import (
            CourseExercisesPartialUpdateSegelBriefErrorComponent,
        )
        from ..models.course_exercises_partial_update_style_error_component import (
            CourseExercisesPartialUpdateStyleErrorComponent,
        )
        from ..models.course_exercises_partial_update_tags_error_component import (
            CourseExercisesPartialUpdateTagsErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "CourseExercisesPartialUpdateAutocheckTagErrorComponent",
                "CourseExercisesPartialUpdateAutodoneErrorComponent",
                "CourseExercisesPartialUpdateDownloadErrorComponent",
                "CourseExercisesPartialUpdateExpectedDurationErrorComponent",
                "CourseExercisesPartialUpdateIsLectureErrorComponent",
                "CourseExercisesPartialUpdateNameErrorComponent",
                "CourseExercisesPartialUpdateNonFieldErrorsErrorComponent",
                "CourseExercisesPartialUpdateOnCreationDataErrorComponent",
                "CourseExercisesPartialUpdateOrderErrorComponent",
                "CourseExercisesPartialUpdateParentModuleErrorComponent",
                "CourseExercisesPartialUpdatePatbasDownloadErrorComponent",
                "CourseExercisesPartialUpdatePatbasErrorComponent",
                "CourseExercisesPartialUpdatePatbasPreviewErrorComponent",
                "CourseExercisesPartialUpdatePreviewErrorComponent",
                "CourseExercisesPartialUpdateSegelBriefErrorComponent",
                "CourseExercisesPartialUpdateStyleErrorComponent",
                "CourseExercisesPartialUpdateTagsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_0 = (
                        CourseExercisesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_1 = (
                        CourseExercisesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_2 = (
                        CourseExercisesPartialUpdateParentModuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_3 = (
                        CourseExercisesPartialUpdateDownloadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_4 = (
                        CourseExercisesPartialUpdatePreviewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_5 = (
                        CourseExercisesPartialUpdatePatbasPreviewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_6 = (
                        CourseExercisesPartialUpdatePatbasDownloadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_7 = (
                        CourseExercisesPartialUpdateIsLectureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_8 = (
                        CourseExercisesPartialUpdateStyleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_9 = (
                        CourseExercisesPartialUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_10 = (
                        CourseExercisesPartialUpdateTagsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_11 = (
                        CourseExercisesPartialUpdatePatbasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_12 = (
                        CourseExercisesPartialUpdateOnCreationDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_13 = (
                        CourseExercisesPartialUpdateAutocheckTagErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_14 = (
                        CourseExercisesPartialUpdateAutodoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_course_exercises_partial_update_error_type_15 = (
                        CourseExercisesPartialUpdateExpectedDurationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_course_exercises_partial_update_error_type_15
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_exercises_partial_update_error_type_16 = (
                    CourseExercisesPartialUpdateSegelBriefErrorComponent.from_dict(data)
                )

                return componentsschemas_course_exercises_partial_update_error_type_16

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        course_exercises_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        course_exercises_partial_update_validation_error.additional_properties = d
        return course_exercises_partial_update_validation_error

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
