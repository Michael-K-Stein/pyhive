from enum import Enum


class NotificationListHelpErrorComponentCode(str, Enum):
    INVALID_CHOICE = "invalid_choice"

    def __str__(self) -> str:
        return str(self.value)
