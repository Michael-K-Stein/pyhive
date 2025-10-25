from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_partial_update_help_error_component_attr import (
    NotificationPartialUpdateHelpErrorComponentAttr,
)
from ..models.notification_partial_update_help_error_component_code import (
    NotificationPartialUpdateHelpErrorComponentCode,
)

T = TypeVar("T", bound="NotificationPartialUpdateHelpErrorComponent")


@_attrs_define
class NotificationPartialUpdateHelpErrorComponent:
    """
    Attributes:
        attr (NotificationPartialUpdateHelpErrorComponentAttr): * `help` - help
        code (NotificationPartialUpdateHelpErrorComponentCode): * `does_not_exist` - does_not_exist
            * `incorrect_type` - incorrect_type
        detail (str):
    """

    attr: NotificationPartialUpdateHelpErrorComponentAttr
    code: NotificationPartialUpdateHelpErrorComponentCode
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attr = self.attr.value

        code = self.code.value

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attr": attr,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attr = NotificationPartialUpdateHelpErrorComponentAttr(d.pop("attr"))

        code = NotificationPartialUpdateHelpErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        notification_partial_update_help_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        notification_partial_update_help_error_component.additional_properties = d
        return notification_partial_update_help_error_component

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
