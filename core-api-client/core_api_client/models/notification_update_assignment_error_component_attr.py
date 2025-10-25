from enum import Enum


class NotificationUpdateAssignmentErrorComponentAttr(str, Enum):
    ASSIGNMENT = "assignment"

    def __str__(self) -> str:
        return str(self.value)
