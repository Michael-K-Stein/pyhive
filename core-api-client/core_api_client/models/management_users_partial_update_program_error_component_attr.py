from enum import Enum


class ManagementUsersPartialUpdateProgramErrorComponentAttr(str, Enum):
    PROGRAM = "program"

    def __str__(self) -> str:
        return str(self.value)
