from enum import Enum


class ManagementClassesListTypeErrorComponentCode(str, Enum):
    INVALID_CHOICE = "invalid_choice"

    def __str__(self) -> str:
        return str(self.value)
