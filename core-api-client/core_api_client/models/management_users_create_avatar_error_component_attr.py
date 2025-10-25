from enum import Enum


class ManagementUsersCreateAvatarErrorComponentAttr(str, Enum):
    AVATAR = "avatar"

    def __str__(self) -> str:
        return str(self.value)
