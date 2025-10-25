from enum import Enum


class CourseExercisesFieldsUpdateStaffResponsesErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
