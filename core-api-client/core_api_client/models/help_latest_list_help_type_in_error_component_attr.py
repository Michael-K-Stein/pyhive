from enum import Enum


class HelpLatestListHelpTypeInErrorComponentAttr(str, Enum):
    HELP_TYPE_IN = "help_type__in"

    def __str__(self) -> str:
        return str(self.value)
