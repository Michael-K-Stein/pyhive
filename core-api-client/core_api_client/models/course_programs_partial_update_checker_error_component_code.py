from enum import Enum


class CourseProgramsPartialUpdateCheckerErrorComponentCode(str, Enum):
    DOES_NOT_EXIST = "does_not_exist"
    INCORRECT_TYPE = "incorrect_type"
    NULL = "null"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
