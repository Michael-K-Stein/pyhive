from enum import Enum


class ManagementClassesCreateProgramErrorComponentAttr(str, Enum):
    PROGRAM = "program"

    def __str__(self) -> str:
        return str(self.value)
