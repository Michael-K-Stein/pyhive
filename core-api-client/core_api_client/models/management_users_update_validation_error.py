from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_users_update_avatar_error_component import ManagementUsersUpdateAvatarErrorComponent
    from ..models.management_users_update_avatar_filename_error_component import (
        ManagementUsersUpdateAvatarFilenameErrorComponent,
    )
    from ..models.management_users_update_checkers_brief_error_component import (
        ManagementUsersUpdateCheckersBriefErrorComponent,
    )
    from ..models.management_users_update_classes_error_component import ManagementUsersUpdateClassesErrorComponent
    from ..models.management_users_update_clearance_error_component import ManagementUsersUpdateClearanceErrorComponent
    from ..models.management_users_update_confirmed_error_component import ManagementUsersUpdateConfirmedErrorComponent
    from ..models.management_users_update_disable_queue_error_component import (
        ManagementUsersUpdateDisableQueueErrorComponent,
    )
    from ..models.management_users_update_disable_user_queue_error_component import (
        ManagementUsersUpdateDisableUserQueueErrorComponent,
    )
    from ..models.management_users_update_first_name_error_component import ManagementUsersUpdateFirstNameErrorComponent
    from ..models.management_users_update_gender_error_component import ManagementUsersUpdateGenderErrorComponent
    from ..models.management_users_update_hostname_error_component import ManagementUsersUpdateHostnameErrorComponent
    from ..models.management_users_update_last_name_error_component import ManagementUsersUpdateLastNameErrorComponent
    from ..models.management_users_update_mentees_error_component import ManagementUsersUpdateMenteesErrorComponent
    from ..models.management_users_update_mentor_error_component import ManagementUsersUpdateMentorErrorComponent
    from ..models.management_users_update_non_field_errors_error_component import (
        ManagementUsersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_users_update_number_error_component import ManagementUsersUpdateNumberErrorComponent
    from ..models.management_users_update_override_queue_error_component import (
        ManagementUsersUpdateOverrideQueueErrorComponent,
    )
    from ..models.management_users_update_password_error_component import ManagementUsersUpdatePasswordErrorComponent
    from ..models.management_users_update_program_error_component import ManagementUsersUpdateProgramErrorComponent
    from ..models.management_users_update_queue_error_component import ManagementUsersUpdateQueueErrorComponent
    from ..models.management_users_update_status_error_component import ManagementUsersUpdateStatusErrorComponent
    from ..models.management_users_update_teacher_error_component import ManagementUsersUpdateTeacherErrorComponent
    from ..models.management_users_update_user_queue_error_component import ManagementUsersUpdateUserQueueErrorComponent
    from ..models.management_users_update_username_error_component import ManagementUsersUpdateUsernameErrorComponent


T = TypeVar("T", bound="ManagementUsersUpdateValidationError")


@_attrs_define
class ManagementUsersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementUsersUpdateAvatarErrorComponent',
            'ManagementUsersUpdateAvatarFilenameErrorComponent', 'ManagementUsersUpdateCheckersBriefErrorComponent',
            'ManagementUsersUpdateClassesErrorComponent', 'ManagementUsersUpdateClearanceErrorComponent',
            'ManagementUsersUpdateConfirmedErrorComponent', 'ManagementUsersUpdateDisableQueueErrorComponent',
            'ManagementUsersUpdateDisableUserQueueErrorComponent', 'ManagementUsersUpdateFirstNameErrorComponent',
            'ManagementUsersUpdateGenderErrorComponent', 'ManagementUsersUpdateHostnameErrorComponent',
            'ManagementUsersUpdateLastNameErrorComponent', 'ManagementUsersUpdateMenteesErrorComponent',
            'ManagementUsersUpdateMentorErrorComponent', 'ManagementUsersUpdateNonFieldErrorsErrorComponent',
            'ManagementUsersUpdateNumberErrorComponent', 'ManagementUsersUpdateOverrideQueueErrorComponent',
            'ManagementUsersUpdatePasswordErrorComponent', 'ManagementUsersUpdateProgramErrorComponent',
            'ManagementUsersUpdateQueueErrorComponent', 'ManagementUsersUpdateStatusErrorComponent',
            'ManagementUsersUpdateTeacherErrorComponent', 'ManagementUsersUpdateUserQueueErrorComponent',
            'ManagementUsersUpdateUsernameErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementUsersUpdateAvatarErrorComponent",
            "ManagementUsersUpdateAvatarFilenameErrorComponent",
            "ManagementUsersUpdateCheckersBriefErrorComponent",
            "ManagementUsersUpdateClassesErrorComponent",
            "ManagementUsersUpdateClearanceErrorComponent",
            "ManagementUsersUpdateConfirmedErrorComponent",
            "ManagementUsersUpdateDisableQueueErrorComponent",
            "ManagementUsersUpdateDisableUserQueueErrorComponent",
            "ManagementUsersUpdateFirstNameErrorComponent",
            "ManagementUsersUpdateGenderErrorComponent",
            "ManagementUsersUpdateHostnameErrorComponent",
            "ManagementUsersUpdateLastNameErrorComponent",
            "ManagementUsersUpdateMenteesErrorComponent",
            "ManagementUsersUpdateMentorErrorComponent",
            "ManagementUsersUpdateNonFieldErrorsErrorComponent",
            "ManagementUsersUpdateNumberErrorComponent",
            "ManagementUsersUpdateOverrideQueueErrorComponent",
            "ManagementUsersUpdatePasswordErrorComponent",
            "ManagementUsersUpdateProgramErrorComponent",
            "ManagementUsersUpdateQueueErrorComponent",
            "ManagementUsersUpdateStatusErrorComponent",
            "ManagementUsersUpdateTeacherErrorComponent",
            "ManagementUsersUpdateUserQueueErrorComponent",
            "ManagementUsersUpdateUsernameErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_users_update_avatar_error_component import ManagementUsersUpdateAvatarErrorComponent
        from ..models.management_users_update_avatar_filename_error_component import (
            ManagementUsersUpdateAvatarFilenameErrorComponent,
        )
        from ..models.management_users_update_checkers_brief_error_component import (
            ManagementUsersUpdateCheckersBriefErrorComponent,
        )
        from ..models.management_users_update_classes_error_component import ManagementUsersUpdateClassesErrorComponent
        from ..models.management_users_update_clearance_error_component import (
            ManagementUsersUpdateClearanceErrorComponent,
        )
        from ..models.management_users_update_confirmed_error_component import (
            ManagementUsersUpdateConfirmedErrorComponent,
        )
        from ..models.management_users_update_disable_queue_error_component import (
            ManagementUsersUpdateDisableQueueErrorComponent,
        )
        from ..models.management_users_update_disable_user_queue_error_component import (
            ManagementUsersUpdateDisableUserQueueErrorComponent,
        )
        from ..models.management_users_update_first_name_error_component import (
            ManagementUsersUpdateFirstNameErrorComponent,
        )
        from ..models.management_users_update_gender_error_component import ManagementUsersUpdateGenderErrorComponent
        from ..models.management_users_update_hostname_error_component import (
            ManagementUsersUpdateHostnameErrorComponent,
        )
        from ..models.management_users_update_last_name_error_component import (
            ManagementUsersUpdateLastNameErrorComponent,
        )
        from ..models.management_users_update_mentees_error_component import ManagementUsersUpdateMenteesErrorComponent
        from ..models.management_users_update_mentor_error_component import ManagementUsersUpdateMentorErrorComponent
        from ..models.management_users_update_non_field_errors_error_component import (
            ManagementUsersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_update_number_error_component import ManagementUsersUpdateNumberErrorComponent
        from ..models.management_users_update_override_queue_error_component import (
            ManagementUsersUpdateOverrideQueueErrorComponent,
        )
        from ..models.management_users_update_program_error_component import ManagementUsersUpdateProgramErrorComponent
        from ..models.management_users_update_queue_error_component import ManagementUsersUpdateQueueErrorComponent
        from ..models.management_users_update_status_error_component import ManagementUsersUpdateStatusErrorComponent
        from ..models.management_users_update_teacher_error_component import ManagementUsersUpdateTeacherErrorComponent
        from ..models.management_users_update_user_queue_error_component import (
            ManagementUsersUpdateUserQueueErrorComponent,
        )
        from ..models.management_users_update_username_error_component import (
            ManagementUsersUpdateUsernameErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementUsersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateClearanceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateAvatarErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateAvatarFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateGenderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateProgramErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateCheckersBriefErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateMentorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateMenteesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateUsernameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateDisableQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateUserQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateDisableUserQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateOverrideQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateConfirmedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateTeacherErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersUpdateHostnameErrorComponent):
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
        from ..models.management_users_update_avatar_error_component import ManagementUsersUpdateAvatarErrorComponent
        from ..models.management_users_update_avatar_filename_error_component import (
            ManagementUsersUpdateAvatarFilenameErrorComponent,
        )
        from ..models.management_users_update_checkers_brief_error_component import (
            ManagementUsersUpdateCheckersBriefErrorComponent,
        )
        from ..models.management_users_update_classes_error_component import ManagementUsersUpdateClassesErrorComponent
        from ..models.management_users_update_clearance_error_component import (
            ManagementUsersUpdateClearanceErrorComponent,
        )
        from ..models.management_users_update_confirmed_error_component import (
            ManagementUsersUpdateConfirmedErrorComponent,
        )
        from ..models.management_users_update_disable_queue_error_component import (
            ManagementUsersUpdateDisableQueueErrorComponent,
        )
        from ..models.management_users_update_disable_user_queue_error_component import (
            ManagementUsersUpdateDisableUserQueueErrorComponent,
        )
        from ..models.management_users_update_first_name_error_component import (
            ManagementUsersUpdateFirstNameErrorComponent,
        )
        from ..models.management_users_update_gender_error_component import ManagementUsersUpdateGenderErrorComponent
        from ..models.management_users_update_hostname_error_component import (
            ManagementUsersUpdateHostnameErrorComponent,
        )
        from ..models.management_users_update_last_name_error_component import (
            ManagementUsersUpdateLastNameErrorComponent,
        )
        from ..models.management_users_update_mentees_error_component import ManagementUsersUpdateMenteesErrorComponent
        from ..models.management_users_update_mentor_error_component import ManagementUsersUpdateMentorErrorComponent
        from ..models.management_users_update_non_field_errors_error_component import (
            ManagementUsersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_update_number_error_component import ManagementUsersUpdateNumberErrorComponent
        from ..models.management_users_update_override_queue_error_component import (
            ManagementUsersUpdateOverrideQueueErrorComponent,
        )
        from ..models.management_users_update_password_error_component import (
            ManagementUsersUpdatePasswordErrorComponent,
        )
        from ..models.management_users_update_program_error_component import ManagementUsersUpdateProgramErrorComponent
        from ..models.management_users_update_queue_error_component import ManagementUsersUpdateQueueErrorComponent
        from ..models.management_users_update_status_error_component import ManagementUsersUpdateStatusErrorComponent
        from ..models.management_users_update_teacher_error_component import ManagementUsersUpdateTeacherErrorComponent
        from ..models.management_users_update_user_queue_error_component import (
            ManagementUsersUpdateUserQueueErrorComponent,
        )
        from ..models.management_users_update_username_error_component import (
            ManagementUsersUpdateUsernameErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementUsersUpdateAvatarErrorComponent",
                "ManagementUsersUpdateAvatarFilenameErrorComponent",
                "ManagementUsersUpdateCheckersBriefErrorComponent",
                "ManagementUsersUpdateClassesErrorComponent",
                "ManagementUsersUpdateClearanceErrorComponent",
                "ManagementUsersUpdateConfirmedErrorComponent",
                "ManagementUsersUpdateDisableQueueErrorComponent",
                "ManagementUsersUpdateDisableUserQueueErrorComponent",
                "ManagementUsersUpdateFirstNameErrorComponent",
                "ManagementUsersUpdateGenderErrorComponent",
                "ManagementUsersUpdateHostnameErrorComponent",
                "ManagementUsersUpdateLastNameErrorComponent",
                "ManagementUsersUpdateMenteesErrorComponent",
                "ManagementUsersUpdateMentorErrorComponent",
                "ManagementUsersUpdateNonFieldErrorsErrorComponent",
                "ManagementUsersUpdateNumberErrorComponent",
                "ManagementUsersUpdateOverrideQueueErrorComponent",
                "ManagementUsersUpdatePasswordErrorComponent",
                "ManagementUsersUpdateProgramErrorComponent",
                "ManagementUsersUpdateQueueErrorComponent",
                "ManagementUsersUpdateStatusErrorComponent",
                "ManagementUsersUpdateTeacherErrorComponent",
                "ManagementUsersUpdateUserQueueErrorComponent",
                "ManagementUsersUpdateUsernameErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_0 = (
                        ManagementUsersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_1 = (
                        ManagementUsersUpdateClearanceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_2 = (
                        ManagementUsersUpdateAvatarErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_3 = (
                        ManagementUsersUpdateAvatarFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_4 = (
                        ManagementUsersUpdateGenderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_5 = (
                        ManagementUsersUpdateNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_6 = (
                        ManagementUsersUpdateProgramErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_7 = (
                        ManagementUsersUpdateCheckersBriefErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_8 = (
                        ManagementUsersUpdateMentorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_9 = (
                        ManagementUsersUpdateClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_10 = (
                        ManagementUsersUpdateMenteesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_11 = (
                        ManagementUsersUpdateUsernameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_12 = (
                        ManagementUsersUpdateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_13 = (
                        ManagementUsersUpdateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_14 = (
                        ManagementUsersUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_15 = (
                        ManagementUsersUpdateQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_16 = (
                        ManagementUsersUpdateDisableQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_17 = (
                        ManagementUsersUpdateUserQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_18 = (
                        ManagementUsersUpdateDisableUserQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_19 = (
                        ManagementUsersUpdateOverrideQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_20 = (
                        ManagementUsersUpdateConfirmedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_21 = (
                        ManagementUsersUpdateTeacherErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_update_error_type_22 = (
                        ManagementUsersUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_update_error_type_22
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_users_update_error_type_23 = (
                    ManagementUsersUpdatePasswordErrorComponent.from_dict(data)
                )

                return componentsschemas_management_users_update_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_users_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_users_update_validation_error.additional_properties = d
        return management_users_update_validation_error

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
