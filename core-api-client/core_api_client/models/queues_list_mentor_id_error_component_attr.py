from enum import Enum


class QueuesListMentorIdErrorComponentAttr(str, Enum):
    MENTOR_ID = "mentor__id"

    def __str__(self) -> str:
        return str(self.value)
