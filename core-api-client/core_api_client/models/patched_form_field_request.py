from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.form_field_type_enum import FormFieldTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedFormFieldRequest")


@_attrs_define
class PatchedFormFieldRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        type_ (Union[Unset, FormFieldTypeEnum]): * `text` - Text
            * `number` - Number
            * `multiple` - Multiple
            * `multiResponse` - Multiresponse
        order (Union[Unset, int]):
        required (Union[Unset, bool]):
        staff_responses (Union[Unset, bool]):
        hanich_responses (Union[Unset, bool]):
        has_value (Union[Unset, bool]):
        lower_limit (Union[None, Unset, int]):
        upper_limit (Union[None, Unset, int]):
        choices (Union[None, Unset, list[str]]):
        segel_only (Union[Unset, bool]):
        metadata (Union[Unset, Any]):
        groups (Union[Unset, list[int]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, FormFieldTypeEnum] = UNSET
    order: Union[Unset, int] = UNSET
    required: Union[Unset, bool] = UNSET
    staff_responses: Union[Unset, bool] = UNSET
    hanich_responses: Union[Unset, bool] = UNSET
    has_value: Union[Unset, bool] = UNSET
    lower_limit: Union[None, Unset, int] = UNSET
    upper_limit: Union[None, Unset, int] = UNSET
    choices: Union[None, Unset, list[str]] = UNSET
    segel_only: Union[Unset, bool] = UNSET
    metadata: Union[Unset, Any] = UNSET
    groups: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        order = self.order

        required = self.required

        staff_responses = self.staff_responses

        hanich_responses = self.hanich_responses

        has_value = self.has_value

        lower_limit: Union[None, Unset, int]
        if isinstance(self.lower_limit, Unset):
            lower_limit = UNSET
        else:
            lower_limit = self.lower_limit

        upper_limit: Union[None, Unset, int]
        if isinstance(self.upper_limit, Unset):
            upper_limit = UNSET
        else:
            upper_limit = self.upper_limit

        choices: Union[None, Unset, list[str]]
        if isinstance(self.choices, Unset):
            choices = UNSET
        elif isinstance(self.choices, list):
            choices = self.choices

        else:
            choices = self.choices

        segel_only = self.segel_only

        metadata = self.metadata

        groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if order is not UNSET:
            field_dict["order"] = order
        if required is not UNSET:
            field_dict["required"] = required
        if staff_responses is not UNSET:
            field_dict["staff_responses"] = staff_responses
        if hanich_responses is not UNSET:
            field_dict["hanich_responses"] = hanich_responses
        if has_value is not UNSET:
            field_dict["has_value"] = has_value
        if lower_limit is not UNSET:
            field_dict["lower_limit"] = lower_limit
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit
        if choices is not UNSET:
            field_dict["choices"] = choices
        if segel_only is not UNSET:
            field_dict["segel_only"] = segel_only
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.type_, Unset):
            files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        if not isinstance(self.order, Unset):
            files.append(("order", (None, str(self.order).encode(), "text/plain")))

        if not isinstance(self.required, Unset):
            files.append(("required", (None, str(self.required).encode(), "text/plain")))

        if not isinstance(self.staff_responses, Unset):
            files.append(("staff_responses", (None, str(self.staff_responses).encode(), "text/plain")))

        if not isinstance(self.hanich_responses, Unset):
            files.append(("hanich_responses", (None, str(self.hanich_responses).encode(), "text/plain")))

        if not isinstance(self.has_value, Unset):
            files.append(("has_value", (None, str(self.has_value).encode(), "text/plain")))

        if not isinstance(self.lower_limit, Unset):
            if isinstance(self.lower_limit, int):
                files.append(("lower_limit", (None, str(self.lower_limit).encode(), "text/plain")))
            else:
                files.append(("lower_limit", (None, str(self.lower_limit).encode(), "text/plain")))

        if not isinstance(self.upper_limit, Unset):
            if isinstance(self.upper_limit, int):
                files.append(("upper_limit", (None, str(self.upper_limit).encode(), "text/plain")))
            else:
                files.append(("upper_limit", (None, str(self.upper_limit).encode(), "text/plain")))

        if not isinstance(self.choices, Unset):
            if isinstance(self.choices, list):
                for choices_type_0_item_element in self.choices:
                    files.append(("choices", (None, str(choices_type_0_item_element).encode(), "text/plain")))
            else:
                files.append(("choices", (None, str(self.choices).encode(), "text/plain")))

        if not isinstance(self.segel_only, Unset):
            files.append(("segel_only", (None, str(self.segel_only).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        if not isinstance(self.groups, Unset):
            for groups_item_element in self.groups:
                files.append(("groups", (None, str(groups_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FormFieldTypeEnum]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FormFieldTypeEnum(_type_)

        order = d.pop("order", UNSET)

        required = d.pop("required", UNSET)

        staff_responses = d.pop("staff_responses", UNSET)

        hanich_responses = d.pop("hanich_responses", UNSET)

        has_value = d.pop("has_value", UNSET)

        def _parse_lower_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lower_limit = _parse_lower_limit(d.pop("lower_limit", UNSET))

        def _parse_upper_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        upper_limit = _parse_upper_limit(d.pop("upper_limit", UNSET))

        def _parse_choices(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                choices_type_0 = cast(list[str], data)

                return choices_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        choices = _parse_choices(d.pop("choices", UNSET))

        segel_only = d.pop("segel_only", UNSET)

        metadata = d.pop("metadata", UNSET)

        groups = cast(list[int], d.pop("groups", UNSET))

        patched_form_field_request = cls(
            name=name,
            description=description,
            type_=type_,
            order=order,
            required=required,
            staff_responses=staff_responses,
            hanich_responses=hanich_responses,
            has_value=has_value,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            choices=choices,
            segel_only=segel_only,
            metadata=metadata,
            groups=groups,
        )

        patched_form_field_request.additional_properties = d
        return patched_form_field_request

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
