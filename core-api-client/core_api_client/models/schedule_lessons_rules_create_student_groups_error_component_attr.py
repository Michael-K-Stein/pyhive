from enum import Enum


class ScheduleLessonsRulesCreateStudentGroupsErrorComponentAttr(str, Enum):
    STUDENT_GROUPS = "student_groups"

    def __str__(self) -> str:
        return str(self.value)
