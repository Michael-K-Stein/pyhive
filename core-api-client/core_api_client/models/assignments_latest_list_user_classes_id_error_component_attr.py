from enum import Enum


class AssignmentsLatestListUserClassesIdErrorComponentAttr(str, Enum):
    USER_CLASSES_ID = "user__classes__id"

    def __str__(self) -> str:
        return str(self.value)
