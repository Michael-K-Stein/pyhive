from enum import Enum


class ManagementClassesCreateEmailErrorComponentAttr(str, Enum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
