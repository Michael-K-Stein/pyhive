from enum import Enum


class AssignmentsListUserProgramIdInErrorComponentAttr(str, Enum):
    USER_PROGRAM_ID_IN = "user__program__id__in"

    def __str__(self) -> str:
        return str(self.value)
