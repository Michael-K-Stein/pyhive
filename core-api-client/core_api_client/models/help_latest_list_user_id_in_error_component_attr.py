from enum import Enum


class HelpLatestListUserIdInErrorComponentAttr(str, Enum):
    USER_ID_IN = "user__id__in"

    def __str__(self) -> str:
        return str(self.value)
