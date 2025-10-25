from enum import Enum


class ManagementUsersPartialUpdateGenderErrorComponentAttr(str, Enum):
    GENDER = "gender"

    def __str__(self) -> str:
        return str(self.value)
