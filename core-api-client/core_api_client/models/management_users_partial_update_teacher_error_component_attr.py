from enum import Enum


class ManagementUsersPartialUpdateTeacherErrorComponentAttr(str, Enum):
    TEACHER = "teacher"

    def __str__(self) -> str:
        return str(self.value)
