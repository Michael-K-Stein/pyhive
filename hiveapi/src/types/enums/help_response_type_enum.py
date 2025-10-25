from enum import Enum


class HelpResponseTypeEnum(str, Enum):
    COMMENT = "Comment"
    OPEN = "Open"
    RESOLVE = "Resolve"

    def __str__(self) -> str:
        return str(self.value)
