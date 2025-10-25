from enum import Enum


class CourseModulesListParentSubjectIdErrorComponentAttr(str, Enum):
    PARENT_SUBJECT_ID = "parent_subject__id"

    def __str__(self) -> str:
        return str(self.value)
