from enum import Enum


class VisibilityEnum(str, Enum):
    ALL_STAFF = "All Staff"
    ALL_STAFF_AND_CHECKERS = "All Staff And Checkers"
    AUTHOR_ONLY = "Author Only"

    def __str__(self) -> str:
        return str(self.value)
