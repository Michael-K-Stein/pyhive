"""Module model definition for the Hive system.

Represents a logical course module within a subject, supporting serialization,
lazy loading of parent subject, and retrieval of exercises.
"""

from collections.abc import Generator, Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field
from .enums.sync_status_enum import SyncStatusEnum
from .exercise import Exercise
from .program import HiveCoreItem

if TYPE_CHECKING:
    from ...client import HiveClient
    from .subject import Subject

T = TypeVar("T", bound="Module")


@_attrs_define
class Module(HiveCoreItem):
    """Course Subject Module.

    Attributes:
        id: Unique identifier.
        name: Name of the module.
        parent_subject_id: ID of the parent subject.
        order: Order of display within the subject.
        sync_status: Synchronization status.
        sync_message: Optional error or status message.
        parent_program_name: Name of the program the subject belongs to.
        parent_subject_name: Name of the parent subject.
        parent_subject_symbol: Symbol of the parent subject.
        segel_path: Network path accessible to staff.

    """

    hive_client: "HiveClient"
    id: int
    name: str
    parent_subject_id: int
    order: str
    sync_status: SyncStatusEnum
    sync_message: None | str
    parent_program_name: str
    parent_subject_name: str
    parent_subject_symbol: str
    segel_path: str

    _parent_subject: "Subject | None" = field(init=False, default=None)

    @property
    def parent_subject(self) -> "Subject":
        """Lazily load and return the parent subject."""
        if self._parent_subject is None:
            self._parent_subject = self.hive_client.get_subject(self.parent_subject_id)
        return self._parent_subject

    def get_exercises(self) -> Generator[Exercise]:
        """Fetch all exercises within this module."""
        return self.hive_client.get_exercises(parent_module__id=self.id)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the module to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "parent_subject": self.parent_subject_id,
            "order": self.order,
            "sync_status": self.sync_status.value,
            "sync_message": self.sync_message,
            "parent_program_name": self.parent_program_name,
            "parent_subject_name": self.parent_subject_name,
            "parent_subject_symbol": self.parent_subject_symbol,
            "segel_path": self.segel_path,
        }

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any], hive_client: "HiveClient") -> Self:
        """Deserialize a module from a dictionary."""
        d = dict(src_dict)
        return cls(
            hive_client=hive_client,
            id=d["id"],
            name=d["name"],
            parent_subject_id=d["parent_subject"],
            order=d["order"],
            sync_status=SyncStatusEnum(d["sync_status"]),
            sync_message=cast("None | str", d["sync_message"]),
            parent_program_name=d["parent_program_name"],
            parent_subject_name=d["parent_subject_name"],
            parent_subject_symbol=d["parent_subject_symbol"],
            segel_path=d["segel_path"],
        )

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Module):
            return False
        return self.id == value.id and self.parent_subject == value.parent_subject

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Module):
            return NotImplemented
        return self.order < value.order
