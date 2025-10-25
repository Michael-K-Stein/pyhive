from enum import Enum


class CourseSubjectsPartialUpdateColorErrorComponentAttr(str, Enum):
    COLOR = "color"

    def __str__(self) -> str:
        return str(self.value)
