from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.event_type_enum import EventTypeEnum
from src.common import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_attendees_type_0_item import EventAttendeesType0Item


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        start (datetime.datetime):
        end (datetime.datetime):
        title (Union[None, str]):
        attendees (Union[None, list['EventAttendeesType0Item']]):
        subject_id (Union[None, int]):
        subject_name (Union[None, str]):
        color (Union[None, str]):
        type_ (EventTypeEnum):
            * `פתבס` - Patbas
            * `הרצאה` - Lecture
            * `עע` - Work
        module_id (Union[None, int]):
        lesson_name (Union[None, str]):
        location (Union[None, Unset, str]):
    """

    hive_client: "HiveClient"
    start: datetime.datetime
    end: datetime.datetime
    title: Union[None, str]
    attendees: Union[None, list["EventAttendeesType0Item"]]
    subject_id: Union[None, int]
    subject_name: Union[None, str]
    color: Union[None, str]
    type_: EventTypeEnum
    module_id: Union[None, int]
    lesson_name: Union[None, str]
    location: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        title: Union[None, str]
        title = self.title

        attendees: Union[None, list[dict[str, Any]]]
        if isinstance(self.attendees, list):
            attendees = []
            for attendees_type_0_item_data in self.attendees:
                attendees_type_0_item = attendees_type_0_item_data.to_dict()
                attendees.append(attendees_type_0_item)

        else:
            attendees = self.attendees

        subject_id: Union[None, int]
        subject_id = self.subject_id

        subject_name: Union[None, str]
        subject_name = self.subject_name

        color: Union[None, str]
        color = self.color

        type_ = self.type_.value

        module_id: Union[None, int]
        module_id = self.module_id

        lesson_name: Union[None, str]
        lesson_name = self.lesson_name

        location: Union[None, Unset, str]
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "title": title,
                "attendees": attendees,
                "subject_id": subject_id,
                "subject_name": subject_name,
                "color": color,
                "type": type_,
                "module_id": module_id,
                "lesson_name": lesson_name,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        from ..models.event_attendees_type_0_item import EventAttendeesType0Item

        d = dict(src_dict)
        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        def _parse_title(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        title = _parse_title(d.pop("title"))

        def _parse_attendees(data: object) -> Union[None, list["EventAttendeesType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attendees_type_0 = []
                _attendees_type_0 = data
                for attendees_type_0_item_data in _attendees_type_0:
                    attendees_type_0_item = EventAttendeesType0Item.from_dict(attendees_type_0_item_data)

                    attendees_type_0.append(attendees_type_0_item)

                return attendees_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["EventAttendeesType0Item"]], data)

        attendees = _parse_attendees(d.pop("attendees"))

        def _parse_subject_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        subject_id = _parse_subject_id(d.pop("subject_id"))

        def _parse_subject_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_name = _parse_subject_name(d.pop("subject_name"))

        def _parse_color(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        color = _parse_color(d.pop("color"))

        type_ = EventTypeEnum(d.pop("type"))

        def _parse_module_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        module_id = _parse_module_id(d.pop("module_id"))

        def _parse_lesson_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        lesson_name = _parse_lesson_name(d.pop("lesson_name"))

        def _parse_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location = _parse_location(d.pop("location", UNSET))

        event = cls(
            start=start,
            end=end,
            title=title,
            attendees=attendees,
            subject_id=subject_id,
            subject_name=subject_name,
            color=color,
            type_=type_,
            module_id=module_id,
            lesson_name=lesson_name,
            location=location,
        )

        event.additional_properties = d
        return event

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
