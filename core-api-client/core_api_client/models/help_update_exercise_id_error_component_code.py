from enum import Enum


class HelpUpdateExerciseIdErrorComponentCode(str, Enum):
    DOES_NOT_EXIST = "does_not_exist"
    INCORRECT_TYPE = "incorrect_type"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
