from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.clearance_enum import ClearanceEnum
from ..models.gender_enum import GenderEnum
from ..models.status_enum import StatusEnum
from src.common import UNSET, Unset

T = TypeVar("T", bound="CourseUser")


@_attrs_define
class CourseUser:
    """
    Attributes:
        id (int):
        display_name (str):
        clearance (ClearanceEnum):
            * `1` - Hanich
            * `2` - Checker
            * `3` - Segel
            * `5` - Admin
        gender (GenderEnum):
            * `Male` - Male
            * `Female` - Female
            * `NonBinary` - Nonbinary
        current_assignment (Union[None, int]):
        current_assignment_options (list[int]):
        mentees (list[int]):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        status (StatusEnum):
            * `Present` - Present
            * `Raised Hand` - Raisedhand
            * `Toilet Request` - Toiletrequest
            * `Toilet` - Toilet
            * `Personal Talk` - Personaltalk
            * `Work Talk` - Worktalk
            * `Medical` - Medical
            * `Prayer` - Prayer
            * `Room` - Room
            * `Home` - Home
        status_date (datetime.datetime):
        avatar_filename (Union[Unset, str]):
        number (Union[None, Unset, int]):
        program (Union[None, Unset, int]):
        checkers_brief (Union[Unset, str]):
        mentor (Union[None, Unset, int]):
        classes (Union[Unset, list[int]]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        queue (Union[None, Unset, int]):
        disable_queue (Union[Unset, bool]):
        user_queue (Union[None, Unset, int]):
        disable_user_queue (Union[Unset, bool]):
        override_queue (Union[None, Unset, int]):
        confirmed (Union[Unset, bool]):
        teacher (Union[Unset, bool]):
        hostname (Union[Unset, str]):
    """

    hive_client: "HiveClient"
    id: int
    display_name: str
    clearance: ClearanceEnum
    gender: GenderEnum
    current_assignment: Union[None, int]
    current_assignment_options: list[int]
    mentees: list[int]
    username: str
    status: StatusEnum
    status_date: datetime.datetime
    avatar_filename: Union[Unset, str] = UNSET
    number: Union[None, Unset, int] = UNSET
    program: Union[None, Unset, int] = UNSET
    checkers_brief: Union[Unset, str] = UNSET
    mentor: Union[None, Unset, int] = UNSET
    classes: Union[Unset, list[int]] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    queue: Union[None, Unset, int] = UNSET
    disable_queue: Union[Unset, bool] = UNSET
    user_queue: Union[None, Unset, int] = UNSET
    disable_user_queue: Union[Unset, bool] = UNSET
    override_queue: Union[None, Unset, int] = UNSET
    confirmed: Union[Unset, bool] = UNSET
    teacher: Union[Unset, bool] = UNSET
    hostname: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        clearance = self.clearance.value

        gender = self.gender.value

        current_assignment: Union[None, int]
        current_assignment = self.current_assignment

        current_assignment_options = self.current_assignment_options

        mentees = self.mentees

        username = self.username

        status = self.status.value

        status_date = self.status_date.isoformat()

        avatar_filename = self.avatar_filename

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        program: Union[None, Unset, int]
        if isinstance(self.program, Unset):
            program = UNSET
        else:
            program = self.program

        checkers_brief = self.checkers_brief

        mentor: Union[None, Unset, int]
        if isinstance(self.mentor, Unset):
            mentor = UNSET
        else:
            mentor = self.mentor

        classes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        first_name = self.first_name

        last_name = self.last_name

        queue: Union[None, Unset, int]
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        disable_queue = self.disable_queue

        user_queue: Union[None, Unset, int]
        if isinstance(self.user_queue, Unset):
            user_queue = UNSET
        else:
            user_queue = self.user_queue

        disable_user_queue = self.disable_user_queue

        override_queue: Union[None, Unset, int]
        if isinstance(self.override_queue, Unset):
            override_queue = UNSET
        else:
            override_queue = self.override_queue

        confirmed = self.confirmed

        teacher = self.teacher

        hostname = self.hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "clearance": clearance,
                "gender": gender,
                "current_assignment": current_assignment,
                "current_assignment_options": current_assignment_options,
                "mentees": mentees,
                "username": username,
                "status": status,
                "status_date": status_date,
            }
        )
        if avatar_filename is not UNSET:
            field_dict["avatar_filename"] = avatar_filename
        if number is not UNSET:
            field_dict["number"] = number
        if program is not UNSET:
            field_dict["program"] = program
        if checkers_brief is not UNSET:
            field_dict["checkers_brief"] = checkers_brief
        if mentor is not UNSET:
            field_dict["mentor"] = mentor
        if classes is not UNSET:
            field_dict["classes"] = classes
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if queue is not UNSET:
            field_dict["queue"] = queue
        if disable_queue is not UNSET:
            field_dict["disable_queue"] = disable_queue
        if user_queue is not UNSET:
            field_dict["user_queue"] = user_queue
        if disable_user_queue is not UNSET:
            field_dict["disable_user_queue"] = disable_user_queue
        if override_queue is not UNSET:
            field_dict["override_queue"] = override_queue
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if teacher is not UNSET:
            field_dict["teacher"] = teacher
        if hostname is not UNSET:
            field_dict["hostname"] = hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        clearance = ClearanceEnum(d.pop("clearance"))

        gender = GenderEnum(d.pop("gender"))

        def _parse_current_assignment(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        current_assignment = _parse_current_assignment(d.pop("current_assignment"))

        current_assignment_options = cast(list[int], d.pop("current_assignment_options"))

        mentees = cast(list[int], d.pop("mentees"))

        username = d.pop("username")

        status = StatusEnum(d.pop("status"))

        status_date = isoparse(d.pop("status_date"))

        avatar_filename = d.pop("avatar_filename", UNSET)

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_program(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        program = _parse_program(d.pop("program", UNSET))

        checkers_brief = d.pop("checkers_brief", UNSET)

        def _parse_mentor(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mentor = _parse_mentor(d.pop("mentor", UNSET))

        classes = cast(list[int], d.pop("classes", UNSET))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_queue(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        queue = _parse_queue(d.pop("queue", UNSET))

        disable_queue = d.pop("disable_queue", UNSET)

        def _parse_user_queue(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user_queue = _parse_user_queue(d.pop("user_queue", UNSET))

        disable_user_queue = d.pop("disable_user_queue", UNSET)

        def _parse_override_queue(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        override_queue = _parse_override_queue(d.pop("override_queue", UNSET))

        confirmed = d.pop("confirmed", UNSET)

        teacher = d.pop("teacher", UNSET)

        hostname = d.pop("hostname", UNSET)

        course_user = cls(
            hive_client=hive_client,
            id=id,
            display_name=display_name,
            clearance=clearance,
            gender=gender,
            current_assignment=current_assignment,
            current_assignment_options=current_assignment_options,
            mentees=mentees,
            username=username,
            status=status,
            status_date=status_date,
            avatar_filename=avatar_filename,
            number=number,
            program=program,
            checkers_brief=checkers_brief,
            mentor=mentor,
            classes=classes,
            first_name=first_name,
            last_name=last_name,
            queue=queue,
            disable_queue=disable_queue,
            user_queue=user_queue,
            disable_user_queue=disable_user_queue,
            override_queue=override_queue,
            confirmed=confirmed,
            teacher=teacher,
            hostname=hostname,
        )

        course_user.additional_properties = d
        return course_user

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
