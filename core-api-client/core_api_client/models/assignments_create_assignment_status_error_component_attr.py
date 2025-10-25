from enum import Enum


class AssignmentsCreateAssignmentStatusErrorComponentAttr(str, Enum):
    ASSIGNMENT_STATUS = "assignment_status"

    def __str__(self) -> str:
        return str(self.value)
