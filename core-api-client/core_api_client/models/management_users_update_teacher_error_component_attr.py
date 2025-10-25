from enum import Enum


class ManagementUsersUpdateTeacherErrorComponentAttr(str, Enum):
    TEACHER = "teacher"

    def __str__(self) -> str:
        return str(self.value)
