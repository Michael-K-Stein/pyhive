from enum import Enum


class ManagementClassesPartialUpdateEmailErrorComponentAttr(str, Enum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
