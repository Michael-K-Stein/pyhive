from enum import Enum


class AssignmentsPartialUpdateAssignmentStatusErrorComponentAttr(str, Enum):
    ASSIGNMENT_STATUS = "assignment_status"

    def __str__(self) -> str:
        return str(self.value)
