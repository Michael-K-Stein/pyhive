from enum import Enum


class HelpLatestListUserMentorIdErrorComponentAttr(str, Enum):
    USER_MENTOR_ID = "user__mentor__id"

    def __str__(self) -> str:
        return str(self.value)
