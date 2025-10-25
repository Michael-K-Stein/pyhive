from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.queues_duplicate_create_module_error_component import QueuesDuplicateCreateModuleErrorComponent
    from ..models.queues_duplicate_create_name_error_component import QueuesDuplicateCreateNameErrorComponent
    from ..models.queues_duplicate_create_non_field_errors_error_component import (
        QueuesDuplicateCreateNonFieldErrorsErrorComponent,
    )
    from ..models.queues_duplicate_create_user_error_component import QueuesDuplicateCreateUserErrorComponent


T = TypeVar("T", bound="QueuesDuplicateCreateValidationError")


@_attrs_define
class QueuesDuplicateCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['QueuesDuplicateCreateModuleErrorComponent', 'QueuesDuplicateCreateNameErrorComponent',
            'QueuesDuplicateCreateNonFieldErrorsErrorComponent', 'QueuesDuplicateCreateUserErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "QueuesDuplicateCreateModuleErrorComponent",
            "QueuesDuplicateCreateNameErrorComponent",
            "QueuesDuplicateCreateNonFieldErrorsErrorComponent",
            "QueuesDuplicateCreateUserErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.queues_duplicate_create_module_error_component import QueuesDuplicateCreateModuleErrorComponent
        from ..models.queues_duplicate_create_name_error_component import QueuesDuplicateCreateNameErrorComponent
        from ..models.queues_duplicate_create_non_field_errors_error_component import (
            QueuesDuplicateCreateNonFieldErrorsErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, QueuesDuplicateCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesDuplicateCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesDuplicateCreateModuleErrorComponent):
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
        from ..models.queues_duplicate_create_module_error_component import QueuesDuplicateCreateModuleErrorComponent
        from ..models.queues_duplicate_create_name_error_component import QueuesDuplicateCreateNameErrorComponent
        from ..models.queues_duplicate_create_non_field_errors_error_component import (
            QueuesDuplicateCreateNonFieldErrorsErrorComponent,
        )
        from ..models.queues_duplicate_create_user_error_component import QueuesDuplicateCreateUserErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "QueuesDuplicateCreateModuleErrorComponent",
                "QueuesDuplicateCreateNameErrorComponent",
                "QueuesDuplicateCreateNonFieldErrorsErrorComponent",
                "QueuesDuplicateCreateUserErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_duplicate_create_error_type_0 = (
                        QueuesDuplicateCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_duplicate_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_duplicate_create_error_type_1 = (
                        QueuesDuplicateCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_duplicate_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_duplicate_create_error_type_2 = (
                        QueuesDuplicateCreateModuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_duplicate_create_error_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_queues_duplicate_create_error_type_3 = (
                    QueuesDuplicateCreateUserErrorComponent.from_dict(data)
                )

                return componentsschemas_queues_duplicate_create_error_type_3

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        queues_duplicate_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        queues_duplicate_create_validation_error.additional_properties = d
        return queues_duplicate_create_validation_error

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
