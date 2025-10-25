from enum import Enum


class CourseSubjectsPartialUpdateSymbolErrorComponentAttr(str, Enum):
    SYMBOL = "symbol"

    def __str__(self) -> str:
        return str(self.value)
