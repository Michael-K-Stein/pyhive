from enum import Enum


class CourseSubjectsUpdateParentProgramErrorComponentAttr(str, Enum):
    PARENT_PROGRAM = "parent_program"

    def __str__(self) -> str:
        return str(self.value)
