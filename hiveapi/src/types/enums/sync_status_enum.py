from enum import Enum


class SyncStatusEnum(str, Enum):
    CREATING = "Creating"
    DELETING = "Deleting"
    ERROR = "Error"
    NORMAL = "Normal"

    def __str__(self) -> str:
        return str(self.value)
