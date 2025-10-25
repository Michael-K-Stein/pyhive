from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.queues_items_move_create_new_order_error_component import QueuesItemsMoveCreateNewOrderErrorComponent
    from ..models.queues_items_move_create_non_field_errors_error_component import (
        QueuesItemsMoveCreateNonFieldErrorsErrorComponent,
    )


T = TypeVar("T", bound="QueuesItemsMoveCreateValidationError")


@_attrs_define
class QueuesItemsMoveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['QueuesItemsMoveCreateNewOrderErrorComponent',
            'QueuesItemsMoveCreateNonFieldErrorsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union["QueuesItemsMoveCreateNewOrderErrorComponent", "QueuesItemsMoveCreateNonFieldErrorsErrorComponent"]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.queues_items_move_create_non_field_errors_error_component import (
            QueuesItemsMoveCreateNonFieldErrorsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, QueuesItemsMoveCreateNonFieldErrorsErrorComponent):
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
        from ..models.queues_items_move_create_new_order_error_component import (
            QueuesItemsMoveCreateNewOrderErrorComponent,
        )
        from ..models.queues_items_move_create_non_field_errors_error_component import (
            QueuesItemsMoveCreateNonFieldErrorsErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "QueuesItemsMoveCreateNewOrderErrorComponent", "QueuesItemsMoveCreateNonFieldErrorsErrorComponent"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_move_create_error_type_0 = (
                        QueuesItemsMoveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_move_create_error_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_queues_items_move_create_error_type_1 = (
                    QueuesItemsMoveCreateNewOrderErrorComponent.from_dict(data)
                )

                return componentsschemas_queues_items_move_create_error_type_1

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        queues_items_move_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        queues_items_move_create_validation_error.additional_properties = d
        return queues_items_move_create_validation_error

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
