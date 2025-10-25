from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queues_list_program_id_in_error_component_attr import QueuesListProgramIdInErrorComponentAttr
from ..models.queues_list_program_id_in_error_component_code import QueuesListProgramIdInErrorComponentCode

T = TypeVar("T", bound="QueuesListProgramIdInErrorComponent")


@_attrs_define
class QueuesListProgramIdInErrorComponent:
    """
    Attributes:
        attr (QueuesListProgramIdInErrorComponentAttr): * `program__id__in` - program__id__in
        code (QueuesListProgramIdInErrorComponentCode): * `invalid_choice` - invalid_choice
            * `invalid_list` - invalid_list
            * `invalid_pk_value` - invalid_pk_value
        detail (str):
    """

    attr: QueuesListProgramIdInErrorComponentAttr
    code: QueuesListProgramIdInErrorComponentCode
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
        attr = QueuesListProgramIdInErrorComponentAttr(d.pop("attr"))

        code = QueuesListProgramIdInErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        queues_list_program_id_in_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        queues_list_program_id_in_error_component.additional_properties = d
        return queues_list_program_id_in_error_component

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
