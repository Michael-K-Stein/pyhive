from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_status_enum import SyncStatusEnum
from src.common import UNSET, Unset

T = TypeVar("T", bound="Program")


@_attrs_define
class Program:
    """
    Attributes:
        id (int):
        name (str):
        checker (int):
        sync_status (SyncStatusEnum):
            * `Creating` - Creating
            * `Deleting` - Deleting
            * `Normal` - Normal
            * `Error` - Error
        sync_message (Union[None, str]):
        default_class (Union[None, Unset, int]):
        auto_toilet (Union[Unset, bool]):
        hanich_raise_hand (Union[Unset, bool]):
        auto_schedule (Union[Unset, bool]):
        auto_room (Union[Unset, bool]):
        hanich_day_only (Union[Unset, bool]):
        hanich_work_name (Union[Unset, bool]):
        auto_toilet_count (Union[Unset, int]):
        hanich_classes_only (Union[Unset, bool]):
        hanich_schedule (Union[Unset, bool]):
    """

    hive_client: "HiveClient"
    id: int
    name: str
    checker: int
    sync_status: SyncStatusEnum
    sync_message: Union[None, str]
    default_class: Union[None, Unset, int] = UNSET
    auto_toilet: Union[Unset, bool] = UNSET
    hanich_raise_hand: Union[Unset, bool] = UNSET
    auto_schedule: Union[Unset, bool] = UNSET
    auto_room: Union[Unset, bool] = UNSET
    hanich_day_only: Union[Unset, bool] = UNSET
    hanich_work_name: Union[Unset, bool] = UNSET
    auto_toilet_count: Union[Unset, int] = UNSET
    hanich_classes_only: Union[Unset, bool] = UNSET
    hanich_schedule: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        checker = self.checker

        sync_status = self.sync_status.value

        sync_message: Union[None, str]
        sync_message = self.sync_message

        default_class: Union[None, Unset, int]
        if isinstance(self.default_class, Unset):
            default_class = UNSET
        else:
            default_class = self.default_class

        auto_toilet = self.auto_toilet

        hanich_raise_hand = self.hanich_raise_hand

        auto_schedule = self.auto_schedule

        auto_room = self.auto_room

        hanich_day_only = self.hanich_day_only

        hanich_work_name = self.hanich_work_name

        auto_toilet_count = self.auto_toilet_count

        hanich_classes_only = self.hanich_classes_only

        hanich_schedule = self.hanich_schedule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "checker": checker,
                "sync_status": sync_status,
                "sync_message": sync_message,
            }
        )
        if default_class is not UNSET:
            field_dict["default_class"] = default_class
        if auto_toilet is not UNSET:
            field_dict["auto_toilet"] = auto_toilet
        if hanich_raise_hand is not UNSET:
            field_dict["hanich_raise_hand"] = hanich_raise_hand
        if auto_schedule is not UNSET:
            field_dict["auto_schedule"] = auto_schedule
        if auto_room is not UNSET:
            field_dict["auto_room"] = auto_room
        if hanich_day_only is not UNSET:
            field_dict["hanich_day_only"] = hanich_day_only
        if hanich_work_name is not UNSET:
            field_dict["hanich_work_name"] = hanich_work_name
        if auto_toilet_count is not UNSET:
            field_dict["auto_toilet_count"] = auto_toilet_count
        if hanich_classes_only is not UNSET:
            field_dict["hanich_classes_only"] = hanich_classes_only
        if hanich_schedule is not UNSET:
            field_dict["hanich_schedule"] = hanich_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        checker = d.pop("checker")

        sync_status = SyncStatusEnum(d.pop("sync_status"))

        def _parse_sync_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sync_message = _parse_sync_message(d.pop("sync_message"))

        def _parse_default_class(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_class = _parse_default_class(d.pop("default_class", UNSET))

        auto_toilet = d.pop("auto_toilet", UNSET)

        hanich_raise_hand = d.pop("hanich_raise_hand", UNSET)

        auto_schedule = d.pop("auto_schedule", UNSET)

        auto_room = d.pop("auto_room", UNSET)

        hanich_day_only = d.pop("hanich_day_only", UNSET)

        hanich_work_name = d.pop("hanich_work_name", UNSET)

        auto_toilet_count = d.pop("auto_toilet_count", UNSET)

        hanich_classes_only = d.pop("hanich_classes_only", UNSET)

        hanich_schedule = d.pop("hanich_schedule", UNSET)

        program = cls(
            hive_client=hive_client,
            id=id,
            name=name,
            checker=checker,
            sync_status=sync_status,
            sync_message=sync_message,
            default_class=default_class,
            auto_toilet=auto_toilet,
            hanich_raise_hand=hanich_raise_hand,
            auto_schedule=auto_schedule,
            auto_room=auto_room,
            hanich_day_only=hanich_day_only,
            hanich_work_name=hanich_work_name,
            auto_toilet_count=auto_toilet_count,
            hanich_classes_only=hanich_classes_only,
            hanich_schedule=hanich_schedule,
        )

        program.additional_properties = d
        return program

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
