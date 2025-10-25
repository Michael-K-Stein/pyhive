from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field
from src.types.common import UNSET, Unset

if TYPE_CHECKING:
    from client import HiveClient
    from src.types.module import Module
    from src.types.program import Program
    from src.types.subject import Subject
    from src.types.user import User

T = TypeVar("T", bound="Queue")


@_attrs_define
class Queue:
    """Queue model representing a student/program/module queue entry."""

    hive_client: "HiveClient"
    id: int
    name: str
    user_name: None | str
    subject_id: None | int
    subject_name: None | str
    subject_color: None | str
    subject_symbol: None | str
    module_name: None | str
    module_order: None | str
    program_id: int
    program_name: str
    description: None | Unset | str = UNSET

    module_id: None | Unset | int = UNSET
    user_id: None | Unset | int = UNSET

    _user: "User | None" = field(init=False, default=None)
    _module: "Module | None" = field(init=False, default=None)
    _subject: "Subject | None" = field(init=False, default=None)
    _program: "Program | None" = field(init=False, default=None)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "subject_id": self.subject_id,
            "subject_name": self.subject_name,
            "subject_color": self.subject_color,
            "subject_symbol": self.subject_symbol,
            "module_id": self.module_id,
            "module_name": self.module_name,
            "module_order": self.module_order,
            "program_id": self.program_id,
            "program_name": self.program_name,
            **({"description": self.description} if self.description is not UNSET else {}),
            **({"module": self.module} if self.module is not UNSET else {}),
            **({"user": self.user} if self.user_id is not UNSET else {}),
        }

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any], hive_client: "HiveClient") -> Self:
        d = dict(src_dict)

        def _optional(data: object) -> Any:
            return data if not isinstance(data, Unset) else UNSET

        return cls(
            hive_client=hive_client,
            id=d.pop("id"),
            name=d.pop("name"),
            user_id=cast("None | int", d.pop("user_id")),
            user_name=cast("None | str", d.pop("user_name")),
            subject_id=cast("None | int", d.pop("subject_id")),
            subject_name=cast("None | str", d.pop("subject_name")),
            subject_color=cast("None | str", d.pop("subject_color")),
            subject_symbol=cast("None | str", d.pop("subject_symbol")),
            module_id=cast("None | int", d.pop("module_id")),
            module_name=cast("None | str", d.pop("module_name")),
            module_order=cast("None | str", d.pop("module_order")),
            program_id=d.pop("program_id"),
            program_name=d.pop("program_name"),
            description=_optional(d.pop("description", UNSET)),
        )

    @property
    def user(self) -> "User | None":
        if self._user is None and isinstance(self.user_id, int):
            self._user = self.hive_client.get_user(self.user_id)
        return self._user

    @property
    def module(self) -> "Module | None":
        if self._module is None and isinstance(self.module_id, int):
            self._module = self.hive_client.get_module(self.module_id)
        return self._module

    @property
    def subject(self) -> "Subject | None":
        if isinstance(self.subject_id, int):
            return self.hive_client.get_subject(self.subject_id)
        return None

    @property
    def program(self) -> "Program":
        return self.hive_client.get_program(self.program_id)
