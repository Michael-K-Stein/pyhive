from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_users_partial_update_avatar_error_component import (
        ManagementUsersPartialUpdateAvatarErrorComponent,
    )
    from ..models.management_users_partial_update_avatar_filename_error_component import (
        ManagementUsersPartialUpdateAvatarFilenameErrorComponent,
    )
    from ..models.management_users_partial_update_checkers_brief_error_component import (
        ManagementUsersPartialUpdateCheckersBriefErrorComponent,
    )
    from ..models.management_users_partial_update_classes_error_component import (
        ManagementUsersPartialUpdateClassesErrorComponent,
    )
    from ..models.management_users_partial_update_clearance_error_component import (
        ManagementUsersPartialUpdateClearanceErrorComponent,
    )
    from ..models.management_users_partial_update_confirmed_error_component import (
        ManagementUsersPartialUpdateConfirmedErrorComponent,
    )
    from ..models.management_users_partial_update_disable_queue_error_component import (
        ManagementUsersPartialUpdateDisableQueueErrorComponent,
    )
    from ..models.management_users_partial_update_disable_user_queue_error_component import (
        ManagementUsersPartialUpdateDisableUserQueueErrorComponent,
    )
    from ..models.management_users_partial_update_first_name_error_component import (
        ManagementUsersPartialUpdateFirstNameErrorComponent,
    )
    from ..models.management_users_partial_update_gender_error_component import (
        ManagementUsersPartialUpdateGenderErrorComponent,
    )
    from ..models.management_users_partial_update_hostname_error_component import (
        ManagementUsersPartialUpdateHostnameErrorComponent,
    )
    from ..models.management_users_partial_update_last_name_error_component import (
        ManagementUsersPartialUpdateLastNameErrorComponent,
    )
    from ..models.management_users_partial_update_mentees_error_component import (
        ManagementUsersPartialUpdateMenteesErrorComponent,
    )
    from ..models.management_users_partial_update_mentor_error_component import (
        ManagementUsersPartialUpdateMentorErrorComponent,
    )
    from ..models.management_users_partial_update_non_field_errors_error_component import (
        ManagementUsersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_users_partial_update_number_error_component import (
        ManagementUsersPartialUpdateNumberErrorComponent,
    )
    from ..models.management_users_partial_update_override_queue_error_component import (
        ManagementUsersPartialUpdateOverrideQueueErrorComponent,
    )
    from ..models.management_users_partial_update_password_error_component import (
        ManagementUsersPartialUpdatePasswordErrorComponent,
    )
    from ..models.management_users_partial_update_program_error_component import (
        ManagementUsersPartialUpdateProgramErrorComponent,
    )
    from ..models.management_users_partial_update_queue_error_component import (
        ManagementUsersPartialUpdateQueueErrorComponent,
    )
    from ..models.management_users_partial_update_status_error_component import (
        ManagementUsersPartialUpdateStatusErrorComponent,
    )
    from ..models.management_users_partial_update_teacher_error_component import (
        ManagementUsersPartialUpdateTeacherErrorComponent,
    )
    from ..models.management_users_partial_update_user_queue_error_component import (
        ManagementUsersPartialUpdateUserQueueErrorComponent,
    )
    from ..models.management_users_partial_update_username_error_component import (
        ManagementUsersPartialUpdateUsernameErrorComponent,
    )


T = TypeVar("T", bound="ManagementUsersPartialUpdateValidationError")


@_attrs_define
class ManagementUsersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementUsersPartialUpdateAvatarErrorComponent',
            'ManagementUsersPartialUpdateAvatarFilenameErrorComponent',
            'ManagementUsersPartialUpdateCheckersBriefErrorComponent', 'ManagementUsersPartialUpdateClassesErrorComponent',
            'ManagementUsersPartialUpdateClearanceErrorComponent', 'ManagementUsersPartialUpdateConfirmedErrorComponent',
            'ManagementUsersPartialUpdateDisableQueueErrorComponent',
            'ManagementUsersPartialUpdateDisableUserQueueErrorComponent',
            'ManagementUsersPartialUpdateFirstNameErrorComponent', 'ManagementUsersPartialUpdateGenderErrorComponent',
            'ManagementUsersPartialUpdateHostnameErrorComponent', 'ManagementUsersPartialUpdateLastNameErrorComponent',
            'ManagementUsersPartialUpdateMenteesErrorComponent', 'ManagementUsersPartialUpdateMentorErrorComponent',
            'ManagementUsersPartialUpdateNonFieldErrorsErrorComponent', 'ManagementUsersPartialUpdateNumberErrorComponent',
            'ManagementUsersPartialUpdateOverrideQueueErrorComponent', 'ManagementUsersPartialUpdatePasswordErrorComponent',
            'ManagementUsersPartialUpdateProgramErrorComponent', 'ManagementUsersPartialUpdateQueueErrorComponent',
            'ManagementUsersPartialUpdateStatusErrorComponent', 'ManagementUsersPartialUpdateTeacherErrorComponent',
            'ManagementUsersPartialUpdateUserQueueErrorComponent', 'ManagementUsersPartialUpdateUsernameErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementUsersPartialUpdateAvatarErrorComponent",
            "ManagementUsersPartialUpdateAvatarFilenameErrorComponent",
            "ManagementUsersPartialUpdateCheckersBriefErrorComponent",
            "ManagementUsersPartialUpdateClassesErrorComponent",
            "ManagementUsersPartialUpdateClearanceErrorComponent",
            "ManagementUsersPartialUpdateConfirmedErrorComponent",
            "ManagementUsersPartialUpdateDisableQueueErrorComponent",
            "ManagementUsersPartialUpdateDisableUserQueueErrorComponent",
            "ManagementUsersPartialUpdateFirstNameErrorComponent",
            "ManagementUsersPartialUpdateGenderErrorComponent",
            "ManagementUsersPartialUpdateHostnameErrorComponent",
            "ManagementUsersPartialUpdateLastNameErrorComponent",
            "ManagementUsersPartialUpdateMenteesErrorComponent",
            "ManagementUsersPartialUpdateMentorErrorComponent",
            "ManagementUsersPartialUpdateNonFieldErrorsErrorComponent",
            "ManagementUsersPartialUpdateNumberErrorComponent",
            "ManagementUsersPartialUpdateOverrideQueueErrorComponent",
            "ManagementUsersPartialUpdatePasswordErrorComponent",
            "ManagementUsersPartialUpdateProgramErrorComponent",
            "ManagementUsersPartialUpdateQueueErrorComponent",
            "ManagementUsersPartialUpdateStatusErrorComponent",
            "ManagementUsersPartialUpdateTeacherErrorComponent",
            "ManagementUsersPartialUpdateUserQueueErrorComponent",
            "ManagementUsersPartialUpdateUsernameErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_users_partial_update_avatar_error_component import (
            ManagementUsersPartialUpdateAvatarErrorComponent,
        )
        from ..models.management_users_partial_update_avatar_filename_error_component import (
            ManagementUsersPartialUpdateAvatarFilenameErrorComponent,
        )
        from ..models.management_users_partial_update_checkers_brief_error_component import (
            ManagementUsersPartialUpdateCheckersBriefErrorComponent,
        )
        from ..models.management_users_partial_update_classes_error_component import (
            ManagementUsersPartialUpdateClassesErrorComponent,
        )
        from ..models.management_users_partial_update_clearance_error_component import (
            ManagementUsersPartialUpdateClearanceErrorComponent,
        )
        from ..models.management_users_partial_update_confirmed_error_component import (
            ManagementUsersPartialUpdateConfirmedErrorComponent,
        )
        from ..models.management_users_partial_update_disable_queue_error_component import (
            ManagementUsersPartialUpdateDisableQueueErrorComponent,
        )
        from ..models.management_users_partial_update_disable_user_queue_error_component import (
            ManagementUsersPartialUpdateDisableUserQueueErrorComponent,
        )
        from ..models.management_users_partial_update_first_name_error_component import (
            ManagementUsersPartialUpdateFirstNameErrorComponent,
        )
        from ..models.management_users_partial_update_gender_error_component import (
            ManagementUsersPartialUpdateGenderErrorComponent,
        )
        from ..models.management_users_partial_update_hostname_error_component import (
            ManagementUsersPartialUpdateHostnameErrorComponent,
        )
        from ..models.management_users_partial_update_last_name_error_component import (
            ManagementUsersPartialUpdateLastNameErrorComponent,
        )
        from ..models.management_users_partial_update_mentees_error_component import (
            ManagementUsersPartialUpdateMenteesErrorComponent,
        )
        from ..models.management_users_partial_update_mentor_error_component import (
            ManagementUsersPartialUpdateMentorErrorComponent,
        )
        from ..models.management_users_partial_update_non_field_errors_error_component import (
            ManagementUsersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_partial_update_number_error_component import (
            ManagementUsersPartialUpdateNumberErrorComponent,
        )
        from ..models.management_users_partial_update_override_queue_error_component import (
            ManagementUsersPartialUpdateOverrideQueueErrorComponent,
        )
        from ..models.management_users_partial_update_program_error_component import (
            ManagementUsersPartialUpdateProgramErrorComponent,
        )
        from ..models.management_users_partial_update_queue_error_component import (
            ManagementUsersPartialUpdateQueueErrorComponent,
        )
        from ..models.management_users_partial_update_status_error_component import (
            ManagementUsersPartialUpdateStatusErrorComponent,
        )
        from ..models.management_users_partial_update_teacher_error_component import (
            ManagementUsersPartialUpdateTeacherErrorComponent,
        )
        from ..models.management_users_partial_update_user_queue_error_component import (
            ManagementUsersPartialUpdateUserQueueErrorComponent,
        )
        from ..models.management_users_partial_update_username_error_component import (
            ManagementUsersPartialUpdateUsernameErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementUsersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateClearanceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateAvatarErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateAvatarFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateGenderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateProgramErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateCheckersBriefErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateMentorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateMenteesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateUsernameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateDisableQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateUserQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateDisableUserQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateOverrideQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateConfirmedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateTeacherErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersPartialUpdateHostnameErrorComponent):
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
        from ..models.management_users_partial_update_avatar_error_component import (
            ManagementUsersPartialUpdateAvatarErrorComponent,
        )
        from ..models.management_users_partial_update_avatar_filename_error_component import (
            ManagementUsersPartialUpdateAvatarFilenameErrorComponent,
        )
        from ..models.management_users_partial_update_checkers_brief_error_component import (
            ManagementUsersPartialUpdateCheckersBriefErrorComponent,
        )
        from ..models.management_users_partial_update_classes_error_component import (
            ManagementUsersPartialUpdateClassesErrorComponent,
        )
        from ..models.management_users_partial_update_clearance_error_component import (
            ManagementUsersPartialUpdateClearanceErrorComponent,
        )
        from ..models.management_users_partial_update_confirmed_error_component import (
            ManagementUsersPartialUpdateConfirmedErrorComponent,
        )
        from ..models.management_users_partial_update_disable_queue_error_component import (
            ManagementUsersPartialUpdateDisableQueueErrorComponent,
        )
        from ..models.management_users_partial_update_disable_user_queue_error_component import (
            ManagementUsersPartialUpdateDisableUserQueueErrorComponent,
        )
        from ..models.management_users_partial_update_first_name_error_component import (
            ManagementUsersPartialUpdateFirstNameErrorComponent,
        )
        from ..models.management_users_partial_update_gender_error_component import (
            ManagementUsersPartialUpdateGenderErrorComponent,
        )
        from ..models.management_users_partial_update_hostname_error_component import (
            ManagementUsersPartialUpdateHostnameErrorComponent,
        )
        from ..models.management_users_partial_update_last_name_error_component import (
            ManagementUsersPartialUpdateLastNameErrorComponent,
        )
        from ..models.management_users_partial_update_mentees_error_component import (
            ManagementUsersPartialUpdateMenteesErrorComponent,
        )
        from ..models.management_users_partial_update_mentor_error_component import (
            ManagementUsersPartialUpdateMentorErrorComponent,
        )
        from ..models.management_users_partial_update_non_field_errors_error_component import (
            ManagementUsersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_partial_update_number_error_component import (
            ManagementUsersPartialUpdateNumberErrorComponent,
        )
        from ..models.management_users_partial_update_override_queue_error_component import (
            ManagementUsersPartialUpdateOverrideQueueErrorComponent,
        )
        from ..models.management_users_partial_update_password_error_component import (
            ManagementUsersPartialUpdatePasswordErrorComponent,
        )
        from ..models.management_users_partial_update_program_error_component import (
            ManagementUsersPartialUpdateProgramErrorComponent,
        )
        from ..models.management_users_partial_update_queue_error_component import (
            ManagementUsersPartialUpdateQueueErrorComponent,
        )
        from ..models.management_users_partial_update_status_error_component import (
            ManagementUsersPartialUpdateStatusErrorComponent,
        )
        from ..models.management_users_partial_update_teacher_error_component import (
            ManagementUsersPartialUpdateTeacherErrorComponent,
        )
        from ..models.management_users_partial_update_user_queue_error_component import (
            ManagementUsersPartialUpdateUserQueueErrorComponent,
        )
        from ..models.management_users_partial_update_username_error_component import (
            ManagementUsersPartialUpdateUsernameErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementUsersPartialUpdateAvatarErrorComponent",
                "ManagementUsersPartialUpdateAvatarFilenameErrorComponent",
                "ManagementUsersPartialUpdateCheckersBriefErrorComponent",
                "ManagementUsersPartialUpdateClassesErrorComponent",
                "ManagementUsersPartialUpdateClearanceErrorComponent",
                "ManagementUsersPartialUpdateConfirmedErrorComponent",
                "ManagementUsersPartialUpdateDisableQueueErrorComponent",
                "ManagementUsersPartialUpdateDisableUserQueueErrorComponent",
                "ManagementUsersPartialUpdateFirstNameErrorComponent",
                "ManagementUsersPartialUpdateGenderErrorComponent",
                "ManagementUsersPartialUpdateHostnameErrorComponent",
                "ManagementUsersPartialUpdateLastNameErrorComponent",
                "ManagementUsersPartialUpdateMenteesErrorComponent",
                "ManagementUsersPartialUpdateMentorErrorComponent",
                "ManagementUsersPartialUpdateNonFieldErrorsErrorComponent",
                "ManagementUsersPartialUpdateNumberErrorComponent",
                "ManagementUsersPartialUpdateOverrideQueueErrorComponent",
                "ManagementUsersPartialUpdatePasswordErrorComponent",
                "ManagementUsersPartialUpdateProgramErrorComponent",
                "ManagementUsersPartialUpdateQueueErrorComponent",
                "ManagementUsersPartialUpdateStatusErrorComponent",
                "ManagementUsersPartialUpdateTeacherErrorComponent",
                "ManagementUsersPartialUpdateUserQueueErrorComponent",
                "ManagementUsersPartialUpdateUsernameErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_0 = (
                        ManagementUsersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_1 = (
                        ManagementUsersPartialUpdateClearanceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_2 = (
                        ManagementUsersPartialUpdateAvatarErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_3 = (
                        ManagementUsersPartialUpdateAvatarFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_4 = (
                        ManagementUsersPartialUpdateGenderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_5 = (
                        ManagementUsersPartialUpdateNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_6 = (
                        ManagementUsersPartialUpdateProgramErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_7 = (
                        ManagementUsersPartialUpdateCheckersBriefErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_8 = (
                        ManagementUsersPartialUpdateMentorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_9 = (
                        ManagementUsersPartialUpdateClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_10 = (
                        ManagementUsersPartialUpdateMenteesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_11 = (
                        ManagementUsersPartialUpdateUsernameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_12 = (
                        ManagementUsersPartialUpdateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_13 = (
                        ManagementUsersPartialUpdateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_14 = (
                        ManagementUsersPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_15 = (
                        ManagementUsersPartialUpdateQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_16 = (
                        ManagementUsersPartialUpdateDisableQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_17 = (
                        ManagementUsersPartialUpdateUserQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_18 = (
                        ManagementUsersPartialUpdateDisableUserQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_19 = (
                        ManagementUsersPartialUpdateOverrideQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_20 = (
                        ManagementUsersPartialUpdateConfirmedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_21 = (
                        ManagementUsersPartialUpdateTeacherErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_partial_update_error_type_22 = (
                        ManagementUsersPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_partial_update_error_type_22
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_users_partial_update_error_type_23 = (
                    ManagementUsersPartialUpdatePasswordErrorComponent.from_dict(data)
                )

                return componentsschemas_management_users_partial_update_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_users_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_users_partial_update_validation_error.additional_properties = d
        return management_users_partial_update_validation_error

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
