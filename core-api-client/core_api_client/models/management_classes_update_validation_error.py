from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_classes_update_classes_error_component import ManagementClassesUpdateClassesErrorComponent
    from ..models.management_classes_update_description_error_component import (
        ManagementClassesUpdateDescriptionErrorComponent,
    )
    from ..models.management_classes_update_email_error_component import ManagementClassesUpdateEmailErrorComponent
    from ..models.management_classes_update_name_error_component import ManagementClassesUpdateNameErrorComponent
    from ..models.management_classes_update_non_field_errors_error_component import (
        ManagementClassesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_classes_update_program_error_component import ManagementClassesUpdateProgramErrorComponent
    from ..models.management_classes_update_type_error_component import ManagementClassesUpdateTypeErrorComponent
    from ..models.management_classes_update_users_error_component import ManagementClassesUpdateUsersErrorComponent


T = TypeVar("T", bound="ManagementClassesUpdateValidationError")


@_attrs_define
class ManagementClassesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementClassesUpdateClassesErrorComponent',
            'ManagementClassesUpdateDescriptionErrorComponent', 'ManagementClassesUpdateEmailErrorComponent',
            'ManagementClassesUpdateNameErrorComponent', 'ManagementClassesUpdateNonFieldErrorsErrorComponent',
            'ManagementClassesUpdateProgramErrorComponent', 'ManagementClassesUpdateTypeErrorComponent',
            'ManagementClassesUpdateUsersErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementClassesUpdateClassesErrorComponent",
            "ManagementClassesUpdateDescriptionErrorComponent",
            "ManagementClassesUpdateEmailErrorComponent",
            "ManagementClassesUpdateNameErrorComponent",
            "ManagementClassesUpdateNonFieldErrorsErrorComponent",
            "ManagementClassesUpdateProgramErrorComponent",
            "ManagementClassesUpdateTypeErrorComponent",
            "ManagementClassesUpdateUsersErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_classes_update_classes_error_component import (
            ManagementClassesUpdateClassesErrorComponent,
        )
        from ..models.management_classes_update_email_error_component import ManagementClassesUpdateEmailErrorComponent
        from ..models.management_classes_update_name_error_component import ManagementClassesUpdateNameErrorComponent
        from ..models.management_classes_update_non_field_errors_error_component import (
            ManagementClassesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_classes_update_program_error_component import (
            ManagementClassesUpdateProgramErrorComponent,
        )
        from ..models.management_classes_update_type_error_component import ManagementClassesUpdateTypeErrorComponent
        from ..models.management_classes_update_users_error_component import ManagementClassesUpdateUsersErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementClassesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesUpdateProgramErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesUpdateUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesUpdateClassesErrorComponent):
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
        from ..models.management_classes_update_classes_error_component import (
            ManagementClassesUpdateClassesErrorComponent,
        )
        from ..models.management_classes_update_description_error_component import (
            ManagementClassesUpdateDescriptionErrorComponent,
        )
        from ..models.management_classes_update_email_error_component import ManagementClassesUpdateEmailErrorComponent
        from ..models.management_classes_update_name_error_component import ManagementClassesUpdateNameErrorComponent
        from ..models.management_classes_update_non_field_errors_error_component import (
            ManagementClassesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_classes_update_program_error_component import (
            ManagementClassesUpdateProgramErrorComponent,
        )
        from ..models.management_classes_update_type_error_component import ManagementClassesUpdateTypeErrorComponent
        from ..models.management_classes_update_users_error_component import ManagementClassesUpdateUsersErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementClassesUpdateClassesErrorComponent",
                "ManagementClassesUpdateDescriptionErrorComponent",
                "ManagementClassesUpdateEmailErrorComponent",
                "ManagementClassesUpdateNameErrorComponent",
                "ManagementClassesUpdateNonFieldErrorsErrorComponent",
                "ManagementClassesUpdateProgramErrorComponent",
                "ManagementClassesUpdateTypeErrorComponent",
                "ManagementClassesUpdateUsersErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_0 = (
                        ManagementClassesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_1 = (
                        ManagementClassesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_2 = (
                        ManagementClassesUpdateProgramErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_3 = (
                        ManagementClassesUpdateUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_4 = (
                        ManagementClassesUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_5 = (
                        ManagementClassesUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_update_error_type_6 = (
                        ManagementClassesUpdateClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_update_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_classes_update_error_type_7 = (
                    ManagementClassesUpdateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_management_classes_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_classes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_classes_update_validation_error.additional_properties = d
        return management_classes_update_validation_error

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
