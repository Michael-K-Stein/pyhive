from enum import Enum


class ManagementUsersCreateTeacherErrorComponentAttr(str, Enum):
    TEACHER = "teacher"

    def __str__(self) -> str:
        return str(self.value)
