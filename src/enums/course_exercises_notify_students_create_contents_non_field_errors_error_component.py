from enum import Enum


class CourseExercisesNotifyStudentsCreateContentsNonFieldErrorsErrorComponentCode(str, Enum):
    NOT_A_LIST = "not_a_list"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
