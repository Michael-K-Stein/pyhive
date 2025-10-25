from enum import Enum


class CourseSubjectsCreateParentProgramErrorComponentAttr(str, Enum):
    PARENT_PROGRAM = "parent_program"

    def __str__(self) -> str:
        return str(self.value)
