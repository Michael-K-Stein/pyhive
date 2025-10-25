from enum import Enum


class NotificationListHelpInErrorComponentAttr(str, Enum):
    HELP_IN = "help__in"

    def __str__(self) -> str:
        return str(self.value)
