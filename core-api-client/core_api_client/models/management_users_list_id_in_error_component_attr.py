from enum import Enum


class ManagementUsersListIdInErrorComponentAttr(str, Enum):
    ID_IN = "id__in"

    def __str__(self) -> str:
        return str(self.value)
