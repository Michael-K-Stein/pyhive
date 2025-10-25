import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.help_type_enum import HelpTypeEnum
from ..models.notification_response_type_enum import NotificationResponseTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """
    Attributes:
        id (int):
        response_type (Union[None, NotificationResponseTypeEnum]):
        exercise (Union[None, int]):
        exercise_name (Union[None, str]):
        module (Union[None, int]):
        subject (Union[None, int]):
        program (Union[None, int]):
        help_type (Union[HelpTypeEnum, None]):
        help_title (Union[None, str]):
        from_user (Union[None, int]):
        from_user_name (str):
        time (datetime.datetime):
        for_user (int):
        for_user_name (str):
        help_ (Union[None, Unset, int]):
        assignment (Union[None, Unset, int]):
        comment (Union[Unset, str]):
        was_read (Union[Unset, bool]):
    """

    id: int
    response_type: Union[None, NotificationResponseTypeEnum]
    exercise: Union[None, int]
    exercise_name: Union[None, str]
    module: Union[None, int]
    subject: Union[None, int]
    program: Union[None, int]
    help_type: Union[HelpTypeEnum, None]
    help_title: Union[None, str]
    from_user: Union[None, int]
    from_user_name: str
    time: datetime.datetime
    for_user: int
    for_user_name: str
    help_: Union[None, Unset, int] = UNSET
    assignment: Union[None, Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    was_read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        response_type: Union[None, str]
        if isinstance(self.response_type, NotificationResponseTypeEnum):
            response_type = self.response_type.value
        else:
            response_type = self.response_type

        exercise: Union[None, int]
        exercise = self.exercise

        exercise_name: Union[None, str]
        exercise_name = self.exercise_name

        module: Union[None, int]
        module = self.module

        subject: Union[None, int]
        subject = self.subject

        program: Union[None, int]
        program = self.program

        help_type: Union[None, str]
        if isinstance(self.help_type, HelpTypeEnum):
            help_type = self.help_type.value
        else:
            help_type = self.help_type

        help_title: Union[None, str]
        help_title = self.help_title

        from_user: Union[None, int]
        from_user = self.from_user

        from_user_name = self.from_user_name

        time = self.time.isoformat()

        for_user = self.for_user

        for_user_name = self.for_user_name

        help_: Union[None, Unset, int]
        if isinstance(self.help_, Unset):
            help_ = UNSET
        else:
            help_ = self.help_

        assignment: Union[None, Unset, int]
        if isinstance(self.assignment, Unset):
            assignment = UNSET
        else:
            assignment = self.assignment

        comment = self.comment

        was_read = self.was_read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "response_type": response_type,
                "exercise": exercise,
                "exercise_name": exercise_name,
                "module": module,
                "subject": subject,
                "program": program,
                "help_type": help_type,
                "help_title": help_title,
                "from_user": from_user,
                "from_user_name": from_user_name,
                "time": time,
                "for_user": for_user,
                "for_user_name": for_user_name,
            }
        )
        if help_ is not UNSET:
            field_dict["help"] = help_
        if assignment is not UNSET:
            field_dict["assignment"] = assignment
        if comment is not UNSET:
            field_dict["comment"] = comment
        if was_read is not UNSET:
            field_dict["was_read"] = was_read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_response_type(data: object) -> Union[None, NotificationResponseTypeEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                response_type_type_0 = NotificationResponseTypeEnum(data)

                return response_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, NotificationResponseTypeEnum], data)

        response_type = _parse_response_type(d.pop("response_type"))

        def _parse_exercise(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        exercise = _parse_exercise(d.pop("exercise"))

        def _parse_exercise_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        exercise_name = _parse_exercise_name(d.pop("exercise_name"))

        def _parse_module(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        module = _parse_module(d.pop("module"))

        def _parse_subject(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_program(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        program = _parse_program(d.pop("program"))

        def _parse_help_type(data: object) -> Union[HelpTypeEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                help_type_type_1 = HelpTypeEnum(data)

                return help_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[HelpTypeEnum, None], data)

        help_type = _parse_help_type(d.pop("help_type"))

        def _parse_help_title(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        help_title = _parse_help_title(d.pop("help_title"))

        def _parse_from_user(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        from_user = _parse_from_user(d.pop("from_user"))

        from_user_name = d.pop("from_user_name")

        time = isoparse(d.pop("time"))

        for_user = d.pop("for_user")

        for_user_name = d.pop("for_user_name")

        def _parse_help_(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        help_ = _parse_help_(d.pop("help", UNSET))

        def _parse_assignment(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assignment = _parse_assignment(d.pop("assignment", UNSET))

        comment = d.pop("comment", UNSET)

        was_read = d.pop("was_read", UNSET)

        notification = cls(
            id=id,
            response_type=response_type,
            exercise=exercise,
            exercise_name=exercise_name,
            module=module,
            subject=subject,
            program=program,
            help_type=help_type,
            help_title=help_title,
            from_user=from_user,
            from_user_name=from_user_name,
            time=time,
            for_user=for_user,
            for_user_name=for_user_name,
            help_=help_,
            assignment=assignment,
            comment=comment,
            was_read=was_read,
        )

        notification.additional_properties = d
        return notification

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
