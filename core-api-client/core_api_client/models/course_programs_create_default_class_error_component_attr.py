from enum import Enum


class CourseProgramsCreateDefaultClassErrorComponentAttr(str, Enum):
    DEFAULT_CLASS = "default_class"

    def __str__(self) -> str:
        return str(self.value)
