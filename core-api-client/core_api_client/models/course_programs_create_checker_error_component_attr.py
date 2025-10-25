from enum import Enum


class CourseProgramsCreateCheckerErrorComponentAttr(str, Enum):
    CHECKER = "checker"

    def __str__(self) -> str:
        return str(self.value)
