from enum import Enum


class NotificationListAssignmentErrorComponentAttr(str, Enum):
    ASSIGNMENT = "assignment"

    def __str__(self) -> str:
        return str(self.value)
