from enum import Enum


class CourseModulesCreateOrderErrorComponentAttr(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
