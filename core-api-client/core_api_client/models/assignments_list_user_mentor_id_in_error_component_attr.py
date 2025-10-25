from enum import Enum


class AssignmentsListUserMentorIdInErrorComponentAttr(str, Enum):
    USER_MENTOR_ID_IN = "user__mentor__id__in"

    def __str__(self) -> str:
        return str(self.value)
