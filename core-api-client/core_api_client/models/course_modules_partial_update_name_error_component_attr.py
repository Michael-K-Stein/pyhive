from enum import Enum


class CourseModulesPartialUpdateNameErrorComponentAttr(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
