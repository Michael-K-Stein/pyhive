from enum import Enum


class CourseSubjectsListParentProgramIdInErrorComponentAttr(str, Enum):
    PARENT_PROGRAM_ID_IN = "parent_program__id__in"

    def __str__(self) -> str:
        return str(self.value)
