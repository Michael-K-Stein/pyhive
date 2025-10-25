from enum import Enum


class ParseErrorCodeEnum(str, Enum):
    PARSE_ERROR = "parse_error"

    def __str__(self) -> str:
        return str(self.value)
