from enum import Enum


class HelpListHelpStatusInErrorComponentAttr(str, Enum):
    HELP_STATUS_IN = "help_status__in"

    def __str__(self) -> str:
        return str(self.value)
