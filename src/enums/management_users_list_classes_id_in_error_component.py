from enum import Enum


class ManagementUsersListClassesIdInErrorComponentCode(str, Enum):
    INVALID_CHOICE = "invalid_choice"
    INVALID_LIST = "invalid_list"
    INVALID_PK_VALUE = "invalid_pk_value"

    def __str__(self) -> str:
        return str(self.value)
