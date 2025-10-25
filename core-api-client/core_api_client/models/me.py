from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.me_clearance_enum import MeClearanceEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignment_option_hanich import AssignmentOptionHanich


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        id (int):
        only_today (bool):
        display_name (str):
        number (Union[None, int]):
        program (Union[None, int]):
        clearance (MeClearanceEnum):
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
        current_assignment_options (list['AssignmentOptionHanich']):
        current_assignment_exercise_name (str):
        current_assignment_exercise_id (int):
        current_assignment_module_id (int):
        current_assignment_subject_id (int):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        program_name (str):
        schedule_enabled (bool):
        hanich_raise_hand (bool):
        teacher (bool):
        current_assignment (Union[None, Unset, int]):
        confirmed (Union[Unset, bool]):
    """

    id: int
    only_today: bool
    display_name: str
    number: Union[None, int]
    program: Union[None, int]
    clearance: MeClearanceEnum
    status: StatusEnum
    current_assignment_options: list["AssignmentOptionHanich"]
    current_assignment_exercise_name: str
    current_assignment_exercise_id: int
    current_assignment_module_id: int
    current_assignment_subject_id: int
    username: str
    program_name: str
    schedule_enabled: bool
    hanich_raise_hand: bool
    teacher: bool
    current_assignment: Union[None, Unset, int] = UNSET
    confirmed: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        only_today = self.only_today

        display_name = self.display_name

        number: Union[None, int]
        number = self.number

        program: Union[None, int]
        program = self.program

        clearance = self.clearance.value

        status = self.status.value

        current_assignment_options = []
        for current_assignment_options_item_data in self.current_assignment_options:
            current_assignment_options_item = current_assignment_options_item_data.to_dict()
            current_assignment_options.append(current_assignment_options_item)

        current_assignment_exercise_name = self.current_assignment_exercise_name

        current_assignment_exercise_id = self.current_assignment_exercise_id

        current_assignment_module_id = self.current_assignment_module_id

        current_assignment_subject_id = self.current_assignment_subject_id

        username = self.username

        program_name = self.program_name

        schedule_enabled = self.schedule_enabled

        hanich_raise_hand = self.hanich_raise_hand

        teacher = self.teacher

        current_assignment: Union[None, Unset, int]
        if isinstance(self.current_assignment, Unset):
            current_assignment = UNSET
        else:
            current_assignment = self.current_assignment

        confirmed = self.confirmed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "only_today": only_today,
                "display_name": display_name,
                "number": number,
                "program": program,
                "clearance": clearance,
                "status": status,
                "current_assignment_options": current_assignment_options,
                "current_assignment__exercise_name": current_assignment_exercise_name,
                "current_assignment__exercise_id": current_assignment_exercise_id,
                "current_assignment__module_id": current_assignment_module_id,
                "current_assignment__subject_id": current_assignment_subject_id,
                "username": username,
                "program__name": program_name,
                "schedule_enabled": schedule_enabled,
                "hanich_raise_hand": hanich_raise_hand,
                "teacher": teacher,
            }
        )
        if current_assignment is not UNSET:
            field_dict["current_assignment"] = current_assignment
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignment_option_hanich import AssignmentOptionHanich

        d = dict(src_dict)
        id = d.pop("id")

        only_today = d.pop("only_today")

        display_name = d.pop("display_name")

        def _parse_number(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        number = _parse_number(d.pop("number"))

        def _parse_program(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        program = _parse_program(d.pop("program"))

        clearance = MeClearanceEnum(d.pop("clearance"))

        status = StatusEnum(d.pop("status"))

        current_assignment_options = []
        _current_assignment_options = d.pop("current_assignment_options")
        for current_assignment_options_item_data in _current_assignment_options:
            current_assignment_options_item = AssignmentOptionHanich.from_dict(current_assignment_options_item_data)

            current_assignment_options.append(current_assignment_options_item)

        current_assignment_exercise_name = d.pop("current_assignment__exercise_name")

        current_assignment_exercise_id = d.pop("current_assignment__exercise_id")

        current_assignment_module_id = d.pop("current_assignment__module_id")

        current_assignment_subject_id = d.pop("current_assignment__subject_id")

        username = d.pop("username")

        program_name = d.pop("program__name")

        schedule_enabled = d.pop("schedule_enabled")

        hanich_raise_hand = d.pop("hanich_raise_hand")

        teacher = d.pop("teacher")

        def _parse_current_assignment(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        current_assignment = _parse_current_assignment(d.pop("current_assignment", UNSET))

        confirmed = d.pop("confirmed", UNSET)

        me = cls(
            id=id,
            only_today=only_today,
            display_name=display_name,
            number=number,
            program=program,
            clearance=clearance,
            status=status,
            current_assignment_options=current_assignment_options,
            current_assignment_exercise_name=current_assignment_exercise_name,
            current_assignment_exercise_id=current_assignment_exercise_id,
            current_assignment_module_id=current_assignment_module_id,
            current_assignment_subject_id=current_assignment_subject_id,
            username=username,
            program_name=program_name,
            schedule_enabled=schedule_enabled,
            hanich_raise_hand=hanich_raise_hand,
            teacher=teacher,
            current_assignment=current_assignment,
            confirmed=confirmed,
        )

        me.additional_properties = d
        return me

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
