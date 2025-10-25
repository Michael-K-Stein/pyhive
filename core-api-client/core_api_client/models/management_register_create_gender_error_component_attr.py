from enum import Enum


class ManagementRegisterCreateGenderErrorComponentAttr(str, Enum):
    GENDER = "gender"

    def __str__(self) -> str:
        return str(self.value)
