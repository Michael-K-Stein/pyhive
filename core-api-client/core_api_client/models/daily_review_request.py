import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types

T = TypeVar("T", bound="DailyReviewRequest")


@_attrs_define
class DailyReviewRequest:
    """
    Attributes:
        date (datetime.datetime):
        show_lesson_names (bool):
        hide_work_details (bool):
    """

    date: datetime.datetime
    show_lesson_names: bool
    hide_work_details: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        show_lesson_names = self.show_lesson_names

        hide_work_details = self.hide_work_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "show_lesson_names": show_lesson_names,
                "hide_work_details": hide_work_details,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("date", (None, self.date.isoformat().encode(), "text/plain")))

        files.append(("show_lesson_names", (None, str(self.show_lesson_names).encode(), "text/plain")))

        files.append(("hide_work_details", (None, str(self.hide_work_details).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date"))

        show_lesson_names = d.pop("show_lesson_names")

        hide_work_details = d.pop("hide_work_details")

        daily_review_request = cls(
            date=date,
            show_lesson_names=show_lesson_names,
            hide_work_details=hide_work_details,
        )

        daily_review_request.additional_properties = d
        return daily_review_request

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
