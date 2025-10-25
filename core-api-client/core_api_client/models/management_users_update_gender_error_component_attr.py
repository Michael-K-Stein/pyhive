from enum import Enum


class ManagementUsersUpdateGenderErrorComponentAttr(str, Enum):
    GENDER = "gender"

    def __str__(self) -> str:
        return str(self.value)
