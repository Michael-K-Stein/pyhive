import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..models.event_type_enum import EventTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventRequest")


@_attrs_define
class EventRequest:
    """
    Attributes:
        start (datetime.datetime):
        end (datetime.datetime):
        type_ (EventTypeEnum):
            * `פתבס` - Patbas
            * `הרצאה` - Lecture
            * `עע` - Work
        location (Union[None, Unset, str]):
    """

    start: datetime.datetime
    end: datetime.datetime
    type_: EventTypeEnum
    location: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        type_ = self.type_.value

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
                "type": type_,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("start", (None, self.start.isoformat().encode(), "text/plain")))

        files.append(("end", (None, self.end.isoformat().encode(), "text/plain")))

        files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        if not isinstance(self.location, Unset):
            if isinstance(self.location, str):
                files.append(("location", (None, str(self.location).encode(), "text/plain")))
            else:
                files.append(("location", (None, str(self.location).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        type_ = EventTypeEnum(d.pop("type"))

        def _parse_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location = _parse_location(d.pop("location", UNSET))

        event_request = cls(
            start=start,
            end=end,
            type_=type_,
            location=location,
        )

        event_request.additional_properties = d
        return event_request

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
