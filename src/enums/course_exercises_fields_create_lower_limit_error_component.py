from enum import Enum


class CourseExercisesFieldsCreateLowerLimitErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_STRING_LENGTH = "max_string_length"
    MAX_VALUE = "max_value"
    MIN_VALUE = "min_value"

    def __str__(self) -> str:
        return str(self.value)
