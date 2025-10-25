from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_users_create_avatar_error_component import ManagementUsersCreateAvatarErrorComponent
    from ..models.management_users_create_avatar_filename_error_component import (
        ManagementUsersCreateAvatarFilenameErrorComponent,
    )
    from ..models.management_users_create_checkers_brief_error_component import (
        ManagementUsersCreateCheckersBriefErrorComponent,
    )
    from ..models.management_users_create_classes_error_component import ManagementUsersCreateClassesErrorComponent
    from ..models.management_users_create_clearance_error_component import ManagementUsersCreateClearanceErrorComponent
    from ..models.management_users_create_confirmed_error_component import ManagementUsersCreateConfirmedErrorComponent
    from ..models.management_users_create_disable_queue_error_component import (
        ManagementUsersCreateDisableQueueErrorComponent,
    )
    from ..models.management_users_create_disable_user_queue_error_component import (
        ManagementUsersCreateDisableUserQueueErrorComponent,
    )
    from ..models.management_users_create_first_name_error_component import ManagementUsersCreateFirstNameErrorComponent
    from ..models.management_users_create_gender_error_component import ManagementUsersCreateGenderErrorComponent
    from ..models.management_users_create_hostname_error_component import ManagementUsersCreateHostnameErrorComponent
    from ..models.management_users_create_last_name_error_component import ManagementUsersCreateLastNameErrorComponent
    from ..models.management_users_create_mentees_error_component import ManagementUsersCreateMenteesErrorComponent
    from ..models.management_users_create_mentor_error_component import ManagementUsersCreateMentorErrorComponent
    from ..models.management_users_create_non_field_errors_error_component import (
        ManagementUsersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.management_users_create_number_error_component import ManagementUsersCreateNumberErrorComponent
    from ..models.management_users_create_override_queue_error_component import (
        ManagementUsersCreateOverrideQueueErrorComponent,
    )
    from ..models.management_users_create_password_error_component import ManagementUsersCreatePasswordErrorComponent
    from ..models.management_users_create_program_error_component import ManagementUsersCreateProgramErrorComponent
    from ..models.management_users_create_queue_error_component import ManagementUsersCreateQueueErrorComponent
    from ..models.management_users_create_status_error_component import ManagementUsersCreateStatusErrorComponent
    from ..models.management_users_create_teacher_error_component import ManagementUsersCreateTeacherErrorComponent
    from ..models.management_users_create_user_queue_error_component import ManagementUsersCreateUserQueueErrorComponent
    from ..models.management_users_create_username_error_component import ManagementUsersCreateUsernameErrorComponent


T = TypeVar("T", bound="ManagementUsersCreateValidationError")


@_attrs_define
class ManagementUsersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementUsersCreateAvatarErrorComponent',
            'ManagementUsersCreateAvatarFilenameErrorComponent', 'ManagementUsersCreateCheckersBriefErrorComponent',
            'ManagementUsersCreateClassesErrorComponent', 'ManagementUsersCreateClearanceErrorComponent',
            'ManagementUsersCreateConfirmedErrorComponent', 'ManagementUsersCreateDisableQueueErrorComponent',
            'ManagementUsersCreateDisableUserQueueErrorComponent', 'ManagementUsersCreateFirstNameErrorComponent',
            'ManagementUsersCreateGenderErrorComponent', 'ManagementUsersCreateHostnameErrorComponent',
            'ManagementUsersCreateLastNameErrorComponent', 'ManagementUsersCreateMenteesErrorComponent',
            'ManagementUsersCreateMentorErrorComponent', 'ManagementUsersCreateNonFieldErrorsErrorComponent',
            'ManagementUsersCreateNumberErrorComponent', 'ManagementUsersCreateOverrideQueueErrorComponent',
            'ManagementUsersCreatePasswordErrorComponent', 'ManagementUsersCreateProgramErrorComponent',
            'ManagementUsersCreateQueueErrorComponent', 'ManagementUsersCreateStatusErrorComponent',
            'ManagementUsersCreateTeacherErrorComponent', 'ManagementUsersCreateUserQueueErrorComponent',
            'ManagementUsersCreateUsernameErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementUsersCreateAvatarErrorComponent",
            "ManagementUsersCreateAvatarFilenameErrorComponent",
            "ManagementUsersCreateCheckersBriefErrorComponent",
            "ManagementUsersCreateClassesErrorComponent",
            "ManagementUsersCreateClearanceErrorComponent",
            "ManagementUsersCreateConfirmedErrorComponent",
            "ManagementUsersCreateDisableQueueErrorComponent",
            "ManagementUsersCreateDisableUserQueueErrorComponent",
            "ManagementUsersCreateFirstNameErrorComponent",
            "ManagementUsersCreateGenderErrorComponent",
            "ManagementUsersCreateHostnameErrorComponent",
            "ManagementUsersCreateLastNameErrorComponent",
            "ManagementUsersCreateMenteesErrorComponent",
            "ManagementUsersCreateMentorErrorComponent",
            "ManagementUsersCreateNonFieldErrorsErrorComponent",
            "ManagementUsersCreateNumberErrorComponent",
            "ManagementUsersCreateOverrideQueueErrorComponent",
            "ManagementUsersCreatePasswordErrorComponent",
            "ManagementUsersCreateProgramErrorComponent",
            "ManagementUsersCreateQueueErrorComponent",
            "ManagementUsersCreateStatusErrorComponent",
            "ManagementUsersCreateTeacherErrorComponent",
            "ManagementUsersCreateUserQueueErrorComponent",
            "ManagementUsersCreateUsernameErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_users_create_avatar_error_component import ManagementUsersCreateAvatarErrorComponent
        from ..models.management_users_create_avatar_filename_error_component import (
            ManagementUsersCreateAvatarFilenameErrorComponent,
        )
        from ..models.management_users_create_checkers_brief_error_component import (
            ManagementUsersCreateCheckersBriefErrorComponent,
        )
        from ..models.management_users_create_classes_error_component import ManagementUsersCreateClassesErrorComponent
        from ..models.management_users_create_clearance_error_component import (
            ManagementUsersCreateClearanceErrorComponent,
        )
        from ..models.management_users_create_confirmed_error_component import (
            ManagementUsersCreateConfirmedErrorComponent,
        )
        from ..models.management_users_create_disable_queue_error_component import (
            ManagementUsersCreateDisableQueueErrorComponent,
        )
        from ..models.management_users_create_disable_user_queue_error_component import (
            ManagementUsersCreateDisableUserQueueErrorComponent,
        )
        from ..models.management_users_create_first_name_error_component import (
            ManagementUsersCreateFirstNameErrorComponent,
        )
        from ..models.management_users_create_gender_error_component import ManagementUsersCreateGenderErrorComponent
        from ..models.management_users_create_hostname_error_component import (
            ManagementUsersCreateHostnameErrorComponent,
        )
        from ..models.management_users_create_last_name_error_component import (
            ManagementUsersCreateLastNameErrorComponent,
        )
        from ..models.management_users_create_mentees_error_component import ManagementUsersCreateMenteesErrorComponent
        from ..models.management_users_create_mentor_error_component import ManagementUsersCreateMentorErrorComponent
        from ..models.management_users_create_non_field_errors_error_component import (
            ManagementUsersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_create_number_error_component import ManagementUsersCreateNumberErrorComponent
        from ..models.management_users_create_override_queue_error_component import (
            ManagementUsersCreateOverrideQueueErrorComponent,
        )
        from ..models.management_users_create_program_error_component import ManagementUsersCreateProgramErrorComponent
        from ..models.management_users_create_queue_error_component import ManagementUsersCreateQueueErrorComponent
        from ..models.management_users_create_status_error_component import ManagementUsersCreateStatusErrorComponent
        from ..models.management_users_create_teacher_error_component import ManagementUsersCreateTeacherErrorComponent
        from ..models.management_users_create_user_queue_error_component import (
            ManagementUsersCreateUserQueueErrorComponent,
        )
        from ..models.management_users_create_username_error_component import (
            ManagementUsersCreateUsernameErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementUsersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateClearanceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateAvatarErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateAvatarFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateGenderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateProgramErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateCheckersBriefErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateMentorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateMenteesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateUsernameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateDisableQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateUserQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateDisableUserQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateOverrideQueueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateConfirmedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateTeacherErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersCreateHostnameErrorComponent):
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
        from ..models.management_users_create_avatar_error_component import ManagementUsersCreateAvatarErrorComponent
        from ..models.management_users_create_avatar_filename_error_component import (
            ManagementUsersCreateAvatarFilenameErrorComponent,
        )
        from ..models.management_users_create_checkers_brief_error_component import (
            ManagementUsersCreateCheckersBriefErrorComponent,
        )
        from ..models.management_users_create_classes_error_component import ManagementUsersCreateClassesErrorComponent
        from ..models.management_users_create_clearance_error_component import (
            ManagementUsersCreateClearanceErrorComponent,
        )
        from ..models.management_users_create_confirmed_error_component import (
            ManagementUsersCreateConfirmedErrorComponent,
        )
        from ..models.management_users_create_disable_queue_error_component import (
            ManagementUsersCreateDisableQueueErrorComponent,
        )
        from ..models.management_users_create_disable_user_queue_error_component import (
            ManagementUsersCreateDisableUserQueueErrorComponent,
        )
        from ..models.management_users_create_first_name_error_component import (
            ManagementUsersCreateFirstNameErrorComponent,
        )
        from ..models.management_users_create_gender_error_component import ManagementUsersCreateGenderErrorComponent
        from ..models.management_users_create_hostname_error_component import (
            ManagementUsersCreateHostnameErrorComponent,
        )
        from ..models.management_users_create_last_name_error_component import (
            ManagementUsersCreateLastNameErrorComponent,
        )
        from ..models.management_users_create_mentees_error_component import ManagementUsersCreateMenteesErrorComponent
        from ..models.management_users_create_mentor_error_component import ManagementUsersCreateMentorErrorComponent
        from ..models.management_users_create_non_field_errors_error_component import (
            ManagementUsersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_create_number_error_component import ManagementUsersCreateNumberErrorComponent
        from ..models.management_users_create_override_queue_error_component import (
            ManagementUsersCreateOverrideQueueErrorComponent,
        )
        from ..models.management_users_create_password_error_component import (
            ManagementUsersCreatePasswordErrorComponent,
        )
        from ..models.management_users_create_program_error_component import ManagementUsersCreateProgramErrorComponent
        from ..models.management_users_create_queue_error_component import ManagementUsersCreateQueueErrorComponent
        from ..models.management_users_create_status_error_component import ManagementUsersCreateStatusErrorComponent
        from ..models.management_users_create_teacher_error_component import ManagementUsersCreateTeacherErrorComponent
        from ..models.management_users_create_user_queue_error_component import (
            ManagementUsersCreateUserQueueErrorComponent,
        )
        from ..models.management_users_create_username_error_component import (
            ManagementUsersCreateUsernameErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementUsersCreateAvatarErrorComponent",
                "ManagementUsersCreateAvatarFilenameErrorComponent",
                "ManagementUsersCreateCheckersBriefErrorComponent",
                "ManagementUsersCreateClassesErrorComponent",
                "ManagementUsersCreateClearanceErrorComponent",
                "ManagementUsersCreateConfirmedErrorComponent",
                "ManagementUsersCreateDisableQueueErrorComponent",
                "ManagementUsersCreateDisableUserQueueErrorComponent",
                "ManagementUsersCreateFirstNameErrorComponent",
                "ManagementUsersCreateGenderErrorComponent",
                "ManagementUsersCreateHostnameErrorComponent",
                "ManagementUsersCreateLastNameErrorComponent",
                "ManagementUsersCreateMenteesErrorComponent",
                "ManagementUsersCreateMentorErrorComponent",
                "ManagementUsersCreateNonFieldErrorsErrorComponent",
                "ManagementUsersCreateNumberErrorComponent",
                "ManagementUsersCreateOverrideQueueErrorComponent",
                "ManagementUsersCreatePasswordErrorComponent",
                "ManagementUsersCreateProgramErrorComponent",
                "ManagementUsersCreateQueueErrorComponent",
                "ManagementUsersCreateStatusErrorComponent",
                "ManagementUsersCreateTeacherErrorComponent",
                "ManagementUsersCreateUserQueueErrorComponent",
                "ManagementUsersCreateUsernameErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_0 = (
                        ManagementUsersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_1 = (
                        ManagementUsersCreateClearanceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_2 = (
                        ManagementUsersCreateAvatarErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_3 = (
                        ManagementUsersCreateAvatarFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_4 = (
                        ManagementUsersCreateGenderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_5 = (
                        ManagementUsersCreateNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_6 = (
                        ManagementUsersCreateProgramErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_7 = (
                        ManagementUsersCreateCheckersBriefErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_8 = (
                        ManagementUsersCreateMentorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_9 = (
                        ManagementUsersCreateClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_10 = (
                        ManagementUsersCreateMenteesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_11 = (
                        ManagementUsersCreateUsernameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_12 = (
                        ManagementUsersCreateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_13 = (
                        ManagementUsersCreateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_14 = (
                        ManagementUsersCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_15 = (
                        ManagementUsersCreateQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_16 = (
                        ManagementUsersCreateDisableQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_17 = (
                        ManagementUsersCreateUserQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_18 = (
                        ManagementUsersCreateDisableUserQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_19 = (
                        ManagementUsersCreateOverrideQueueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_20 = (
                        ManagementUsersCreateConfirmedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_21 = (
                        ManagementUsersCreateTeacherErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_create_error_type_22 = (
                        ManagementUsersCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_create_error_type_22
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_users_create_error_type_23 = (
                    ManagementUsersCreatePasswordErrorComponent.from_dict(data)
                )

                return componentsschemas_management_users_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_users_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_users_create_validation_error.additional_properties = d
        return management_users_create_validation_error

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
