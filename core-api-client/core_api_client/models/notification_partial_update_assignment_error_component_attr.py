from enum import Enum


class NotificationPartialUpdateAssignmentErrorComponentAttr(str, Enum):
    ASSIGNMENT = "assignment"

    def __str__(self) -> str:
        return str(self.value)
