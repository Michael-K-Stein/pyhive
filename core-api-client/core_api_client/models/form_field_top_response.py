from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_type_enum import FormFieldTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormFieldTopResponse")


@_attrs_define
class FormFieldTopResponse:
    """
    Attributes:
        id (int):
        exercise (int):
        name (str):
        type_ (FormFieldTypeEnum):
            * `text` - Text
            * `number` - Number
            * `multiple` - Multiple
            * `multiResponse` - Multiresponse
        order (int):
        required (bool):
        staff_responses (bool):
        hanich_responses (bool):
        has_value (bool):
        segel_only (bool):
        top_responses (list[str]):
        description (Union[Unset, str]):
        lower_limit (Union[None, Unset, int]):
        upper_limit (Union[None, Unset, int]):
        choices (Union[None, Unset, list[str]]):
        metadata (Union[Unset, Any]):
        groups (Union[Unset, list[int]]):
    """

    id: int
    exercise: int
    name: str
    type_: FormFieldTypeEnum
    order: int
    required: bool
    staff_responses: bool
    hanich_responses: bool
    has_value: bool
    segel_only: bool
    top_responses: list[str]
    description: Union[Unset, str] = UNSET
    lower_limit: Union[None, Unset, int] = UNSET
    upper_limit: Union[None, Unset, int] = UNSET
    choices: Union[None, Unset, list[str]] = UNSET
    metadata: Union[Unset, Any] = UNSET
    groups: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        exercise = self.exercise

        name = self.name

        type_ = self.type_.value

        order = self.order

        required = self.required

        staff_responses = self.staff_responses

        hanich_responses = self.hanich_responses

        has_value = self.has_value

        segel_only = self.segel_only

        top_responses = self.top_responses

        description = self.description

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

        metadata = self.metadata

        groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "exercise": exercise,
                "name": name,
                "type": type_,
                "order": order,
                "required": required,
                "staff_responses": staff_responses,
                "hanich_responses": hanich_responses,
                "has_value": has_value,
                "segel_only": segel_only,
                "top_responses": top_responses,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if lower_limit is not UNSET:
            field_dict["lower_limit"] = lower_limit
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit
        if choices is not UNSET:
            field_dict["choices"] = choices
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        exercise = d.pop("exercise")

        name = d.pop("name")

        type_ = FormFieldTypeEnum(d.pop("type"))

        order = d.pop("order")

        required = d.pop("required")

        staff_responses = d.pop("staff_responses")

        hanich_responses = d.pop("hanich_responses")

        has_value = d.pop("has_value")

        segel_only = d.pop("segel_only")

        top_responses = cast(list[str], d.pop("top_responses"))

        description = d.pop("description", UNSET)

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

        metadata = d.pop("metadata", UNSET)

        groups = cast(list[int], d.pop("groups", UNSET))

        form_field_top_response = cls(
            id=id,
            exercise=exercise,
            name=name,
            type_=type_,
            order=order,
            required=required,
            staff_responses=staff_responses,
            hanich_responses=hanich_responses,
            has_value=has_value,
            segel_only=segel_only,
            top_responses=top_responses,
            description=description,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            choices=choices,
            metadata=metadata,
            groups=groups,
        )

        form_field_top_response.additional_properties = d
        return form_field_top_response

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
