from enum import Enum


class ManagementUsersPartialUpdateMentorErrorComponentAttr(str, Enum):
    MENTOR = "mentor"

    def __str__(self) -> str:
        return str(self.value)
