from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.notification_create_assignment_error_component import NotificationCreateAssignmentErrorComponent
    from ..models.notification_create_comment_error_component import NotificationCreateCommentErrorComponent
    from ..models.notification_create_help_error_component import NotificationCreateHelpErrorComponent
    from ..models.notification_create_non_field_errors_error_component import (
        NotificationCreateNonFieldErrorsErrorComponent,
    )
    from ..models.notification_create_user_error_component import NotificationCreateUserErrorComponent
    from ..models.notification_create_was_read_error_component import NotificationCreateWasReadErrorComponent


T = TypeVar("T", bound="NotificationCreateValidationError")


@_attrs_define
class NotificationCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['NotificationCreateAssignmentErrorComponent', 'NotificationCreateCommentErrorComponent',
            'NotificationCreateHelpErrorComponent', 'NotificationCreateNonFieldErrorsErrorComponent',
            'NotificationCreateUserErrorComponent', 'NotificationCreateWasReadErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "NotificationCreateAssignmentErrorComponent",
            "NotificationCreateCommentErrorComponent",
            "NotificationCreateHelpErrorComponent",
            "NotificationCreateNonFieldErrorsErrorComponent",
            "NotificationCreateUserErrorComponent",
            "NotificationCreateWasReadErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_create_assignment_error_component import NotificationCreateAssignmentErrorComponent
        from ..models.notification_create_comment_error_component import NotificationCreateCommentErrorComponent
        from ..models.notification_create_help_error_component import NotificationCreateHelpErrorComponent
        from ..models.notification_create_non_field_errors_error_component import (
            NotificationCreateNonFieldErrorsErrorComponent,
        )
        from ..models.notification_create_was_read_error_component import NotificationCreateWasReadErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, NotificationCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationCreateHelpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationCreateAssignmentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationCreateCommentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, NotificationCreateWasReadErrorComponent):
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
        from ..models.notification_create_assignment_error_component import NotificationCreateAssignmentErrorComponent
        from ..models.notification_create_comment_error_component import NotificationCreateCommentErrorComponent
        from ..models.notification_create_help_error_component import NotificationCreateHelpErrorComponent
        from ..models.notification_create_non_field_errors_error_component import (
            NotificationCreateNonFieldErrorsErrorComponent,
        )
        from ..models.notification_create_user_error_component import NotificationCreateUserErrorComponent
        from ..models.notification_create_was_read_error_component import NotificationCreateWasReadErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "NotificationCreateAssignmentErrorComponent",
                "NotificationCreateCommentErrorComponent",
                "NotificationCreateHelpErrorComponent",
                "NotificationCreateNonFieldErrorsErrorComponent",
                "NotificationCreateUserErrorComponent",
                "NotificationCreateWasReadErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_create_error_type_0 = (
                        NotificationCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_create_error_type_1 = NotificationCreateHelpErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_notification_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_create_error_type_2 = (
                        NotificationCreateAssignmentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_create_error_type_3 = (
                        NotificationCreateCommentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_notification_create_error_type_4 = (
                        NotificationCreateWasReadErrorComponent.from_dict(data)
                    )

                    return componentsschemas_notification_create_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_notification_create_error_type_5 = NotificationCreateUserErrorComponent.from_dict(
                    data
                )

                return componentsschemas_notification_create_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        notification_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        notification_create_validation_error.additional_properties = d
        return notification_create_validation_error

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
