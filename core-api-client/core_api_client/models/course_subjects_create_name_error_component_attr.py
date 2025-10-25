from enum import Enum


class CourseSubjectsCreateNameErrorComponentAttr(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
