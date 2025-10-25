from enum import Enum


class HelpUpdateHelpTypeErrorComponentAttr(str, Enum):
    HELP_TYPE = "help_type"

    def __str__(self) -> str:
        return str(self.value)
