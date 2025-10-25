from enum import Enum


class CourseExercisesCreateTagsErrorComponentCode(str, Enum):
    DOES_NOT_EXIST = "does_not_exist"
    INVALID = "invalid"
    NOT_A_LIST = "not_a_list"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
