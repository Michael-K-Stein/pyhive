from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.queues_items_partial_update_continue_on_redo_error_component import (
        QueuesItemsPartialUpdateContinueOnRedoErrorComponent,
    )
    from ..models.queues_items_partial_update_enabled_error_component import (
        QueuesItemsPartialUpdateEnabledErrorComponent,
    )
    from ..models.queues_items_partial_update_non_field_errors_error_component import (
        QueuesItemsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.queues_items_partial_update_order_error_component import QueuesItemsPartialUpdateOrderErrorComponent
    from ..models.queues_items_partial_update_queue_rule_error_component import (
        QueuesItemsPartialUpdateQueueRuleErrorComponent,
    )
    from ..models.queues_items_partial_update_set_exercise_id_error_component import (
        QueuesItemsPartialUpdateSetExerciseIdErrorComponent,
    )
    from ..models.queues_items_partial_update_set_module_id_error_component import (
        QueuesItemsPartialUpdateSetModuleIdErrorComponent,
    )
    from ..models.queues_items_partial_update_set_nested_queue_id_error_component import (
        QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent,
    )
    from ..models.queues_items_partial_update_set_tags_id_error_component import (
        QueuesItemsPartialUpdateSetTagsIdErrorComponent,
    )


T = TypeVar("T", bound="QueuesItemsPartialUpdateValidationError")


@_attrs_define
class QueuesItemsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['QueuesItemsPartialUpdateContinueOnRedoErrorComponent',
            'QueuesItemsPartialUpdateEnabledErrorComponent', 'QueuesItemsPartialUpdateNonFieldErrorsErrorComponent',
            'QueuesItemsPartialUpdateOrderErrorComponent', 'QueuesItemsPartialUpdateQueueRuleErrorComponent',
            'QueuesItemsPartialUpdateSetExerciseIdErrorComponent', 'QueuesItemsPartialUpdateSetModuleIdErrorComponent',
            'QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent', 'QueuesItemsPartialUpdateSetTagsIdErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "QueuesItemsPartialUpdateContinueOnRedoErrorComponent",
            "QueuesItemsPartialUpdateEnabledErrorComponent",
            "QueuesItemsPartialUpdateNonFieldErrorsErrorComponent",
            "QueuesItemsPartialUpdateOrderErrorComponent",
            "QueuesItemsPartialUpdateQueueRuleErrorComponent",
            "QueuesItemsPartialUpdateSetExerciseIdErrorComponent",
            "QueuesItemsPartialUpdateSetModuleIdErrorComponent",
            "QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent",
            "QueuesItemsPartialUpdateSetTagsIdErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.queues_items_partial_update_continue_on_redo_error_component import (
            QueuesItemsPartialUpdateContinueOnRedoErrorComponent,
        )
        from ..models.queues_items_partial_update_enabled_error_component import (
            QueuesItemsPartialUpdateEnabledErrorComponent,
        )
        from ..models.queues_items_partial_update_non_field_errors_error_component import (
            QueuesItemsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.queues_items_partial_update_order_error_component import (
            QueuesItemsPartialUpdateOrderErrorComponent,
        )
        from ..models.queues_items_partial_update_queue_rule_error_component import (
            QueuesItemsPartialUpdateQueueRuleErrorComponent,
        )
        from ..models.queues_items_partial_update_set_exercise_id_error_component import (
            QueuesItemsPartialUpdateSetExerciseIdErrorComponent,
        )
        from ..models.queues_items_partial_update_set_module_id_error_component import (
            QueuesItemsPartialUpdateSetModuleIdErrorComponent,
        )
        from ..models.queues_items_partial_update_set_nested_queue_id_error_component import (
            QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, QueuesItemsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateSetExerciseIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateSetModuleIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateQueueRuleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateContinueOnRedoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, QueuesItemsPartialUpdateEnabledErrorComponent):
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
        from ..models.queues_items_partial_update_continue_on_redo_error_component import (
            QueuesItemsPartialUpdateContinueOnRedoErrorComponent,
        )
        from ..models.queues_items_partial_update_enabled_error_component import (
            QueuesItemsPartialUpdateEnabledErrorComponent,
        )
        from ..models.queues_items_partial_update_non_field_errors_error_component import (
            QueuesItemsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.queues_items_partial_update_order_error_component import (
            QueuesItemsPartialUpdateOrderErrorComponent,
        )
        from ..models.queues_items_partial_update_queue_rule_error_component import (
            QueuesItemsPartialUpdateQueueRuleErrorComponent,
        )
        from ..models.queues_items_partial_update_set_exercise_id_error_component import (
            QueuesItemsPartialUpdateSetExerciseIdErrorComponent,
        )
        from ..models.queues_items_partial_update_set_module_id_error_component import (
            QueuesItemsPartialUpdateSetModuleIdErrorComponent,
        )
        from ..models.queues_items_partial_update_set_nested_queue_id_error_component import (
            QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent,
        )
        from ..models.queues_items_partial_update_set_tags_id_error_component import (
            QueuesItemsPartialUpdateSetTagsIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "QueuesItemsPartialUpdateContinueOnRedoErrorComponent",
                "QueuesItemsPartialUpdateEnabledErrorComponent",
                "QueuesItemsPartialUpdateNonFieldErrorsErrorComponent",
                "QueuesItemsPartialUpdateOrderErrorComponent",
                "QueuesItemsPartialUpdateQueueRuleErrorComponent",
                "QueuesItemsPartialUpdateSetExerciseIdErrorComponent",
                "QueuesItemsPartialUpdateSetModuleIdErrorComponent",
                "QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent",
                "QueuesItemsPartialUpdateSetTagsIdErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_0 = (
                        QueuesItemsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_1 = (
                        QueuesItemsPartialUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_2 = (
                        QueuesItemsPartialUpdateSetExerciseIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_3 = (
                        QueuesItemsPartialUpdateSetNestedQueueIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_4 = (
                        QueuesItemsPartialUpdateSetModuleIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_5 = (
                        QueuesItemsPartialUpdateQueueRuleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_6 = (
                        QueuesItemsPartialUpdateContinueOnRedoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_queues_items_partial_update_error_type_7 = (
                        QueuesItemsPartialUpdateEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_queues_items_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_queues_items_partial_update_error_type_8 = (
                    QueuesItemsPartialUpdateSetTagsIdErrorComponent.from_dict(data)
                )

                return componentsschemas_queues_items_partial_update_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        queues_items_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        queues_items_partial_update_validation_error.additional_properties = d
        return queues_items_partial_update_validation_error

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
