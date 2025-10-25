from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queues_create_module_error_component_attr import QueuesCreateModuleErrorComponentAttr
from ..models.queues_create_module_error_component_code import QueuesCreateModuleErrorComponentCode

T = TypeVar("T", bound="QueuesCreateModuleErrorComponent")


@_attrs_define
class QueuesCreateModuleErrorComponent:
    """
    Attributes:
        attr (QueuesCreateModuleErrorComponentAttr): * `module` - module
        code (QueuesCreateModuleErrorComponentCode): * `does_not_exist` - does_not_exist
            * `incorrect_type` - incorrect_type
            * `required` - required
        detail (str):
    """

    attr: QueuesCreateModuleErrorComponentAttr
    code: QueuesCreateModuleErrorComponentCode
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
        attr = QueuesCreateModuleErrorComponentAttr(d.pop("attr"))

        code = QueuesCreateModuleErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        queues_create_module_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        queues_create_module_error_component.additional_properties = d
        return queues_create_module_error_component

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
