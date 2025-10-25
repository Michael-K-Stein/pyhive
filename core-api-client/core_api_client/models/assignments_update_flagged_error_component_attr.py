from enum import Enum


class AssignmentsUpdateFlaggedErrorComponentAttr(str, Enum):
    FLAGGED = "flagged"

    def __str__(self) -> str:
        return str(self.value)
