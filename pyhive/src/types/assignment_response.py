import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast, Generator

from attrs import define, field
from dateutil.parser import isoparse

from .autocheck_status import AutoCheckStatus
from .assignment import Assignment
from .enums.assignment_response_type_enum import AssignmentResponseTypeEnum
from .common import UNSET, Unset

if TYPE_CHECKING:
    from .user import User
    from .assignment_response_content import AssignmentResponseContent
    from .autocheck_status import AutoCheckStatus
    from .assignment import Assignment
    from ...client import HiveClient


T = TypeVar("T", bound="AssignmentResponse")


@define
class AssignmentResponse:
    """
    Attributes:
        id (int):
        user_id (int):
        contents (list['AssignmentResponseContent']):
        date (datetime.datetime):
        response_type (AssignmentResponseTypeEnum):
            * `Comment` - Comment
            * `Work In Progress` - Workinprogress
            * `Submission` - Submission
            * `AutoCheck` - Autocheck
            * `Redo` - Redo
            * `Done` - Done
        autocheck_statuses (Union[None, list['Status']]):
        file_name (Union[Unset, str]):
        dear_student (Union[Unset, bool]):  Default: True.
        hide_checker_name (Union[Unset, bool]):
        segel_only (Union[Unset, bool]):
    """

    hive_client: "HiveClient"
    assignment_id: int
    id: int
    user_id: int
    contents: list["AssignmentResponseContent"]
    date: datetime.datetime
    response_type: AssignmentResponseTypeEnum
    autocheck_statuses: Union[None, list["AutoCheckStatus"]]
    file_name: Union[Unset, str] = UNSET
    dear_student: Union[Unset, bool] = True
    hide_checker_name: Union[Unset, bool] = UNSET
    segel_only: Union[Unset, bool] = UNSET

    # Lazy-loaded objects
    _user: "User | None" = field(init=False, default=None)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user

        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()
            contents.append(contents_item)

        date = self.date.isoformat()

        response_type = self.response_type.value

        autocheck_statuses: Union[None, list[dict[str, Any]]]
        if isinstance(self.autocheck_statuses, list):
            autocheck_statuses = []
            for autocheck_statuses_type_0_item_data in self.autocheck_statuses:
                autocheck_statuses_type_0_item = (
                    autocheck_statuses_type_0_item_data.to_dict()
                )
                autocheck_statuses.append(autocheck_statuses_type_0_item)

        else:
            autocheck_statuses = self.autocheck_statuses

        file_name = self.file_name

        dear_student = self.dear_student

        hide_checker_name = self.hide_checker_name

        segel_only = self.segel_only

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "user": user,
                "contents": contents,
                "date": date,
                "response_type": response_type,
                "autocheck_statuses": autocheck_statuses,
            }
        )
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if dear_student is not UNSET:
            field_dict["dear_student"] = dear_student
        if hide_checker_name is not UNSET:
            field_dict["hide_checker_name"] = hide_checker_name
        if segel_only is not UNSET:
            field_dict["segel_only"] = segel_only

        return field_dict

    @classmethod
    def from_dict(
        cls: type[T],
        src_dict: dict[str, Any],
        assignment_id: int,
        hive_client: "HiveClient",
    ) -> T:
        from .assignment_response_content import AssignmentResponseContent
        from .autocheck_status import AutoCheckStatus

        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user")

        contents = []
        _contents = d.pop("contents")
        if not isinstance(_contents, list):
            raise TypeError(
                f"Assignment response contents must be a list, not {type(_contents)}"
            )
        for contents_item_data in _contents:
            contents_item = AssignmentResponseContent.from_dict(
                contents_item_data,
                assignment_id=assignment_id,
                assignment_response_id=id,
                hive_client=hive_client,
            )
            contents.append(contents_item)
        date = isoparse(d.pop("date"))
        response_type = AssignmentResponseTypeEnum(d.pop("response_type"))

        def _parse_autocheck_statuses(
            data: object,
        ) -> Union[None, list["AutoCheckStatus"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                autocheck_statuses_type_0 = []
                _autocheck_statuses_type_0 = data
                for autocheck_statuses_type_0_item_data in _autocheck_statuses_type_0:
                    autocheck_statuses_type_0_item = AutoCheckStatus.from_dict(
                        autocheck_statuses_type_0_item_data
                    )

                    autocheck_statuses_type_0.append(autocheck_statuses_type_0_item)

                return autocheck_statuses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["AutoCheckStatus"]], data)

        autocheck_statuses = _parse_autocheck_statuses(d.pop("autocheck_statuses"))

        file_name = d.pop("file_name", UNSET)

        dear_student = d.pop("dear_student", UNSET)

        hide_checker_name = d.pop("hide_checker_name", UNSET)

        segel_only = d.pop("segel_only", UNSET)

        return cls(
            hive_client=hive_client,
            assignment_id=assignment_id,
            id=id,
            user_id=user_id,
            contents=contents,
            date=date,
            response_type=response_type,
            autocheck_statuses=autocheck_statuses,
            file_name=file_name,
            dear_student=dear_student,
            hide_checker_name=hide_checker_name,
            segel_only=segel_only,
        )

    @property
    def user(self) -> "User":
        """Lazily load and return the user this assignment belongs to."""
        if self._user is None:
            self._user = self.hive_client.get_user(self.user_id)
        return self._user

    @property
    def assignment(self) -> "Assignment":
        if self._assignment is None:
            self._assignment = self.hive_client.get_assignment(
                assignment_id=self.assignment_id
            )
        return self._assignment

    def __iter__(self) -> Generator["AssignmentResponseContent", None, None]:
        """Allow iteration over this AssignmentResponse to yield its contents."""
        yield from self.contents
