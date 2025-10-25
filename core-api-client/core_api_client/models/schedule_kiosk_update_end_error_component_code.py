from enum import Enum


class ScheduleKioskUpdateEndErrorComponentCode(str, Enum):
    DATE = "date"
    INVALID = "invalid"
    MAKE_AWARE = "make_aware"
    NULL = "null"
    OVERFLOW = "overflow"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
