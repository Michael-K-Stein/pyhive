from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_register_create_first_name_error_component import (
        ManagementRegisterCreateFirstNameErrorComponent,
    )
    from ..models.management_register_create_gender_error_component import ManagementRegisterCreateGenderErrorComponent
    from ..models.management_register_create_last_name_error_component import (
        ManagementRegisterCreateLastNameErrorComponent,
    )
    from ..models.management_register_create_non_field_errors_error_component import (
        ManagementRegisterCreateNonFieldErrorsErrorComponent,
    )
    from ..models.management_register_create_password_error_component import (
        ManagementRegisterCreatePasswordErrorComponent,
    )
    from ..models.management_register_create_secret_error_component import ManagementRegisterCreateSecretErrorComponent
    from ..models.management_register_create_username_error_component import (
        ManagementRegisterCreateUsernameErrorComponent,
    )


T = TypeVar("T", bound="ManagementRegisterCreateValidationError")


@_attrs_define
class ManagementRegisterCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementRegisterCreateFirstNameErrorComponent',
            'ManagementRegisterCreateGenderErrorComponent', 'ManagementRegisterCreateLastNameErrorComponent',
            'ManagementRegisterCreateNonFieldErrorsErrorComponent', 'ManagementRegisterCreatePasswordErrorComponent',
            'ManagementRegisterCreateSecretErrorComponent', 'ManagementRegisterCreateUsernameErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementRegisterCreateFirstNameErrorComponent",
            "ManagementRegisterCreateGenderErrorComponent",
            "ManagementRegisterCreateLastNameErrorComponent",
            "ManagementRegisterCreateNonFieldErrorsErrorComponent",
            "ManagementRegisterCreatePasswordErrorComponent",
            "ManagementRegisterCreateSecretErrorComponent",
            "ManagementRegisterCreateUsernameErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_register_create_first_name_error_component import (
            ManagementRegisterCreateFirstNameErrorComponent,
        )
        from ..models.management_register_create_gender_error_component import (
            ManagementRegisterCreateGenderErrorComponent,
        )
        from ..models.management_register_create_last_name_error_component import (
            ManagementRegisterCreateLastNameErrorComponent,
        )
        from ..models.management_register_create_non_field_errors_error_component import (
            ManagementRegisterCreateNonFieldErrorsErrorComponent,
        )
        from ..models.management_register_create_password_error_component import (
            ManagementRegisterCreatePasswordErrorComponent,
        )
        from ..models.management_register_create_username_error_component import (
            ManagementRegisterCreateUsernameErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementRegisterCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementRegisterCreateFirstNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementRegisterCreateLastNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementRegisterCreateUsernameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementRegisterCreateGenderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementRegisterCreatePasswordErrorComponent):
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
        from ..models.management_register_create_first_name_error_component import (
            ManagementRegisterCreateFirstNameErrorComponent,
        )
        from ..models.management_register_create_gender_error_component import (
            ManagementRegisterCreateGenderErrorComponent,
        )
        from ..models.management_register_create_last_name_error_component import (
            ManagementRegisterCreateLastNameErrorComponent,
        )
        from ..models.management_register_create_non_field_errors_error_component import (
            ManagementRegisterCreateNonFieldErrorsErrorComponent,
        )
        from ..models.management_register_create_password_error_component import (
            ManagementRegisterCreatePasswordErrorComponent,
        )
        from ..models.management_register_create_secret_error_component import (
            ManagementRegisterCreateSecretErrorComponent,
        )
        from ..models.management_register_create_username_error_component import (
            ManagementRegisterCreateUsernameErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementRegisterCreateFirstNameErrorComponent",
                "ManagementRegisterCreateGenderErrorComponent",
                "ManagementRegisterCreateLastNameErrorComponent",
                "ManagementRegisterCreateNonFieldErrorsErrorComponent",
                "ManagementRegisterCreatePasswordErrorComponent",
                "ManagementRegisterCreateSecretErrorComponent",
                "ManagementRegisterCreateUsernameErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_register_create_error_type_0 = (
                        ManagementRegisterCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_register_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_register_create_error_type_1 = (
                        ManagementRegisterCreateFirstNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_register_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_register_create_error_type_2 = (
                        ManagementRegisterCreateLastNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_register_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_register_create_error_type_3 = (
                        ManagementRegisterCreateUsernameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_register_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_register_create_error_type_4 = (
                        ManagementRegisterCreateGenderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_register_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_register_create_error_type_5 = (
                        ManagementRegisterCreatePasswordErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_register_create_error_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_register_create_error_type_6 = (
                    ManagementRegisterCreateSecretErrorComponent.from_dict(data)
                )

                return componentsschemas_management_register_create_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_register_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_register_create_validation_error.additional_properties = d
        return management_register_create_validation_error

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
