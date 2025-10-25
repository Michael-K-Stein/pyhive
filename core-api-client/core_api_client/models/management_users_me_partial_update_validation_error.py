from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_users_me_partial_update_confirmed_error_component import (
        ManagementUsersMePartialUpdateConfirmedErrorComponent,
    )
    from ..models.management_users_me_partial_update_current_assignment_error_component import (
        ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent,
    )
    from ..models.management_users_me_partial_update_current_password_error_component import (
        ManagementUsersMePartialUpdateCurrentPasswordErrorComponent,
    )
    from ..models.management_users_me_partial_update_hostname_error_component import (
        ManagementUsersMePartialUpdateHostnameErrorComponent,
    )
    from ..models.management_users_me_partial_update_non_field_errors_error_component import (
        ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_users_me_partial_update_password_error_component import (
        ManagementUsersMePartialUpdatePasswordErrorComponent,
    )
    from ..models.management_users_me_partial_update_status_error_component import (
        ManagementUsersMePartialUpdateStatusErrorComponent,
    )


T = TypeVar("T", bound="ManagementUsersMePartialUpdateValidationError")


@_attrs_define
class ManagementUsersMePartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementUsersMePartialUpdateConfirmedErrorComponent',
            'ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent',
            'ManagementUsersMePartialUpdateCurrentPasswordErrorComponent',
            'ManagementUsersMePartialUpdateHostnameErrorComponent',
            'ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent',
            'ManagementUsersMePartialUpdatePasswordErrorComponent', 'ManagementUsersMePartialUpdateStatusErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementUsersMePartialUpdateConfirmedErrorComponent",
            "ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent",
            "ManagementUsersMePartialUpdateCurrentPasswordErrorComponent",
            "ManagementUsersMePartialUpdateHostnameErrorComponent",
            "ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent",
            "ManagementUsersMePartialUpdatePasswordErrorComponent",
            "ManagementUsersMePartialUpdateStatusErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_users_me_partial_update_confirmed_error_component import (
            ManagementUsersMePartialUpdateConfirmedErrorComponent,
        )
        from ..models.management_users_me_partial_update_current_assignment_error_component import (
            ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent,
        )
        from ..models.management_users_me_partial_update_current_password_error_component import (
            ManagementUsersMePartialUpdateCurrentPasswordErrorComponent,
        )
        from ..models.management_users_me_partial_update_non_field_errors_error_component import (
            ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_me_partial_update_password_error_component import (
            ManagementUsersMePartialUpdatePasswordErrorComponent,
        )
        from ..models.management_users_me_partial_update_status_error_component import (
            ManagementUsersMePartialUpdateStatusErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersMePartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersMePartialUpdateConfirmedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersMePartialUpdatePasswordErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersMePartialUpdateCurrentPasswordErrorComponent):
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
        from ..models.management_users_me_partial_update_confirmed_error_component import (
            ManagementUsersMePartialUpdateConfirmedErrorComponent,
        )
        from ..models.management_users_me_partial_update_current_assignment_error_component import (
            ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent,
        )
        from ..models.management_users_me_partial_update_current_password_error_component import (
            ManagementUsersMePartialUpdateCurrentPasswordErrorComponent,
        )
        from ..models.management_users_me_partial_update_hostname_error_component import (
            ManagementUsersMePartialUpdateHostnameErrorComponent,
        )
        from ..models.management_users_me_partial_update_non_field_errors_error_component import (
            ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_users_me_partial_update_password_error_component import (
            ManagementUsersMePartialUpdatePasswordErrorComponent,
        )
        from ..models.management_users_me_partial_update_status_error_component import (
            ManagementUsersMePartialUpdateStatusErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementUsersMePartialUpdateConfirmedErrorComponent",
                "ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent",
                "ManagementUsersMePartialUpdateCurrentPasswordErrorComponent",
                "ManagementUsersMePartialUpdateHostnameErrorComponent",
                "ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent",
                "ManagementUsersMePartialUpdatePasswordErrorComponent",
                "ManagementUsersMePartialUpdateStatusErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_me_partial_update_error_type_0 = (
                        ManagementUsersMePartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_me_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_me_partial_update_error_type_1 = (
                        ManagementUsersMePartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_me_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_me_partial_update_error_type_2 = (
                        ManagementUsersMePartialUpdateCurrentAssignmentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_me_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_me_partial_update_error_type_3 = (
                        ManagementUsersMePartialUpdateConfirmedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_me_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_me_partial_update_error_type_4 = (
                        ManagementUsersMePartialUpdatePasswordErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_me_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_me_partial_update_error_type_5 = (
                        ManagementUsersMePartialUpdateCurrentPasswordErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_me_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_users_me_partial_update_error_type_6 = (
                    ManagementUsersMePartialUpdateHostnameErrorComponent.from_dict(data)
                )

                return componentsschemas_management_users_me_partial_update_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_users_me_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_users_me_partial_update_validation_error.additional_properties = d
        return management_users_me_partial_update_validation_error

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
