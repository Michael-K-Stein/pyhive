from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_seating_update_classroom_error_component import (
        ManagementSeatingUpdateClassroomErrorComponent,
    )
    from ..models.management_seating_update_hanich_error_component import ManagementSeatingUpdateHanichErrorComponent
    from ..models.management_seating_update_hostname_error_component import (
        ManagementSeatingUpdateHostnameErrorComponent,
    )
    from ..models.management_seating_update_non_field_errors_error_component import (
        ManagementSeatingUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_seating_update_x_error_component import ManagementSeatingUpdateXErrorComponent
    from ..models.management_seating_update_y_error_component import ManagementSeatingUpdateYErrorComponent


T = TypeVar("T", bound="ManagementSeatingUpdateValidationError")


@_attrs_define
class ManagementSeatingUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementSeatingUpdateClassroomErrorComponent',
            'ManagementSeatingUpdateHanichErrorComponent', 'ManagementSeatingUpdateHostnameErrorComponent',
            'ManagementSeatingUpdateNonFieldErrorsErrorComponent', 'ManagementSeatingUpdateXErrorComponent',
            'ManagementSeatingUpdateYErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementSeatingUpdateClassroomErrorComponent",
            "ManagementSeatingUpdateHanichErrorComponent",
            "ManagementSeatingUpdateHostnameErrorComponent",
            "ManagementSeatingUpdateNonFieldErrorsErrorComponent",
            "ManagementSeatingUpdateXErrorComponent",
            "ManagementSeatingUpdateYErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_seating_update_classroom_error_component import (
            ManagementSeatingUpdateClassroomErrorComponent,
        )
        from ..models.management_seating_update_hanich_error_component import (
            ManagementSeatingUpdateHanichErrorComponent,
        )
        from ..models.management_seating_update_hostname_error_component import (
            ManagementSeatingUpdateHostnameErrorComponent,
        )
        from ..models.management_seating_update_non_field_errors_error_component import (
            ManagementSeatingUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_seating_update_x_error_component import ManagementSeatingUpdateXErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementSeatingUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingUpdateHanichErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingUpdateClassroomErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingUpdateXErrorComponent):
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
        from ..models.management_seating_update_classroom_error_component import (
            ManagementSeatingUpdateClassroomErrorComponent,
        )
        from ..models.management_seating_update_hanich_error_component import (
            ManagementSeatingUpdateHanichErrorComponent,
        )
        from ..models.management_seating_update_hostname_error_component import (
            ManagementSeatingUpdateHostnameErrorComponent,
        )
        from ..models.management_seating_update_non_field_errors_error_component import (
            ManagementSeatingUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_seating_update_x_error_component import ManagementSeatingUpdateXErrorComponent
        from ..models.management_seating_update_y_error_component import ManagementSeatingUpdateYErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementSeatingUpdateClassroomErrorComponent",
                "ManagementSeatingUpdateHanichErrorComponent",
                "ManagementSeatingUpdateHostnameErrorComponent",
                "ManagementSeatingUpdateNonFieldErrorsErrorComponent",
                "ManagementSeatingUpdateXErrorComponent",
                "ManagementSeatingUpdateYErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_update_error_type_0 = (
                        ManagementSeatingUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_update_error_type_1 = (
                        ManagementSeatingUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_update_error_type_2 = (
                        ManagementSeatingUpdateHanichErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_update_error_type_3 = (
                        ManagementSeatingUpdateClassroomErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_update_error_type_4 = (
                        ManagementSeatingUpdateXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_update_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_seating_update_error_type_5 = (
                    ManagementSeatingUpdateYErrorComponent.from_dict(data)
                )

                return componentsschemas_management_seating_update_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_seating_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_seating_update_validation_error.additional_properties = d
        return management_seating_update_validation_error

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
