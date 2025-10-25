from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_error_enum import ClientErrorEnum

if TYPE_CHECKING:
    from ..models.error_405 import Error405


T = TypeVar("T", bound="ErrorResponse405")


@_attrs_define
class ErrorResponse405:
    """
    Attributes:
        type_ (ClientErrorEnum):
            * `client_error` - Client Error
        errors (list['Error405']):
    """

    hive_client: "HiveClient"
    type_: ClientErrorEnum
    errors: list["Error405"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        from ..models.error_405 import Error405

        d = dict(src_dict)
        type_ = ClientErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = Error405.from_dict(errors_item_data)

            errors.append(errors_item)

        error_response_405 = cls(
            type_=type_,
            errors=errors,
        )

        error_response_405.additional_properties = d
        return error_response_405

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
