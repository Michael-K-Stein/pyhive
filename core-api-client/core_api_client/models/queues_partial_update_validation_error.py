from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.queues_partial_update_description_error_component import QueuesPartialUpdateDescriptionErrorComponent
    from ..models.queues_partial_update_module_error_component import QueuesPartialUpdateModuleErrorComponent
    from ..models.queues_partial_update_name_error_component import QueuesPartialUpdateNameErrorComponent
    from ..models.queues_partial_update_non_field_errors_error_component import (
        QueuesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.queues_partial_update_user_error_component import QueuesPartialUpdateUserErrorComponent


T = TypeVar("T", bound="QueuesPartialUpdateValidationError")


@_attrs_define
class QueuesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['QueuesPartialUpdateDescriptionErrorComponent', 'QueuesPartialUpdateModuleErrorComponent',
            'QueuesPartialUpdateNameErrorComponent', 'QueuesPartialUpdateNonFieldErrorsErrorComponent',
            'QueuesPartialUpdateUserErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "QueuesPartialUpdateDescriptionErrorComponent",
            "QueuesPartialUpdateModuleErrorComponent",
            "QueuesPartialUpdateNameErrorComponent",
            "QueuesPartialUpdateNonFieldErrorsErrorComponent",
            "QueuesPartialUpdateUserErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.queues_partial_update_description_error_component import (
            QueuesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.queues_partial_update_module_error_component import QueuesPartialUpdateModuleErrorComponent
        from ..models.queues_partial_update_name_error_component import QueuesPartialUpdateNameErrorComponent
        from ..models.queues_partial_update_non_field_errors_error_component import (
            QueuesPartialUpdateNonFieldErrorsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, QueuesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesPartialUpdateModuleErrorComponent):
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
        from ..models.queues_partial_update_description_error_component import (
            QueuesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.queues_partial_update_module_error_component import QueuesPartialUpdateModuleErrorComponent
        from ..models.queues_partial_update_name_error_component import QueuesPartialUpdateNameErrorComponent
        from ..models.queues_partial_update_non_field_errors_error_component import (
            QueuesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.queues_partial_update_user_error_component import QueuesPartialUpdateUserErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "QueuesPartialUpdateDescriptionErrorComponent",
                "QueuesPartialUpdateModuleErrorComponent",
                "QueuesPartialUpdateNameErrorComponent",
                "QueuesPartialUpdateNonFieldErrorsErrorComponent",
                "QueuesPartialUpdateUserErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_partial_update_error_type_0 = (
                        QueuesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_partial_update_error_type_1 = (
                        QueuesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_partial_update_error_type_2 = (
                        QueuesPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_partial_update_error_type_3 = (
                        QueuesPartialUpdateModuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_queues_partial_update_error_type_4 = QueuesPartialUpdateUserErrorComponent.from_dict(
                    data
                )

                return componentsschemas_queues_partial_update_error_type_4

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        queues_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        queues_partial_update_validation_error.additional_properties = d
        return queues_partial_update_validation_error

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
