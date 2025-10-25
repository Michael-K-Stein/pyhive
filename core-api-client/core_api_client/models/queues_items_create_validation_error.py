from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.queues_items_create_continue_on_redo_error_component import (
        QueuesItemsCreateContinueOnRedoErrorComponent,
    )
    from ..models.queues_items_create_enabled_error_component import QueuesItemsCreateEnabledErrorComponent
    from ..models.queues_items_create_non_field_errors_error_component import (
        QueuesItemsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.queues_items_create_order_error_component import QueuesItemsCreateOrderErrorComponent
    from ..models.queues_items_create_queue_rule_error_component import QueuesItemsCreateQueueRuleErrorComponent
    from ..models.queues_items_create_set_exercise_id_error_component import (
        QueuesItemsCreateSetExerciseIdErrorComponent,
    )
    from ..models.queues_items_create_set_module_id_error_component import QueuesItemsCreateSetModuleIdErrorComponent
    from ..models.queues_items_create_set_nested_queue_id_error_component import (
        QueuesItemsCreateSetNestedQueueIdErrorComponent,
    )
    from ..models.queues_items_create_set_tags_id_error_component import QueuesItemsCreateSetTagsIdErrorComponent


T = TypeVar("T", bound="QueuesItemsCreateValidationError")


@_attrs_define
class QueuesItemsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['QueuesItemsCreateContinueOnRedoErrorComponent', 'QueuesItemsCreateEnabledErrorComponent',
            'QueuesItemsCreateNonFieldErrorsErrorComponent', 'QueuesItemsCreateOrderErrorComponent',
            'QueuesItemsCreateQueueRuleErrorComponent', 'QueuesItemsCreateSetExerciseIdErrorComponent',
            'QueuesItemsCreateSetModuleIdErrorComponent', 'QueuesItemsCreateSetNestedQueueIdErrorComponent',
            'QueuesItemsCreateSetTagsIdErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "QueuesItemsCreateContinueOnRedoErrorComponent",
            "QueuesItemsCreateEnabledErrorComponent",
            "QueuesItemsCreateNonFieldErrorsErrorComponent",
            "QueuesItemsCreateOrderErrorComponent",
            "QueuesItemsCreateQueueRuleErrorComponent",
            "QueuesItemsCreateSetExerciseIdErrorComponent",
            "QueuesItemsCreateSetModuleIdErrorComponent",
            "QueuesItemsCreateSetNestedQueueIdErrorComponent",
            "QueuesItemsCreateSetTagsIdErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.queues_items_create_continue_on_redo_error_component import (
            QueuesItemsCreateContinueOnRedoErrorComponent,
        )
        from ..models.queues_items_create_enabled_error_component import QueuesItemsCreateEnabledErrorComponent
        from ..models.queues_items_create_non_field_errors_error_component import (
            QueuesItemsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.queues_items_create_order_error_component import QueuesItemsCreateOrderErrorComponent
        from ..models.queues_items_create_queue_rule_error_component import QueuesItemsCreateQueueRuleErrorComponent
        from ..models.queues_items_create_set_exercise_id_error_component import (
            QueuesItemsCreateSetExerciseIdErrorComponent,
        )
        from ..models.queues_items_create_set_module_id_error_component import (
            QueuesItemsCreateSetModuleIdErrorComponent,
        )
        from ..models.queues_items_create_set_nested_queue_id_error_component import (
            QueuesItemsCreateSetNestedQueueIdErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, QueuesItemsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateSetExerciseIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateSetNestedQueueIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateSetModuleIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateQueueRuleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateContinueOnRedoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsCreateEnabledErrorComponent):
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
        from ..models.queues_items_create_continue_on_redo_error_component import (
            QueuesItemsCreateContinueOnRedoErrorComponent,
        )
        from ..models.queues_items_create_enabled_error_component import QueuesItemsCreateEnabledErrorComponent
        from ..models.queues_items_create_non_field_errors_error_component import (
            QueuesItemsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.queues_items_create_order_error_component import QueuesItemsCreateOrderErrorComponent
        from ..models.queues_items_create_queue_rule_error_component import QueuesItemsCreateQueueRuleErrorComponent
        from ..models.queues_items_create_set_exercise_id_error_component import (
            QueuesItemsCreateSetExerciseIdErrorComponent,
        )
        from ..models.queues_items_create_set_module_id_error_component import (
            QueuesItemsCreateSetModuleIdErrorComponent,
        )
        from ..models.queues_items_create_set_nested_queue_id_error_component import (
            QueuesItemsCreateSetNestedQueueIdErrorComponent,
        )
        from ..models.queues_items_create_set_tags_id_error_component import QueuesItemsCreateSetTagsIdErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "QueuesItemsCreateContinueOnRedoErrorComponent",
                "QueuesItemsCreateEnabledErrorComponent",
                "QueuesItemsCreateNonFieldErrorsErrorComponent",
                "QueuesItemsCreateOrderErrorComponent",
                "QueuesItemsCreateQueueRuleErrorComponent",
                "QueuesItemsCreateSetExerciseIdErrorComponent",
                "QueuesItemsCreateSetModuleIdErrorComponent",
                "QueuesItemsCreateSetNestedQueueIdErrorComponent",
                "QueuesItemsCreateSetTagsIdErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_0 = (
                        QueuesItemsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_1 = QueuesItemsCreateOrderErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_queues_items_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_2 = (
                        QueuesItemsCreateSetExerciseIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_3 = (
                        QueuesItemsCreateSetNestedQueueIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_4 = (
                        QueuesItemsCreateSetModuleIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_5 = (
                        QueuesItemsCreateQueueRuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_6 = (
                        QueuesItemsCreateContinueOnRedoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_create_error_type_7 = (
                        QueuesItemsCreateEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_create_error_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_queues_items_create_error_type_8 = QueuesItemsCreateSetTagsIdErrorComponent.from_dict(
                    data
                )

                return componentsschemas_queues_items_create_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        queues_items_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        queues_items_create_validation_error.additional_properties = d
        return queues_items_create_validation_error

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
