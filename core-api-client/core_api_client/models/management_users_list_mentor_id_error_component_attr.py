from enum import Enum


class ManagementUsersListMentorIdErrorComponentAttr(str, Enum):
    MENTOR_ID = "mentor__id"

    def __str__(self) -> str:
        return str(self.value)
