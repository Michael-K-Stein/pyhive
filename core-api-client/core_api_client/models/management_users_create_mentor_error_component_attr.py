from enum import Enum


class ManagementUsersCreateMentorErrorComponentAttr(str, Enum):
    MENTOR = "mentor"

    def __str__(self) -> str:
        return str(self.value)
