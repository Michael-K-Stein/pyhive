from enum import Enum


class ManagementClassesListProgramIdInErrorComponentAttr(str, Enum):
    PROGRAM_ID_IN = "program__id__in"

    def __str__(self) -> str:
        return str(self.value)
