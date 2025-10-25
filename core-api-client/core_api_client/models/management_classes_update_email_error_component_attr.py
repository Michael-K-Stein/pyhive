from enum import Enum


class ManagementClassesUpdateEmailErrorComponentAttr(str, Enum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
