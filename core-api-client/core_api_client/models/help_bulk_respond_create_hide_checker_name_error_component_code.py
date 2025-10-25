from enum import Enum


class HelpBulkRespondCreateHideCheckerNameErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
