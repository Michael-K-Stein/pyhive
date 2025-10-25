from enum import Enum


class AssignmentsCreateTotalCheckCountErrorComponentAttr(str, Enum):
    TOTAL_CHECK_COUNT = "total_check_count"

    def __str__(self) -> str:
        return str(self.value)
