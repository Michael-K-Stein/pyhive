from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_status_enum import SyncStatusEnum

T = TypeVar("T", bound="Module")


@_attrs_define
class Module:
    """
    Attributes:
        id (int):
        name (str):
        parent_subject (int):
        order (str):
        sync_status (SyncStatusEnum):
            * `Creating` - Creating
            * `Deleting` - Deleting
            * `Normal` - Normal
            * `Error` - Error
        sync_message (Union[None, str]):
        parent_program_name (str):
        parent_subject_name (str):
        parent_subject_symbol (str):
        segel_path (str): The path that is accessible to staff from their computers
    """

    hive_client: "HiveClient"
    id: int
    name: str
    parent_subject: int
    order: str
    sync_status: SyncStatusEnum
    sync_message: Union[None, str]
    parent_program_name: str
    parent_subject_name: str
    parent_subject_symbol: str
    segel_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_subject = self.parent_subject

        order = self.order

        sync_status = self.sync_status.value

        sync_message: Union[None, str]
        sync_message = self.sync_message

        parent_program_name = self.parent_program_name

        parent_subject_name = self.parent_subject_name

        parent_subject_symbol = self.parent_subject_symbol

        segel_path = self.segel_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "parent_subject": parent_subject,
                "order": order,
                "sync_status": sync_status,
                "sync_message": sync_message,
                "parent_program_name": parent_program_name,
                "parent_subject_name": parent_subject_name,
                "parent_subject_symbol": parent_subject_symbol,
                "segel_path": segel_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        parent_subject = d.pop("parent_subject")

        order = d.pop("order")

        sync_status = SyncStatusEnum(d.pop("sync_status"))

        def _parse_sync_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sync_message = _parse_sync_message(d.pop("sync_message"))

        parent_program_name = d.pop("parent_program_name")

        parent_subject_name = d.pop("parent_subject_name")

        parent_subject_symbol = d.pop("parent_subject_symbol")

        segel_path = d.pop("segel_path")

        module = cls(
            hive_client=hive_client,
            id=id,
            name=name,
            parent_subject=parent_subject,
            order=order,
            sync_status=sync_status,
            sync_message=sync_message,
            parent_program_name=parent_program_name,
            parent_subject_name=parent_subject_name,
            parent_subject_symbol=parent_subject_symbol,
            segel_path=segel_path,
        )

        module.additional_properties = d
        return module

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
