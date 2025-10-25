from enum import Enum


class CourseProgramsPartialUpdateCheckerErrorComponentAttr(str, Enum):
    CHECKER = "checker"

    def __str__(self) -> str:
        return str(self.value)
