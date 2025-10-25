from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.help_status_enum import HelpStatusEnum
from ..models.help_type_enum import HelpTypeEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise import Exercise
    from ..models.help_response_segel_nested import HelpResponseSegelNested
    from ..models.notification_nested import NotificationNested


T = TypeVar("T", bound="Help")


@_attrs_define
class Help:
    """
    Attributes:
        id (int):
        user (int):
        checker (Union[None, int]):
        checker_first_name (str):
        checker_last_name (str):
        is_subscribed (bool):
        help_type (HelpTypeEnum):
            * `Exercise` - Exercise
            * `Medical` - Medical
            * `Error` - Error
            * `Music` - Music
            * `Request` - Request
            * `Other` - Other
            * `Chat` - Chat
        help_status (HelpStatusEnum):
            * `Resolved` - Resolved
            * `Open` - Open
        for_exercise (Union['Exercise', None]):
        responses (list['HelpResponseSegelNested']):
        notifications (list['NotificationNested']):
        title (Union[Unset, str]):
        visibility (Union[Unset, VisibilityEnum]): * `All Staff` - Allstaff
            * `All Staff And Checkers` - Allstaffandcheckers
            * `Author Only` - Authoronly
    """

    id: int
    user: int
    checker: Union[None, int]
    checker_first_name: str
    checker_last_name: str
    is_subscribed: bool
    help_type: HelpTypeEnum
    help_status: HelpStatusEnum
    for_exercise: Union["Exercise", None]
    responses: list["HelpResponseSegelNested"]
    notifications: list["NotificationNested"]
    title: Union[Unset, str] = UNSET
    visibility: Union[Unset, VisibilityEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exercise import Exercise

        id = self.id

        user = self.user

        checker: Union[None, int]
        checker = self.checker

        checker_first_name = self.checker_first_name

        checker_last_name = self.checker_last_name

        is_subscribed = self.is_subscribed

        help_type = self.help_type.value

        help_status = self.help_status.value

        for_exercise: Union[None, dict[str, Any]]
        if isinstance(self.for_exercise, Exercise):
            for_exercise = self.for_exercise.to_dict()
        else:
            for_exercise = self.for_exercise

        responses = []
        for responses_item_data in self.responses:
            responses_item = responses_item_data.to_dict()
            responses.append(responses_item)

        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)

        title = self.title

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

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
                "help_type": help_type,
                "help_status": help_status,
                "for_exercise": for_exercise,
                "responses": responses,
                "notifications": notifications,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise import Exercise
        from ..models.help_response_segel_nested import HelpResponseSegelNested
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

        help_type = HelpTypeEnum(d.pop("help_type"))

        help_status = HelpStatusEnum(d.pop("help_status"))

        def _parse_for_exercise(data: object) -> Union["Exercise", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                for_exercise_type_1 = Exercise.from_dict(data)

                return for_exercise_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Exercise", None], data)

        for_exercise = _parse_for_exercise(d.pop("for_exercise"))

        responses = []
        _responses = d.pop("responses")
        for responses_item_data in _responses:
            responses_item = HelpResponseSegelNested.from_dict(responses_item_data)

            responses.append(responses_item)

        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in _notifications:
            notifications_item = NotificationNested.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, VisibilityEnum]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = VisibilityEnum(_visibility)

        help_ = cls(
            id=id,
            user=user,
            checker=checker,
            checker_first_name=checker_first_name,
            checker_last_name=checker_last_name,
            is_subscribed=is_subscribed,
            help_type=help_type,
            help_status=help_status,
            for_exercise=for_exercise,
            responses=responses,
            notifications=notifications,
            title=title,
            visibility=visibility,
        )

        help_.additional_properties = d
        return help_

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
