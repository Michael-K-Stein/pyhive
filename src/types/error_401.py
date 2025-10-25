from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_code_401_enum import ErrorCode401Enum

T = TypeVar("T", bound="Error401")


@_attrs_define
class Error401:
    """
    Attributes:
        code (ErrorCode401Enum):
            * `authentication_failed` - Authentication Failed
            * `not_authenticated` - Not Authenticated
        detail (str):
        attr (Union[None, str]):
    """

    hive_client: "HiveClient"
    code: ErrorCode401Enum
    detail: str
    attr: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        detail = self.detail

        attr: Union[None, str]
        attr = self.attr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "detail": detail,
                "attr": attr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        code = ErrorCode401Enum(d.pop("code"))

        detail = d.pop("detail")

        def _parse_attr(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        attr = _parse_attr(d.pop("attr"))

        error_401 = cls(
            code=code,
            detail=detail,
            attr=attr,
        )

        error_401.additional_properties = d
        return error_401

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
