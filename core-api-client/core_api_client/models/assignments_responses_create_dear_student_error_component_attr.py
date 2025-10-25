from enum import Enum


class AssignmentsResponsesCreateDearStudentErrorComponentAttr(str, Enum):
    DEAR_STUDENT = "dear_student"

    def __str__(self) -> str:
        return str(self.value)
