from enum import Enum


class ManagementSeatingListClassroomIdErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_VALUE = "max_value"

    def __str__(self) -> str:
        return str(self.value)
