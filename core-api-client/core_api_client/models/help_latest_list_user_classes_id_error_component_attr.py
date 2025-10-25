from enum import Enum


class HelpLatestListUserClassesIdErrorComponentAttr(str, Enum):
    USER_CLASSES_ID = "user__classes__id"

    def __str__(self) -> str:
        return str(self.value)
