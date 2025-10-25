from enum import Enum


class ManagementUsersCreateClassesErrorComponentCode(str, Enum):
    DOES_NOT_EXIST = "does_not_exist"
    INCORRECT_TYPE = "incorrect_type"
    NOT_A_LIST = "not_a_list"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
