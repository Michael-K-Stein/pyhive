from enum import Enum


class ValidationErrorEnum(str, Enum):
    VALIDATION_ERROR = "validation_error"

    def __str__(self) -> str:
        return str(self.value)
