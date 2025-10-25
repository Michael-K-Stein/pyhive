from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_seating_partial_update_classroom_error_component import (
        ManagementSeatingPartialUpdateClassroomErrorComponent,
    )
    from ..models.management_seating_partial_update_hanich_error_component import (
        ManagementSeatingPartialUpdateHanichErrorComponent,
    )
    from ..models.management_seating_partial_update_hostname_error_component import (
        ManagementSeatingPartialUpdateHostnameErrorComponent,
    )
    from ..models.management_seating_partial_update_non_field_errors_error_component import (
        ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.management_seating_partial_update_x_error_component import (
        ManagementSeatingPartialUpdateXErrorComponent,
    )
    from ..models.management_seating_partial_update_y_error_component import (
        ManagementSeatingPartialUpdateYErrorComponent,
    )


T = TypeVar("T", bound="ManagementSeatingPartialUpdateValidationError")


@_attrs_define
class ManagementSeatingPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementSeatingPartialUpdateClassroomErrorComponent',
            'ManagementSeatingPartialUpdateHanichErrorComponent', 'ManagementSeatingPartialUpdateHostnameErrorComponent',
            'ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent', 'ManagementSeatingPartialUpdateXErrorComponent',
            'ManagementSeatingPartialUpdateYErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementSeatingPartialUpdateClassroomErrorComponent",
            "ManagementSeatingPartialUpdateHanichErrorComponent",
            "ManagementSeatingPartialUpdateHostnameErrorComponent",
            "ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent",
            "ManagementSeatingPartialUpdateXErrorComponent",
            "ManagementSeatingPartialUpdateYErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_seating_partial_update_classroom_error_component import (
            ManagementSeatingPartialUpdateClassroomErrorComponent,
        )
        from ..models.management_seating_partial_update_hanich_error_component import (
            ManagementSeatingPartialUpdateHanichErrorComponent,
        )
        from ..models.management_seating_partial_update_hostname_error_component import (
            ManagementSeatingPartialUpdateHostnameErrorComponent,
        )
        from ..models.management_seating_partial_update_non_field_errors_error_component import (
            ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_seating_partial_update_x_error_component import (
            ManagementSeatingPartialUpdateXErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingPartialUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingPartialUpdateHanichErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingPartialUpdateClassroomErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementSeatingPartialUpdateXErrorComponent):
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
        from ..models.management_seating_partial_update_classroom_error_component import (
            ManagementSeatingPartialUpdateClassroomErrorComponent,
        )
        from ..models.management_seating_partial_update_hanich_error_component import (
            ManagementSeatingPartialUpdateHanichErrorComponent,
        )
        from ..models.management_seating_partial_update_hostname_error_component import (
            ManagementSeatingPartialUpdateHostnameErrorComponent,
        )
        from ..models.management_seating_partial_update_non_field_errors_error_component import (
            ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.management_seating_partial_update_x_error_component import (
            ManagementSeatingPartialUpdateXErrorComponent,
        )
        from ..models.management_seating_partial_update_y_error_component import (
            ManagementSeatingPartialUpdateYErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementSeatingPartialUpdateClassroomErrorComponent",
                "ManagementSeatingPartialUpdateHanichErrorComponent",
                "ManagementSeatingPartialUpdateHostnameErrorComponent",
                "ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent",
                "ManagementSeatingPartialUpdateXErrorComponent",
                "ManagementSeatingPartialUpdateYErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_partial_update_error_type_0 = (
                        ManagementSeatingPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_partial_update_error_type_1 = (
                        ManagementSeatingPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_partial_update_error_type_2 = (
                        ManagementSeatingPartialUpdateHanichErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_partial_update_error_type_3 = (
                        ManagementSeatingPartialUpdateClassroomErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_seating_partial_update_error_type_4 = (
                        ManagementSeatingPartialUpdateXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_seating_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_seating_partial_update_error_type_5 = (
                    ManagementSeatingPartialUpdateYErrorComponent.from_dict(data)
                )

                return componentsschemas_management_seating_partial_update_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_seating_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_seating_partial_update_validation_error.additional_properties = d
        return management_seating_partial_update_validation_error

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
