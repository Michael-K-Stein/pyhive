from enum import Enum


class EventTypeEnum(str, Enum):
    הרצאה = "הרצאה"
    עע = "עע"
    פתבס = "פתבס"

    def __str__(self) -> str:
        return str(self.value)
