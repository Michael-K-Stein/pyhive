from enum import Enum


class NotificationPartialUpdateHelpErrorComponentAttr(str, Enum):
    HELP = "help"

    def __str__(self) -> str:
        return str(self.value)
