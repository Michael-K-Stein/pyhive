from enum import Enum


class AssignmentsCreateFlaggedErrorComponentAttr(str, Enum):
    FLAGGED = "flagged"

    def __str__(self) -> str:
        return str(self.value)
