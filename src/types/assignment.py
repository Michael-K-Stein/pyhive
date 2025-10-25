from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.assignment_status_enum import AssignmentStatusEnum
from src.common import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_nested import NotificationNested


T = TypeVar("T", bound="Assignment")


@_attrs_define
class Assignment:
    """
    Attributes:
        id (int):
        user (int):
        checker (Union[None, int]):
        checker_first_name (str):
        checker_last_name (str):
        is_subscribed (bool):
        exercise (int):
        assignment_status (AssignmentStatusEnum):
            * `New` - New
            * `Work In Progress` - Work In Progress
            * `Redo` - Redo
            * `Submitted` - Submitted
            * `AutoChecked` - AutoChecked
            * `Done` - Done
        patbas (bool):
        notifications (list['NotificationNested']):
        last_staff_updated (datetime.datetime):
        work_time (int):
        student_assignment_status (Union[Unset, AssignmentStatusEnum]): * `New` - New
            * `Work In Progress` - Work In Progress
            * `Redo` - Redo
            * `Submitted` - Submitted
            * `AutoChecked` - AutoChecked
            * `Done` - Done
        description (Union[None, Unset, str]):
        submission_count (Union[Unset, int]):
        total_check_count (Union[Unset, int]):
        manual_check_count (Union[Unset, int]):
        flagged (Union[Unset, bool]):
        timer (Union[None, Unset, str]):
    """

    hive_client: "HiveClient"
    id: int
    user: int
    checker: Union[None, int]
    checker_first_name: str
    checker_last_name: str
    is_subscribed: bool
    exercise: int
    assignment_status: AssignmentStatusEnum
    patbas: bool
    notifications: list["NotificationNested"]
    last_staff_updated: datetime.datetime
    work_time: int
    student_assignment_status: Union[Unset, AssignmentStatusEnum] = UNSET
    description: Union[None, Unset, str] = UNSET
    submission_count: Union[Unset, int] = UNSET
    total_check_count: Union[Unset, int] = UNSET
    manual_check_count: Union[Unset, int] = UNSET
    flagged: Union[Unset, bool] = UNSET
    timer: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user

        checker: Union[None, int]
        checker = self.checker

        checker_first_name = self.checker_first_name

        checker_last_name = self.checker_last_name

        is_subscribed = self.is_subscribed

        exercise = self.exercise

        assignment_status = self.assignment_status.value

        patbas = self.patbas

        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)

        last_staff_updated = self.last_staff_updated.isoformat()

        work_time = self.work_time

        student_assignment_status: Union[Unset, str] = UNSET
        if not isinstance(self.student_assignment_status, Unset):
            student_assignment_status = self.student_assignment_status.value

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        submission_count = self.submission_count

        total_check_count = self.total_check_count

        manual_check_count = self.manual_check_count

        flagged = self.flagged

        timer: Union[None, Unset, str]
        if isinstance(self.timer, Unset):
            timer = UNSET
        else:
            timer = self.timer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "checker": checker,
                "checker_first_name": checker_first_name,
                "checker_last_name": checker_last_name,
                "is_subscribed": is_subscribed,
                "exercise": exercise,
                "assignment_status": assignment_status,
                "patbas": patbas,
                "notifications": notifications,
                "last_staff_updated": last_staff_updated,
                "work_time": work_time,
            }
        )
        if student_assignment_status is not UNSET:
            field_dict["student_assignment_status"] = student_assignment_status
        if description is not UNSET:
            field_dict["description"] = description
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count
        if total_check_count is not UNSET:
            field_dict["total_check_count"] = total_check_count
        if manual_check_count is not UNSET:
            field_dict["manual_check_count"] = manual_check_count
        if flagged is not UNSET:
            field_dict["flagged"] = flagged
        if timer is not UNSET:
            field_dict["timer"] = timer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        from ..models.notification_nested import NotificationNested

        d = dict(src_dict)
        id = d.pop("id")

        user = d.pop("user")

        def _parse_checker(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        checker = _parse_checker(d.pop("checker"))

        checker_first_name = d.pop("checker_first_name")

        checker_last_name = d.pop("checker_last_name")

        is_subscribed = d.pop("is_subscribed")

        exercise = d.pop("exercise")

        assignment_status = AssignmentStatusEnum(d.pop("assignment_status"))

        patbas = d.pop("patbas")

        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in _notifications:
            notifications_item = NotificationNested.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        last_staff_updated = isoparse(d.pop("last_staff_updated"))

        work_time = d.pop("work_time")

        _student_assignment_status = d.pop("student_assignment_status", UNSET)
        student_assignment_status: Union[Unset, AssignmentStatusEnum]
        if isinstance(_student_assignment_status, Unset):
            student_assignment_status = UNSET
        else:
            student_assignment_status = AssignmentStatusEnum(_student_assignment_status)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        submission_count = d.pop("submission_count", UNSET)

        total_check_count = d.pop("total_check_count", UNSET)

        manual_check_count = d.pop("manual_check_count", UNSET)

        flagged = d.pop("flagged", UNSET)

        def _parse_timer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timer = _parse_timer(d.pop("timer", UNSET))

        assignment = cls(
            hive_client=hive_client,
            id=id,
            user=user,
            checker=checker,
            checker_first_name=checker_first_name,
            checker_last_name=checker_last_name,
            is_subscribed=is_subscribed,
            exercise=exercise,
            assignment_status=assignment_status,
            patbas=patbas,
            notifications=notifications,
            last_staff_updated=last_staff_updated,
            work_time=work_time,
            student_assignment_status=student_assignment_status,
            description=description,
            submission_count=submission_count,
            total_check_count=total_check_count,
            manual_check_count=manual_check_count,
            flagged=flagged,
            timer=timer,
        )

        assignment.additional_properties = d
        return assignment

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
