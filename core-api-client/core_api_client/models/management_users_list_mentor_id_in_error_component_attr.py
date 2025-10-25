from enum import Enum


class ManagementUsersListMentorIdInErrorComponentAttr(str, Enum):
    MENTOR_ID_IN = "mentor__id__in"

    def __str__(self) -> str:
        return str(self.value)
