from enum import Enum


class NotificationCreateAssignmentErrorComponentAttr(str, Enum):
    ASSIGNMENT = "assignment"

    def __str__(self) -> str:
        return str(self.value)
