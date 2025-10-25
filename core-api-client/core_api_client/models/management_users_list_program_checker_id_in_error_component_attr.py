from enum import Enum


class ManagementUsersListProgramCheckerIdInErrorComponentAttr(str, Enum):
    PROGRAM_CHECKER_ID_IN = "program_checker__id__in"

    def __str__(self) -> str:
        return str(self.value)
