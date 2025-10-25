from enum import Enum


class PatbasEnum(str, Enum):
    ALWAYS = "Always"
    NEVER = "Never"
    ON_DONE = "On Done"
    STAFF_ONLY = "Staff Only"

    def __str__(self) -> str:
        return str(self.value)
