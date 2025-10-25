from enum import Enum


class NotificationListHelpErrorComponentAttr(str, Enum):
    HELP = "help"

    def __str__(self) -> str:
        return str(self.value)
