from enum import Enum


class CourseSubjectsCreateNameErrorComponentCode(str, Enum):
    BLANK = "blank"
    INVALID = "invalid"
    MAX_LENGTH = "max_length"
    NULL = "null"
    NULL_CHARACTERS_NOT_ALLOWED = "null_characters_not_allowed"
    REQUIRED = "required"
    SURROGATE_CHARACTERS_NOT_ALLOWED = "surrogate_characters_not_allowed"
    UNIQUE = "unique"

    def __str__(self) -> str:
        return str(self.value)
