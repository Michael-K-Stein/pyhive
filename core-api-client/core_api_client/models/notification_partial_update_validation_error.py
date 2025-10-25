from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.notification_partial_update_assignment_error_component import (
        NotificationPartialUpdateAssignmentErrorComponent,
    )
    from ..models.notification_partial_update_comment_error_component import (
        NotificationPartialUpdateCommentErrorComponent,
    )
    from ..models.notification_partial_update_help_error_component import NotificationPartialUpdateHelpErrorComponent
    from ..models.notification_partial_update_non_field_errors_error_component import (
        NotificationPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.notification_partial_update_user_error_component import NotificationPartialUpdateUserErrorComponent
    from ..models.notification_partial_update_was_read_error_component import (
        NotificationPartialUpdateWasReadErrorComponent,
    )


T = TypeVar("T", bound="NotificationPartialUpdateValidationError")


@_attrs_define
class NotificationPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['NotificationPartialUpdateAssignmentErrorComponent',
            'NotificationPartialUpdateCommentErrorComponent', 'NotificationPartialUpdateHelpErrorComponent',
            'NotificationPartialUpdateNonFieldErrorsErrorComponent', 'NotificationPartialUpdateUserErrorComponent',
            'NotificationPartialUpdateWasReadErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "NotificationPartialUpdateAssignmentErrorComponent",
            "NotificationPartialUpdateCommentErrorComponent",
            "NotificationPartialUpdateHelpErrorComponent",
            "NotificationPartialUpdateNonFieldErrorsErrorComponent",
            "NotificationPartialUpdateUserErrorComponent",
            "NotificationPartialUpdateWasReadErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_partial_update_assignment_error_component import (
            NotificationPartialUpdateAssignmentErrorComponent,
        )
        from ..models.notification_partial_update_comment_error_component import (
            NotificationPartialUpdateCommentErrorComponent,
        )
        from ..models.notification_partial_update_help_error_component import (
            NotificationPartialUpdateHelpErrorComponent,
        )
        from ..models.notification_partial_update_non_field_errors_error_component import (
            NotificationPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.notification_partial_update_was_read_error_component import (
            NotificationPartialUpdateWasReadErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, NotificationPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationPartialUpdateHelpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationPartialUpdateAssignmentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationPartialUpdateCommentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationPartialUpdateWasReadErrorComponent):
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
        from ..models.notification_partial_update_assignment_error_component import (
            NotificationPartialUpdateAssignmentErrorComponent,
        )
        from ..models.notification_partial_update_comment_error_component import (
            NotificationPartialUpdateCommentErrorComponent,
        )
        from ..models.notification_partial_update_help_error_component import (
            NotificationPartialUpdateHelpErrorComponent,
        )
        from ..models.notification_partial_update_non_field_errors_error_component import (
            NotificationPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.notification_partial_update_user_error_component import (
            NotificationPartialUpdateUserErrorComponent,
        )
        from ..models.notification_partial_update_was_read_error_component import (
            NotificationPartialUpdateWasReadErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "NotificationPartialUpdateAssignmentErrorComponent",
                "NotificationPartialUpdateCommentErrorComponent",
                "NotificationPartialUpdateHelpErrorComponent",
                "NotificationPartialUpdateNonFieldErrorsErrorComponent",
                "NotificationPartialUpdateUserErrorComponent",
                "NotificationPartialUpdateWasReadErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_partial_update_error_type_0 = (
                        NotificationPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_partial_update_error_type_1 = (
                        NotificationPartialUpdateHelpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_partial_update_error_type_2 = (
                        NotificationPartialUpdateAssignmentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_partial_update_error_type_3 = (
                        NotificationPartialUpdateCommentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_partial_update_error_type_4 = (
                        NotificationPartialUpdateWasReadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_notification_partial_update_error_type_5 = (
                    NotificationPartialUpdateUserErrorComponent.from_dict(data)
                )

                return componentsschemas_notification_partial_update_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        notification_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        notification_partial_update_validation_error.additional_properties = d
        return notification_partial_update_validation_error

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
