from enum import Enum


class CourseSubjectsCreateSymbolErrorComponentAttr(str, Enum):
    SYMBOL = "symbol"

    def __str__(self) -> str:
        return str(self.value)
