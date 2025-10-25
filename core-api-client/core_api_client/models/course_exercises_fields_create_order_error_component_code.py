from enum import Enum


class CourseExercisesFieldsCreateOrderErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_STRING_LENGTH = "max_string_length"
    MAX_VALUE = "max_value"
    MIN_VALUE = "min_value"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
