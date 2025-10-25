from enum import Enum


class CourseSubjectsUpdateNonFieldErrorsErrorComponentAttr(str, Enum):
    NON_FIELD_ERRORS = "non_field_errors"

    def __str__(self) -> str:
        return str(self.value)
