from enum import Enum


class ManagementClassesUpdateTypeErrorComponentAttr(str, Enum):
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
