from enum import Enum


class ManagementUsersMePartialUpdateCurrentAssignmentErrorComponentAttr(str, Enum):
    CURRENT_ASSIGNMENT = "current_assignment"

    def __str__(self) -> str:
        return str(self.value)
