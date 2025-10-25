from enum import Enum


class ManagementUsersCreateCheckersBriefErrorComponentAttr(str, Enum):
    CHECKERS_BRIEF = "checkers_brief"

    def __str__(self) -> str:
        return str(self.value)
