from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_users_partial_update_non_field_errors_error_component_attr import (
    ManagementUsersPartialUpdateNonFieldErrorsErrorComponentAttr,
)
from ..models.management_users_partial_update_non_field_errors_error_component_code import (
    ManagementUsersPartialUpdateNonFieldErrorsErrorComponentCode,
)

T = TypeVar("T", bound="ManagementUsersPartialUpdateNonFieldErrorsErrorComponent")


@_attrs_define
class ManagementUsersPartialUpdateNonFieldErrorsErrorComponent:
    """
    Attributes:
        attr (ManagementUsersPartialUpdateNonFieldErrorsErrorComponentAttr): * `non_field_errors` - non_field_errors
        code (ManagementUsersPartialUpdateNonFieldErrorsErrorComponentCode): * `invalid` - invalid
            * `null` - null
        detail (str):
    """

    attr: ManagementUsersPartialUpdateNonFieldErrorsErrorComponentAttr
    code: ManagementUsersPartialUpdateNonFieldErrorsErrorComponentCode
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
        attr = ManagementUsersPartialUpdateNonFieldErrorsErrorComponentAttr(d.pop("attr"))

        code = ManagementUsersPartialUpdateNonFieldErrorsErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        management_users_partial_update_non_field_errors_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        management_users_partial_update_non_field_errors_error_component.additional_properties = d
        return management_users_partial_update_non_field_errors_error_component

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
