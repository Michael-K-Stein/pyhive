from enum import Enum


class AssignmentsUpdateStudentAssignmentStatusErrorComponentAttr(str, Enum):
    STUDENT_ASSIGNMENT_STATUS = "student_assignment_status"

    def __str__(self) -> str:
        return str(self.value)
