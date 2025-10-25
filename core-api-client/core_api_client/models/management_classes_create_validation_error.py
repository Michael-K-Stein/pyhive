from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_classes_create_classes_error_component import ManagementClassesCreateClassesErrorComponent
    from ..models.management_classes_create_description_error_component import (
        ManagementClassesCreateDescriptionErrorComponent,
    )
    from ..models.management_classes_create_email_error_component import ManagementClassesCreateEmailErrorComponent
    from ..models.management_classes_create_name_error_component import ManagementClassesCreateNameErrorComponent
    from ..models.management_classes_create_non_field_errors_error_component import (
        ManagementClassesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.management_classes_create_program_error_component import ManagementClassesCreateProgramErrorComponent
    from ..models.management_classes_create_type_error_component import ManagementClassesCreateTypeErrorComponent
    from ..models.management_classes_create_users_error_component import ManagementClassesCreateUsersErrorComponent


T = TypeVar("T", bound="ManagementClassesCreateValidationError")


@_attrs_define
class ManagementClassesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementClassesCreateClassesErrorComponent',
            'ManagementClassesCreateDescriptionErrorComponent', 'ManagementClassesCreateEmailErrorComponent',
            'ManagementClassesCreateNameErrorComponent', 'ManagementClassesCreateNonFieldErrorsErrorComponent',
            'ManagementClassesCreateProgramErrorComponent', 'ManagementClassesCreateTypeErrorComponent',
            'ManagementClassesCreateUsersErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementClassesCreateClassesErrorComponent",
            "ManagementClassesCreateDescriptionErrorComponent",
            "ManagementClassesCreateEmailErrorComponent",
            "ManagementClassesCreateNameErrorComponent",
            "ManagementClassesCreateNonFieldErrorsErrorComponent",
            "ManagementClassesCreateProgramErrorComponent",
            "ManagementClassesCreateTypeErrorComponent",
            "ManagementClassesCreateUsersErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_classes_create_classes_error_component import (
            ManagementClassesCreateClassesErrorComponent,
        )
        from ..models.management_classes_create_email_error_component import ManagementClassesCreateEmailErrorComponent
        from ..models.management_classes_create_name_error_component import ManagementClassesCreateNameErrorComponent
        from ..models.management_classes_create_non_field_errors_error_component import (
            ManagementClassesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.management_classes_create_program_error_component import (
            ManagementClassesCreateProgramErrorComponent,
        )
        from ..models.management_classes_create_type_error_component import ManagementClassesCreateTypeErrorComponent
        from ..models.management_classes_create_users_error_component import ManagementClassesCreateUsersErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementClassesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesCreateProgramErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesCreateUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesCreateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesCreateTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementClassesCreateClassesErrorComponent):
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
        from ..models.management_classes_create_classes_error_component import (
            ManagementClassesCreateClassesErrorComponent,
        )
        from ..models.management_classes_create_description_error_component import (
            ManagementClassesCreateDescriptionErrorComponent,
        )
        from ..models.management_classes_create_email_error_component import ManagementClassesCreateEmailErrorComponent
        from ..models.management_classes_create_name_error_component import ManagementClassesCreateNameErrorComponent
        from ..models.management_classes_create_non_field_errors_error_component import (
            ManagementClassesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.management_classes_create_program_error_component import (
            ManagementClassesCreateProgramErrorComponent,
        )
        from ..models.management_classes_create_type_error_component import ManagementClassesCreateTypeErrorComponent
        from ..models.management_classes_create_users_error_component import ManagementClassesCreateUsersErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementClassesCreateClassesErrorComponent",
                "ManagementClassesCreateDescriptionErrorComponent",
                "ManagementClassesCreateEmailErrorComponent",
                "ManagementClassesCreateNameErrorComponent",
                "ManagementClassesCreateNonFieldErrorsErrorComponent",
                "ManagementClassesCreateProgramErrorComponent",
                "ManagementClassesCreateTypeErrorComponent",
                "ManagementClassesCreateUsersErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_0 = (
                        ManagementClassesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_1 = (
                        ManagementClassesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_2 = (
                        ManagementClassesCreateProgramErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_3 = (
                        ManagementClassesCreateUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_4 = (
                        ManagementClassesCreateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_5 = (
                        ManagementClassesCreateTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_classes_create_error_type_6 = (
                        ManagementClassesCreateClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_classes_create_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_classes_create_error_type_7 = (
                    ManagementClassesCreateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_management_classes_create_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_classes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_classes_create_validation_error.additional_properties = d
        return management_classes_create_validation_error

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
