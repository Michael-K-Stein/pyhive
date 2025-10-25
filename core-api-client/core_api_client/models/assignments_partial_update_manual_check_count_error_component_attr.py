from enum import Enum


class AssignmentsPartialUpdateManualCheckCountErrorComponentAttr(str, Enum):
    MANUAL_CHECK_COUNT = "manual_check_count"

    def __str__(self) -> str:
        return str(self.value)
