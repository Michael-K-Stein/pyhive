from enum import Enum


class CourseExercisesFieldsPartialUpdateChoicesINDEXErrorComponentCode(str, Enum):
    INVALID = "invalid"
    MAX_LENGTH = "max_length"
    NULL = "null"
    NULL_CHARACTERS_NOT_ALLOWED = "null_characters_not_allowed"
    SURROGATE_CHARACTERS_NOT_ALLOWED = "surrogate_characters_not_allowed"

    def __str__(self) -> str:
        return str(self.value)
