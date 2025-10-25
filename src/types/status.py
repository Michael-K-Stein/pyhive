from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.action_enum import ActionEnum
from src.common import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        id (int):
        time (datetime.datetime):
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

    hive_client: "HiveClient"
    id: int
    time: datetime.datetime
    action: ActionEnum
    payload: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        time = self.time.isoformat()

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
                "id": id,
                "time": time,
                "action": action,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        time = isoparse(d.pop("time"))

        action = ActionEnum(d.pop("action"))

        def _parse_payload(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payload = _parse_payload(d.pop("payload", UNSET))

        status = cls(
            hive_client=hive_client,
            id=id,
            time=time,
            action=action,
            payload=payload,
        )

        status.additional_properties = d
        return status

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
