"""Defines the Subject type and related functionality for the Hive API Python bindings."""

from collections.abc import Generator, Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define, field
from src.types.core_item import HiveCoreItem
from src.types.enums.sync_status_enum import SyncStatusEnum

if TYPE_CHECKING:
    from client import HiveClient
    from src.types.module import Module
    from src.types.program import Program

T = TypeVar("T", bound="Subject")


@define
class Subject(HiveCoreItem):
    """Represents a Subject in the Hive system.

    Attributes:
        hive_client (HiveClient): Reference to the Hive API client.
        id (int): Subject ID.
        symbol (str): Subject symbol.
        parent_program_id (int): ID of the parent Program.
        color (str): Subject color (hex code or name).
        name (str): Display name.
        parent_program_name (str): Name of the parent Program.
        sync_status (SyncStatusEnum): Status of subject synchronization.
        sync_message (str | None): Optional sync error or status message.
        segel_path (str): Staff-accessible path on shared drive.

    """

    hive_client: "HiveClient"
    id: int
    symbol: str
    parent_program_id: int
    color: str
    name: str
    parent_program_name: str
    sync_status: SyncStatusEnum
    sync_message: str | None
    segel_path: str
    _parent_program: "Program | None" = field(init=False, default=None)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the Subject to a dictionary."""
        return {
            "id": self.id,
            "symbol": self.symbol,
            "parent_program": self.parent_program_id,
            "color": self.color,
            "name": self.name,
            "parent_program_name": self.parent_program_name,
            "sync_status": self.sync_status.value,
            "sync_message": self.sync_message,
            "segel_path": self.segel_path,
        }

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any], hive_client: "HiveClient") -> Self:
        """Deserialize a Subject from a dictionary.

        Args:
            src_dict: A dictionary containing Subject data.
            hive_client: An instance of HiveClient.

        Returns:
            A Subject instance.

        """
        return cls(
            hive_client=hive_client,
            id=src_dict["id"],
            symbol=src_dict["symbol"],
            parent_program_id=src_dict["parent_program"],
            color=src_dict["color"],
            name=src_dict["name"],
            parent_program_name=src_dict["parent_program_name"],
            sync_status=SyncStatusEnum(src_dict["sync_status"]),
            sync_message=cast("str | None", src_dict.get("sync_message")),
            segel_path=src_dict["segel_path"],
        )

    @property
    def parent_program(self) -> "Program":
        """Lazily load and return the parent Program.

        Returns:
            Program: The parent program instance.

        """
        if self._parent_program is None:
            self._parent_program = self.hive_client.get_program(self.parent_program_id)
        return self._parent_program

    def get_modules(self) -> Generator["Module"]:
        """Retrieve all modules associated with this subject.

        Returns:
            Generator[Module]: Generator of Module instances.

        """
        return self.hive_client.get_course_modules(parent_subject__id=self.id)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Subject):
            return False
        return self.id == value.id and self.parent_program == value.parent_program

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Subject):
            return NotImplemented
        return self.symbol < value.symbol
