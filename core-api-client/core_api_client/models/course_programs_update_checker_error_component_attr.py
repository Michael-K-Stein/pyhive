from enum import Enum


class CourseProgramsUpdateCheckerErrorComponentAttr(str, Enum):
    CHECKER = "checker"

    def __str__(self) -> str:
        return str(self.value)
