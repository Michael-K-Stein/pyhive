from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queues_items_create_order_error_component_attr import QueuesItemsCreateOrderErrorComponentAttr
from ..models.queues_items_create_order_error_component_code import QueuesItemsCreateOrderErrorComponentCode

T = TypeVar("T", bound="QueuesItemsCreateOrderErrorComponent")


@_attrs_define
class QueuesItemsCreateOrderErrorComponent:
    """
    Attributes:
        attr (QueuesItemsCreateOrderErrorComponentAttr): * `order` - order
        code (QueuesItemsCreateOrderErrorComponentCode): * `invalid` - invalid
            * `max_string_length` - max_string_length
            * `max_value` - max_value
            * `min_value` - min_value
            * `null` - null
            * `required` - required
        detail (str):
    """

    attr: QueuesItemsCreateOrderErrorComponentAttr
    code: QueuesItemsCreateOrderErrorComponentCode
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
        attr = QueuesItemsCreateOrderErrorComponentAttr(d.pop("attr"))

        code = QueuesItemsCreateOrderErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        queues_items_create_order_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        queues_items_create_order_error_component.additional_properties = d
        return queues_items_create_order_error_component

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
