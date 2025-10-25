from enum import Enum


class ScheduleLessonsRulesUpdateStudentGroupsErrorComponentAttr(str, Enum):
    STUDENT_GROUPS = "student_groups"

    def __str__(self) -> str:
        return str(self.value)
