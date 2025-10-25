from enum import Enum


class HelpListUserClassesIdInErrorComponentAttr(str, Enum):
    USER_CLASSES_ID_IN = "user__classes__id__in"

    def __str__(self) -> str:
        return str(self.value)
