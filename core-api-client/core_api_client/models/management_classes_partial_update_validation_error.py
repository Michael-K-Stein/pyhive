from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_classes_partial_update_classes_error_component import (
        ManagementClassesPartialUpdateClassesErrorComponent,
    )
    from ..models.management_classes_partial_update_description_error_component import (
        ManagementClassesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.management_classes_partial_update_email_error_component import (
        ManagementClassesPartialUpdateEmailErrorComponent,
    )
    from ..models.management_classes_partial_update_name_error_component import (
        ManagementClassesPartialUpdateNameErrorComponent,
    )
    from ..models.management_classes_partial_update_non_field_errors_error_component import (
        ManagementClassesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_classes_partial_update_program_error_component import (
        ManagementClassesPartialUpdateProgramErrorComponent,
    )
    from ..models.management_classes_partial_update_type_error_component import (
        ManagementClassesPartialUpdateTypeErrorComponent,
    )
    from ..models.management_classes_partial_update_users_error_component import (
        ManagementClassesPartialUpdateUsersErrorComponent,
    )


T = TypeVar("T", bound="ManagementClassesPartialUpdateValidationError")


@_attrs_define
class ManagementClassesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementClassesPartialUpdateClassesErrorComponent',
            'ManagementClassesPartialUpdateDescriptionErrorComponent', 'ManagementClassesPartialUpdateEmailErrorComponent',
            'ManagementClassesPartialUpdateNameErrorComponent',
            'ManagementClassesPartialUpdateNonFieldErrorsErrorComponent',
            'ManagementClassesPartialUpdateProgramErrorComponent', 'ManagementClassesPartialUpdateTypeErrorComponent',
            'ManagementClassesPartialUpdateUsersErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementClassesPartialUpdateClassesErrorComponent",
            "ManagementClassesPartialUpdateDescriptionErrorComponent",
            "ManagementClassesPartialUpdateEmailErrorComponent",
            "ManagementClassesPartialUpdateNameErrorComponent",
            "ManagementClassesPartialUpdateNonFieldErrorsErrorComponent",
            "ManagementClassesPartialUpdateProgramErrorComponent",
            "ManagementClassesPartialUpdateTypeErrorComponent",
            "ManagementClassesPartialUpdateUsersErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_classes_partial_update_classes_error_component import (
            ManagementClassesPartialUpdateClassesErrorComponent,
        )
        from ..models.management_classes_partial_update_email_error_component import (
            ManagementClassesPartialUpdateEmailErrorComponent,
        )
        from ..models.management_classes_partial_update_name_error_component import (
            ManagementClassesPartialUpdateNameErrorComponent,
        )
        from ..models.management_classes_partial_update_non_field_errors_error_component import (
            ManagementClassesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_classes_partial_update_program_error_component import (
            ManagementClassesPartialUpdateProgramErrorComponent,
        )
        from ..models.management_classes_partial_update_type_error_component import (
            ManagementClassesPartialUpdateTypeErrorComponent,
        )
        from ..models.management_classes_partial_update_users_error_component import (
            ManagementClassesPartialUpdateUsersErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementClassesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesPartialUpdateProgramErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesPartialUpdateUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesPartialUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesPartialUpdateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesPartialUpdateClassesErrorComponent):
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
        from ..models.management_classes_partial_update_classes_error_component import (
            ManagementClassesPartialUpdateClassesErrorComponent,
        )
        from ..models.management_classes_partial_update_description_error_component import (
            ManagementClassesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.management_classes_partial_update_email_error_component import (
            ManagementClassesPartialUpdateEmailErrorComponent,
        )
        from ..models.management_classes_partial_update_name_error_component import (
            ManagementClassesPartialUpdateNameErrorComponent,
        )
        from ..models.management_classes_partial_update_non_field_errors_error_component import (
            ManagementClassesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_classes_partial_update_program_error_component import (
            ManagementClassesPartialUpdateProgramErrorComponent,
        )
        from ..models.management_classes_partial_update_type_error_component import (
            ManagementClassesPartialUpdateTypeErrorComponent,
        )
        from ..models.management_classes_partial_update_users_error_component import (
            ManagementClassesPartialUpdateUsersErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementClassesPartialUpdateClassesErrorComponent",
                "ManagementClassesPartialUpdateDescriptionErrorComponent",
                "ManagementClassesPartialUpdateEmailErrorComponent",
                "ManagementClassesPartialUpdateNameErrorComponent",
                "ManagementClassesPartialUpdateNonFieldErrorsErrorComponent",
                "ManagementClassesPartialUpdateProgramErrorComponent",
                "ManagementClassesPartialUpdateTypeErrorComponent",
                "ManagementClassesPartialUpdateUsersErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_0 = (
                        ManagementClassesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_1 = (
                        ManagementClassesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_2 = (
                        ManagementClassesPartialUpdateProgramErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_3 = (
                        ManagementClassesPartialUpdateUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_4 = (
                        ManagementClassesPartialUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_5 = (
                        ManagementClassesPartialUpdateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_partial_update_error_type_6 = (
                        ManagementClassesPartialUpdateClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_classes_partial_update_error_type_7 = (
                    ManagementClassesPartialUpdateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_management_classes_partial_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_classes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_classes_partial_update_validation_error.additional_properties = d
        return management_classes_partial_update_validation_error

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
