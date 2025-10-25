from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignments_responses_create_contents_non_field_errors_error_component_attr import (
    AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentAttr,
)
from ..models.assignments_responses_create_contents_non_field_errors_error_component_code import (
    AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentCode,
)

T = TypeVar("T", bound="AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent")


@_attrs_define
class AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent:
    """
    Attributes:
        attr (AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentAttr): * `contents.non_field_errors` -
            contents.non_field_errors
        code (AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentCode): * `not_a_list` - not_a_list
            * `null` - null
            * `required` - required
        detail (str):
    """

    attr: AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentAttr
    code: AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentCode
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
        attr = AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentAttr(d.pop("attr"))

        code = AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentCode(d.pop("code"))

        detail = d.pop("detail")

        assignments_responses_create_contents_non_field_errors_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        assignments_responses_create_contents_non_field_errors_error_component.additional_properties = d
        return assignments_responses_create_contents_non_field_errors_error_component

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
