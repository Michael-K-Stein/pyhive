from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_enum import ActionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusRequest")


@_attrs_define
class StatusRequest:
    """
    Attributes:
        action (ActionEnum):
            * `Handling` - Handling
            * `No Check` - Nocheck
            * `Built` - Built
            * `Finished` - Finished
            * `Sending` - Sending
            * `Error` - Error
            * `Success` - Success
        payload (Union[None, Unset, str]):
    """

    action: ActionEnum
    payload: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        payload: Union[None, Unset, str]
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ActionEnum(d.pop("action"))

        def _parse_payload(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payload = _parse_payload(d.pop("payload", UNSET))

        status_request = cls(
            action=action,
            payload=payload,
        )

        status_request.additional_properties = d
        return status_request

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
