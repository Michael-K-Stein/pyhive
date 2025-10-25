from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_classes_queue_create_queue_error_component_attr import (
    ManagementClassesQueueCreateQueueErrorComponentAttr,
)
from ..models.management_classes_queue_create_queue_error_component_code import (
    ManagementClassesQueueCreateQueueErrorComponentCode,
)

T = TypeVar("T", bound="ManagementClassesQueueCreateQueueErrorComponent")


@_attrs_define
class ManagementClassesQueueCreateQueueErrorComponent:
    """
    Attributes:
        attr (ManagementClassesQueueCreateQueueErrorComponentAttr): * `queue` - queue
        code (ManagementClassesQueueCreateQueueErrorComponentCode): * `does_not_exist` - does_not_exist
            * `incorrect_type` - incorrect_type
            * `required` - required
        detail (str):
    """

    attr: ManagementClassesQueueCreateQueueErrorComponentAttr
    code: ManagementClassesQueueCreateQueueErrorComponentCode
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
        attr = ManagementClassesQueueCreateQueueErrorComponentAttr(d.pop("attr"))

        code = ManagementClassesQueueCreateQueueErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        management_classes_queue_create_queue_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        management_classes_queue_create_queue_error_component.additional_properties = d
        return management_classes_queue_create_queue_error_component

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
