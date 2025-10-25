from enum import Enum


class ManagementUsersPartialUpdateAvatarErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NO_NAME = "no_name"

    def __str__(self) -> str:
        return str(self.value)
