from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.clearance_enum import ClearanceEnum
from ..models.gender_enum import GenderEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="CourseUserRequest")


@_attrs_define
class CourseUserRequest:
    """
    Attributes:
        clearance (ClearanceEnum):
            * `1` - Hanich
            * `2` - Checker
            * `3` - Segel
            * `5` - Admin
        gender (GenderEnum):
            * `Male` - Male
            * `Female` - Female
            * `NonBinary` - Nonbinary
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
        avatar (Union[File, None, Unset]):
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
        password (Union[Unset, str]):
    """

    clearance: ClearanceEnum
    gender: GenderEnum
    mentees: list[int]
    username: str
    status: StatusEnum
    avatar: Union[File, None, Unset] = UNSET
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
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clearance = self.clearance.value

        gender = self.gender.value

        mentees = self.mentees

        username = self.username

        status = self.status.value

        avatar: Union[FileTypes, None, Unset]
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        elif isinstance(self.avatar, File):
            avatar = self.avatar.to_tuple()

        else:
            avatar = self.avatar

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

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clearance": clearance,
                "gender": gender,
                "mentees": mentees,
                "username": username,
                "status": status,
            }
        )
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
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
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("clearance", (None, str(self.clearance.value).encode(), "text/plain")))

        files.append(("gender", (None, str(self.gender.value).encode(), "text/plain")))

        for mentees_item_element in self.mentees:
            files.append(("mentees", (None, str(mentees_item_element).encode(), "text/plain")))

        files.append(("username", (None, str(self.username).encode(), "text/plain")))

        files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.avatar, Unset):
            if isinstance(self.avatar, File):
                files.append(("avatar", self.avatar.to_tuple()))
            else:
                files.append(("avatar", (None, str(self.avatar).encode(), "text/plain")))

        if not isinstance(self.avatar_filename, Unset):
            files.append(("avatar_filename", (None, str(self.avatar_filename).encode(), "text/plain")))

        if not isinstance(self.number, Unset):
            if isinstance(self.number, int):
                files.append(("number", (None, str(self.number).encode(), "text/plain")))
            else:
                files.append(("number", (None, str(self.number).encode(), "text/plain")))

        if not isinstance(self.program, Unset):
            if isinstance(self.program, int):
                files.append(("program", (None, str(self.program).encode(), "text/plain")))
            else:
                files.append(("program", (None, str(self.program).encode(), "text/plain")))

        if not isinstance(self.checkers_brief, Unset):
            files.append(("checkers_brief", (None, str(self.checkers_brief).encode(), "text/plain")))

        if not isinstance(self.mentor, Unset):
            if isinstance(self.mentor, int):
                files.append(("mentor", (None, str(self.mentor).encode(), "text/plain")))
            else:
                files.append(("mentor", (None, str(self.mentor).encode(), "text/plain")))

        if not isinstance(self.classes, Unset):
            for classes_item_element in self.classes:
                files.append(("classes", (None, str(classes_item_element).encode(), "text/plain")))

        if not isinstance(self.first_name, Unset):
            files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        if not isinstance(self.last_name, Unset):
            files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        if not isinstance(self.queue, Unset):
            if isinstance(self.queue, int):
                files.append(("queue", (None, str(self.queue).encode(), "text/plain")))
            else:
                files.append(("queue", (None, str(self.queue).encode(), "text/plain")))

        if not isinstance(self.disable_queue, Unset):
            files.append(("disable_queue", (None, str(self.disable_queue).encode(), "text/plain")))

        if not isinstance(self.user_queue, Unset):
            if isinstance(self.user_queue, int):
                files.append(("user_queue", (None, str(self.user_queue).encode(), "text/plain")))
            else:
                files.append(("user_queue", (None, str(self.user_queue).encode(), "text/plain")))

        if not isinstance(self.disable_user_queue, Unset):
            files.append(("disable_user_queue", (None, str(self.disable_user_queue).encode(), "text/plain")))

        if not isinstance(self.override_queue, Unset):
            if isinstance(self.override_queue, int):
                files.append(("override_queue", (None, str(self.override_queue).encode(), "text/plain")))
            else:
                files.append(("override_queue", (None, str(self.override_queue).encode(), "text/plain")))

        if not isinstance(self.confirmed, Unset):
            files.append(("confirmed", (None, str(self.confirmed).encode(), "text/plain")))

        if not isinstance(self.teacher, Unset):
            files.append(("teacher", (None, str(self.teacher).encode(), "text/plain")))

        if not isinstance(self.hostname, Unset):
            files.append(("hostname", (None, str(self.hostname).encode(), "text/plain")))

        if not isinstance(self.password, Unset):
            files.append(("password", (None, str(self.password).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clearance = ClearanceEnum(d.pop("clearance"))

        gender = GenderEnum(d.pop("gender"))

        mentees = cast(list[int], d.pop("mentees"))

        username = d.pop("username")

        status = StatusEnum(d.pop("status"))

        def _parse_avatar(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                avatar_type_0 = File(payload=BytesIO(data))

                return avatar_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

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

        password = d.pop("password", UNSET)

        course_user_request = cls(
            clearance=clearance,
            gender=gender,
            mentees=mentees,
            username=username,
            status=status,
            avatar=avatar,
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
            password=password,
        )

        course_user_request.additional_properties = d
        return course_user_request

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
