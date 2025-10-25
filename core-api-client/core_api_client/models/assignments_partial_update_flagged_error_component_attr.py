from enum import Enum


class AssignmentsPartialUpdateFlaggedErrorComponentAttr(str, Enum):
    FLAGGED = "flagged"

    def __str__(self) -> str:
        return str(self.value)
