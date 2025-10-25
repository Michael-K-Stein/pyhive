from enum import Enum


class CourseModulesUpdateNameErrorComponentAttr(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
