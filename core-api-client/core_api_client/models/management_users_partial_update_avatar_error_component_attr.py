from enum import Enum


class ManagementUsersPartialUpdateAvatarErrorComponentAttr(str, Enum):
    AVATAR = "avatar"

    def __str__(self) -> str:
        return str(self.value)
