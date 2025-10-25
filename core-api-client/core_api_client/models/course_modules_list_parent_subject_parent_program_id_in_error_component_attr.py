from enum import Enum


class CourseModulesListParentSubjectParentProgramIdInErrorComponentAttr(str, Enum):
    PARENT_SUBJECT_PARENT_PROGRAM_ID_IN = "parent_subject__parent_program__id__in"

    def __str__(self) -> str:
        return str(self.value)
