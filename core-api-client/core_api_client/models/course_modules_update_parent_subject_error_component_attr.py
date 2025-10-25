from enum import Enum


class CourseModulesUpdateParentSubjectErrorComponentAttr(str, Enum):
    PARENT_SUBJECT = "parent_subject"

    def __str__(self) -> str:
        return str(self.value)
