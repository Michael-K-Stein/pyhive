from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_list_created_by_error_component import HelpListCreatedByErrorComponent
    from ..models.help_list_for_exercise_id_error_component import HelpListForExerciseIdErrorComponent
    from ..models.help_list_for_exercise_parent_module_id_error_component import (
        HelpListForExerciseParentModuleIdErrorComponent,
    )
    from ..models.help_list_for_exercise_parent_module_parent_subject_id_error_component import (
        HelpListForExerciseParentModuleParentSubjectIdErrorComponent,
    )
    from ..models.help_list_free_text_error_component import HelpListFreeTextErrorComponent
    from ..models.help_list_help_status_in_error_component import HelpListHelpStatusInErrorComponent
    from ..models.help_list_help_type_in_error_component import HelpListHelpTypeInErrorComponent
    from ..models.help_list_user_classes_id_error_component import HelpListUserClassesIdErrorComponent
    from ..models.help_list_user_classes_id_in_error_component import HelpListUserClassesIdInErrorComponent
    from ..models.help_list_user_id_in_error_component import HelpListUserIdInErrorComponent
    from ..models.help_list_user_mentor_id_error_component import HelpListUserMentorIdErrorComponent
    from ..models.help_list_user_mentor_id_in_error_component import HelpListUserMentorIdInErrorComponent
    from ..models.help_list_user_program_id_in_error_component import HelpListUserProgramIdInErrorComponent


T = TypeVar("T", bound="HelpListValidationError")


@_attrs_define
class HelpListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpListCreatedByErrorComponent', 'HelpListForExerciseIdErrorComponent',
            'HelpListForExerciseParentModuleIdErrorComponent',
            'HelpListForExerciseParentModuleParentSubjectIdErrorComponent', 'HelpListFreeTextErrorComponent',
            'HelpListHelpStatusInErrorComponent', 'HelpListHelpTypeInErrorComponent', 'HelpListUserClassesIdErrorComponent',
            'HelpListUserClassesIdInErrorComponent', 'HelpListUserIdInErrorComponent', 'HelpListUserMentorIdErrorComponent',
            'HelpListUserMentorIdInErrorComponent', 'HelpListUserProgramIdInErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpListCreatedByErrorComponent",
            "HelpListForExerciseIdErrorComponent",
            "HelpListForExerciseParentModuleIdErrorComponent",
            "HelpListForExerciseParentModuleParentSubjectIdErrorComponent",
            "HelpListFreeTextErrorComponent",
            "HelpListHelpStatusInErrorComponent",
            "HelpListHelpTypeInErrorComponent",
            "HelpListUserClassesIdErrorComponent",
            "HelpListUserClassesIdInErrorComponent",
            "HelpListUserIdInErrorComponent",
            "HelpListUserMentorIdErrorComponent",
            "HelpListUserMentorIdInErrorComponent",
            "HelpListUserProgramIdInErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_list_for_exercise_id_error_component import HelpListForExerciseIdErrorComponent
        from ..models.help_list_for_exercise_parent_module_id_error_component import (
            HelpListForExerciseParentModuleIdErrorComponent,
        )
        from ..models.help_list_for_exercise_parent_module_parent_subject_id_error_component import (
            HelpListForExerciseParentModuleParentSubjectIdErrorComponent,
        )
        from ..models.help_list_free_text_error_component import HelpListFreeTextErrorComponent
        from ..models.help_list_help_status_in_error_component import HelpListHelpStatusInErrorComponent
        from ..models.help_list_help_type_in_error_component import HelpListHelpTypeInErrorComponent
        from ..models.help_list_user_classes_id_error_component import HelpListUserClassesIdErrorComponent
        from ..models.help_list_user_classes_id_in_error_component import HelpListUserClassesIdInErrorComponent
        from ..models.help_list_user_id_in_error_component import HelpListUserIdInErrorComponent
        from ..models.help_list_user_mentor_id_error_component import HelpListUserMentorIdErrorComponent
        from ..models.help_list_user_mentor_id_in_error_component import HelpListUserMentorIdInErrorComponent
        from ..models.help_list_user_program_id_in_error_component import HelpListUserProgramIdInErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpListHelpStatusInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListHelpTypeInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListForExerciseIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListUserIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListForExerciseParentModuleIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListForExerciseParentModuleParentSubjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListUserProgramIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListUserClassesIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListUserClassesIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListUserMentorIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListUserMentorIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpListFreeTextErrorComponent):
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
        from ..models.help_list_created_by_error_component import HelpListCreatedByErrorComponent
        from ..models.help_list_for_exercise_id_error_component import HelpListForExerciseIdErrorComponent
        from ..models.help_list_for_exercise_parent_module_id_error_component import (
            HelpListForExerciseParentModuleIdErrorComponent,
        )
        from ..models.help_list_for_exercise_parent_module_parent_subject_id_error_component import (
            HelpListForExerciseParentModuleParentSubjectIdErrorComponent,
        )
        from ..models.help_list_free_text_error_component import HelpListFreeTextErrorComponent
        from ..models.help_list_help_status_in_error_component import HelpListHelpStatusInErrorComponent
        from ..models.help_list_help_type_in_error_component import HelpListHelpTypeInErrorComponent
        from ..models.help_list_user_classes_id_error_component import HelpListUserClassesIdErrorComponent
        from ..models.help_list_user_classes_id_in_error_component import HelpListUserClassesIdInErrorComponent
        from ..models.help_list_user_id_in_error_component import HelpListUserIdInErrorComponent
        from ..models.help_list_user_mentor_id_error_component import HelpListUserMentorIdErrorComponent
        from ..models.help_list_user_mentor_id_in_error_component import HelpListUserMentorIdInErrorComponent
        from ..models.help_list_user_program_id_in_error_component import HelpListUserProgramIdInErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpListCreatedByErrorComponent",
                "HelpListForExerciseIdErrorComponent",
                "HelpListForExerciseParentModuleIdErrorComponent",
                "HelpListForExerciseParentModuleParentSubjectIdErrorComponent",
                "HelpListFreeTextErrorComponent",
                "HelpListHelpStatusInErrorComponent",
                "HelpListHelpTypeInErrorComponent",
                "HelpListUserClassesIdErrorComponent",
                "HelpListUserClassesIdInErrorComponent",
                "HelpListUserIdInErrorComponent",
                "HelpListUserMentorIdErrorComponent",
                "HelpListUserMentorIdInErrorComponent",
                "HelpListUserProgramIdInErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_0 = HelpListHelpStatusInErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_1 = HelpListHelpTypeInErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_2 = HelpListForExerciseIdErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_3 = HelpListUserIdInErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_4 = (
                        HelpListForExerciseParentModuleIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_list_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_5 = (
                        HelpListForExerciseParentModuleParentSubjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_list_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_6 = HelpListUserProgramIdInErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_7 = HelpListUserClassesIdErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_8 = HelpListUserClassesIdInErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_9 = HelpListUserMentorIdErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_10 = HelpListUserMentorIdInErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_list_error_type_11 = HelpListFreeTextErrorComponent.from_dict(data)

                    return componentsschemas_help_list_error_type_11
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_list_error_type_12 = HelpListCreatedByErrorComponent.from_dict(data)

                return componentsschemas_help_list_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_list_validation_error.additional_properties = d
        return help_list_validation_error

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
